from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

# This block defines a signal handler function create_auth_token using the @receiver decorator.
@receiver(post_save, sender=User) # this is a signal which is sent by django when a user is created. post_save is the signal that triggers this handler when a model instance is saved.
#sender=User specifies that the handler is connected to the User model
def create_auth_token(sender, instance=None, created=False, **kwargs): # The function takes parameters: sender is the model class, instance is the saved instance, created is a boolean indicating if the instance was created, and **kwargs captures any additional keyword arguments.
    if created:
        Token.objects.create(user=instance) # The function checks if the User instance was created (created=True), and if so, it creates a corresponding authentication token for that user using Token.objects.create(user=instance).
