from django.db import models
from django.utils import timezone


class DonatorInfo(models.Model):
    donator_name = models.CharField(max_length=50)
    amount = models.IntegerField()
    description = models.TextField()
    date_donated = models.DateTimeField(default=timezone.now)
    total_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.donator_name
