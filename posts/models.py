from django.db import models
from django.core.urlresolvers import reverse


def upload_location(instance, filename):
    return '%s/%s' % (instance.id, filename)


class Post(models.Model):

    class Meta:
        ordering = ['-timestamp', 'updated']

    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'id':self.id})

    def __str__(self):
        return self.title
