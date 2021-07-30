from django.contrib import admin
from .models import Subscription
# Register your models here.


class subscriptionAdmin(admin.ModelAdmin):

    readonly_fields = ('member_number', 'date',
                       'grand_total',)

    fields = ('member_number', 'date', 'full_name',
              'email', 'town_or_city', 'county', 'grand_total',)

    list_display = ('member_number', 'date', 'full_name',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Subscription)
