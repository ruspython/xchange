from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.utils.translation import ugettext_lazy as _


class Referral(models.Model):
    user = models.ForeignKey(User)
    site_url = models.URLField()
    points = models.BigIntegerField(default=0, blank=True)

    def __str__(self):
        return self.user.username


class Banner(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    site_owner = models.ForeignKey(Referral, related_name='banner_site_owner', blank=True)
    banner_owner = models.ForeignKey(Referral, blank=True)
    url = models.URLField()
    picture = models.ImageField(upload_to='pictures', blank=True, verbose_name=_('banner picture'))
    #picture = ResizedImageField(max_height=800, max_width=600, upload_to='banners/pictures')

    def __str__(self):
        return self.title