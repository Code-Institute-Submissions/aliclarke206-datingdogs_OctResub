from django.contrib import admin
from .models import Breed, Dog

# Register your models here.


class DogAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'image',
    )


class BreedAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Dog, DogAdmin)
admin.site.register(Breed, BreedAdmin)
