from django.contrib import admin

# Register your models here.

from .models import UserProfile, Contact

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'matric_number', 'bluetooth_address')
    search_fields = ('user__username', 'matric_number')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_name', 'contact_bluetooth_address')
    search_fields = ('user__username', 'contact_name', 'contact_bluetooth_address')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Contact, ContactAdmin)
