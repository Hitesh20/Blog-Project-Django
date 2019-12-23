from django.db.models.signals import post_save           ##this gets fired after an object is saved
from django.contrib.auth.models import User             ## will act as sender
from django.dispatch import receiver
from .models import Profile



#To create a profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):             #kwargs just take extra parameters if passed
    if created:
        Profile.objects.create(user = instance)

#To save a profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

