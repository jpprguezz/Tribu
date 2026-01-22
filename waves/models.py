from django.conf import settings
from django.db import models
from django.urls import reverse


class Wave(models.Model):
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='waves', on_delete=models.CASCADE
    )
    echo = models.ForeignKey('echos.Echo', related_name='waves', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('waves:waves-details', kwargs={'wave_pk': self.pk})

    class Meta:
        ordering = ['-created_at']
