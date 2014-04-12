from django.contrib.auth.models import User
from django.db import models

from blog.models.base import CreatedAtAndUpdatedAtModel
from blog.models.fields import AutoSlugField


class Article(CreatedAtAndUpdatedAtModel):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(fields=['title'], editable=False)
    author = models.ForeignKey(User, related_name='articles', editable=False)
    content = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'blog'
        ordering = ['-id']
