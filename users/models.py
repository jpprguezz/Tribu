from django.conf import settings
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    avatar = models.ImageField(
        blank=True, null=True, upload_to='avatars', default='avatars/noavatar.png'
    )
    bio = models.TextField(blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.bio

    def get_absolute_url(self):
        return reverse('users:user_detail', kwargs={'username': self.username})
