from django.conf import settings
from accounts.models import User

from django_common.helper import send_mail
from django_cron import CronJobBase, Schedule

from alumni.profile_getter import getProfile
from linkedin_api import Linkedin


class MyCronJob(CronJobBase):

    RUN_EVERY_MINS = 1 if settings.DEBUG else 1   # 6 hours when not DEBUG
    RETRY_AFTER_FAILURE_MINS = 5
    
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    # schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'cron.MyCronJob'

    def do(self):
        print("inside do")
        # users = User.objects.all()
        # for user in users:
        #     if user.is_active == False:
        #         print("inactiive user")
        #         user.delete()
        # message = 'Active users: %d' % User.objects.count()
        # print(message)
        # send_mail(
        #     '[django-cron demo] Active user count',
        #     message,
        #     'poojariv53@gmail.com', ['poojariv53@gmail.com']
        # )
        
        # profile_link = 'https://www.linkedin.com/in/venkatesh-poojari-984007181/'
        # profile_link = profile_link.replace('https://www.linkedin.com/in/','').replace('/','')
        # print(profile_link)
        
        # getProfile(profile_link)