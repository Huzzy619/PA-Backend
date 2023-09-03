from django.db import transaction

from .models import Wallet


def credit_wallet(user, amount):
    wallet = Wallet.objects.select_for_update().get(user=user)
    with transaction.atomic():
        wallet.balance += amount
        wallet.save()


def debit_wallet(user, amount):
    wallet = Wallet.objects.select_for_update().get(user=user)
    with transaction.atomic():
        wallet.balance -= amount
        wallet.save()
