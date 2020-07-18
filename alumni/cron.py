from django.conf import settings
from accounts.models import User

from django_cron import CronJobBase, Schedule

from alumni.profile_getter import getProfile
from linkedin_api import Linkedin
import time
from accounts.models import User

class MyCronJob(CronJobBase):

    RUN_EVERY_MINS = 0 if settings.DEBUG else 0   # 6 hours when not DEBUG
    RETRY_AFTER_FAILURE_MINS = 5
    
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    # schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'cron.MyCronJob'

    def do(self):
        # pass
        obj = User.objects.all()
        try:
            api = Linkedin('xerito4377@invql.com', 'marvm123')
        except:
            print("Unable to handle linkedin api check for network connections...")
            api = ''
        for i in obj:
            if i.linkedin_url:
                username = i.username
                profile_link = i.linkedin_url
                profile_link = 'https://www.linkedin.com/in/venkatesh-poojari-984007181/'
                profile_link = profile_link.replace('https://www.linkedin.com/in/','').replace('/','')
                try:
                    profile = api.get_profile(profile_link)
                except:
                    profile = ""  
                getProfile(username,profile)
                time.sleep(2)


  