from django.db import models
from django.utils import timezone
class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '<Title: {}, ID: {}'.format(self.title, self.id)

