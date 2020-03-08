from django.db import models
from accounts.models import User

# Create your models here.


class Jobs_details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    last_date = models.DateField()
    company = models.CharField(max_length=50)
    place = models.CharField(max_length= 50)
    experience = models.CharField(max_length = 50)
    salary = models.CharField(max_length = 20)

    def __str__(self):
        return self.user.username
