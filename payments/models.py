from django.db import models
from django.contrib.auth import get_user_model




class Wallet(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.DO_NOTHING)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Transaction():
    ...