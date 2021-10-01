from django.db import models


class Breed(models.Model):

    class Meta:
        verbose_name_plural = 'Breeds'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Dog(models.Model):

    class Meta:
        verbose_name_plural = 'Dogs'

    breed = models.ForeignKey('Breed', null=True, blank=True,
                              on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    location = models.CharField(max_length=254, null=True, blank=True)
    age = models.DecimalField(max_digits=6, decimal_places=0)
    phone = models.CharField(max_length=254, null=True, blank=True)
    type = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
