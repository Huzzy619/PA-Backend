from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Wallet


@receiver(post_save, sender = get_user_model())
def create_wallet(*args, **kwargs):
    if kwargs['created']:
        Wallet.objects.create(user = kwargs['instance'])
        
