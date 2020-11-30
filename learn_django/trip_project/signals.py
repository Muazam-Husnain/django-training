from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='regular')
        instance.groups.add(group)
        instance.save()
        Profile.objects.create(user=instance)

