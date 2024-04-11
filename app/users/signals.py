from django.db.models.signals import post_save #signal fired after object was saved
from django.contrib.auth.models import User # sender of the signal
from django.dispatch import receiver # function that gets the signal
from .models import Profile

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def saveProfile(sender, instance, **kwargs):
  instance.profile.save()