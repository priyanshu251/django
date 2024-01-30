from django.db import models
from django.contrib.auth.models import User # User from django.contrib.auth.models represents the default user model provided by Django. It already has fields like username, password, email, first_name, last_name, etc.
from django.db.models.signals import post_save # post_save from django.db.models.signals is a signal that gets sent after a model's save() method is called.
from django.dispatch import receiver #receiver from django.dispatch is a decorator used to connect signal handlers to signals.
from rest_framework.authtoken.models import Token
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

# This code uses Django's signal mechanism to create an authentication token for a user when a User instance is saved.
@receiver(post_save, sender=User) # this is a signal which is sent by django when a user is created. post_save is the signal that triggers this handler when a model instance is saved.
#sender=User specifies that the handler is connected to the User model
def create_auth_token(sender, instance=None, created=False, **kwargs): # The function takes parameters: sender is the model class, instance is the saved instance, created is a boolean indicating if the instance was created, and **kwargs captures any additional keyword arguments.
    if created:
        Token.objects.create(user=instance) # The function checks if the User instance was created (created=True), and if so, it creates a corresponding authentication token for that user using Token.objects.create(user=instance).





# detailed explaination of signals
        
  # Signals allow certain senders to notify a set of receivers that some action has taken place. They’re especially useful when many pieces of code may be interested in the same events.
        
  # @receiver(post_save, sender=User): This is a decorator that connects the create_auth_token function to the post_save   signal emitted by the User model. The post_save signal is sent after a model's save method is successfully called. In   this case, it specifies that the create_auth_token function should be called whenever a User instance is saved.
        
  # def create_auth_token(sender, instance=None, created=False, **kwargs):: This function is the signal handler. It is   called when the post_save signal is emitted for the User model.

  # sender: The model class that sent the signal (User in this case).
        
  # instance: The actual instance of the model that was saved. It represents the User instance in this context.
        
  # created: A boolean indicating whether the instance was created (True if the instance is newly created, False if it   already existed and was updated).
        
  # **kwargs: A catch-all for any additional keyword arguments. In this case, it allows the function to accept any   additional parameters that may be passed by the signal.
        
  # if created: Token.objects.create(user=instance): This condition checks if the User instance was newly created. If   created is True, it means a new User instance was just created, and the code inside the block will execute.

  # Token.objects.create(user=instance): This line creates a new authentication token for the user (instance) using the   Token.objects.create() method. It associates the token with the specific user.
        
  # In summary, this signal handler function is connected to the post_save signal of the User model. Whenever a new User   instance is created, it responds by creating a corresponding authentication token for that user using the Token.objects.  create() method. This is a common pattern in Django for automatically performing actions in response to certain events   (such as saving a model instance).