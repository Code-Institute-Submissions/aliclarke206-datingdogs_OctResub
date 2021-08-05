from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile

# Create your models here.


class DirectMessage(models.Model):

    class Meta:
        ordering = ['-send_date']

    sender = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='sent_messages')
    recipient = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='received_messages')
    content = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
