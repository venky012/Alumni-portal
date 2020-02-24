from django.db import models

# Create your models here.
class ContactForm_queries(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=54)
    subject=models.CharField(max_length=54)
    message = models.CharField(max_length=1154)

    def __str__(self):
        return str(self.email)

class ReplyForm_queries(models.Model):
    name=models.CharField(max_length=50,default = "name+default")
    email=models.EmailField(max_length=54,default = "email+default")
    subject=models.CharField(max_length=54,default = "subject+default")
    message = models.CharField(max_length=1154,default = "message+default")
    reply_message = models.CharField(max_length=1154)

    def __str__(self):
        return str(self.reply_message)