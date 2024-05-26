from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matric_number = models.CharField(max_length=15, unique=True)
    bluetooth_address = models.CharField(max_length=17, unique=True, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=100)
    contact_bluetooth_address = models.CharField(max_length=17, unique=True)

    def __str__(self):
        return self.contact_name
