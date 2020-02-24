from django.conf import settings
from django.contrib.auth.models import User

from django_common.helper import send_mail
from django_cron import CronJobBase, Schedule


class DeleteInactiveUsers(CronJobBase):
    """
    Send an email with the user count.
    """
    RUN_EVERY_MINS = 0 if settings.DEBUG else 1   # 6 hours when not DEBUG
    RETRY_AFTER_FAILURE_MINS = 5


    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'cron.DeleteInactiveUsers'

    def do(self):
        users = User.objects.all()
        for user in users:
            if user.is_active == False:
                print("inactiive user")
                user.delete()
        message = 'Active users: %d' % User.objects.count()
        print(message)
        # send_mail(
        #     '[django-cron demo] Active user count',
        #     message,
        #     'no-reply@django-cron-demo.com',
        #     ['test@django-cron-demo.com']
        # )