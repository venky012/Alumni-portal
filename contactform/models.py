from django.db import models

# Create your models here.
class ContactForm_queries(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=54)
    subject=models.CharField(max_length=54)
    message = models.CharField(max_length=1154)

    def __str__(self):
        return str(self.email)