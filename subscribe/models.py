import uuid

from django.db import models
from django_countries.fields import CountryField

from profiles.models import UserProfile


# Create your models here.

class Subscription(models.Model):
    member_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='subscription')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_member_number(self):
        """
        Generate a random, unique member number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the member number
        if it hasn't been set already.
        """
        if not self.member_number:
            self.member_number = self._generate_member_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.member_number
