from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from core.models import BaseUser, Assistant


@receiver(post_save, get_user_model())
def create_profiles(*args, **kwargs):
    if kwargs['created']:
        if kwargs['instance'].is_assistant:
            Assistant.objects.create(user_ptr = kwargs['instance'])
        else:
            BaseUser.objects.create(user_ptr = kwargs['instance'])

