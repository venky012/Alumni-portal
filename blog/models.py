from django.db import models
from django.utils import timezone
from accounts.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'id': self.pk})

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', related_name='replies',null=True, blank=True,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog-home')

    def __str__(self):
        return self.text


