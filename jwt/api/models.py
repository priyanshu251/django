from django.db import models
from django.contrib.auth.models import User # User from django.contrib.auth.models represents the default user model provided by Django. It already has fields like username, password, email, first_name, last_name, etc.
from django.db.models.signals import post_save # post_save from django.db.models.signals is a signal that gets sent after a model's save() method is called.
from django.dispatch import receiver #receiver from django.dispatch is a decorator used to connect signal handlers to signals.
from rest_framework.authtoken.models import Token
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)


