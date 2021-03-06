import datetime

from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = HTMLField()
    image = models.ImageField(blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.published_date<= now

    was_published_recently.admin_order_field = 'published_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

