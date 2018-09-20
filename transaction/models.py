# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from service.models import Order
from users.models import User


class Transaction(models.Model):
    # Options for transaction type
    KASH_DEPOSIT = 0
    WALLET_TRANSACTION = 2
    USER_KASH_REFUND = 3
    USER_KASH_PAYMENT = 4
    USER_CASH_PAYMENT = 5
    USER_KASH_DEPOSIT = 6

    TRANSACTION_CHOICES = (
        (KASH_DEPOSIT, "Recharge"), (WALLET_TRANSACTION, "Friendly Transfer"),
        (USER_KASH_REFUND, "Vendor Refund"), (USER_KASH_PAYMENT, "User Payment"),
        (USER_CASH_PAYMENT, "Cash Payment"))
    sender = models.ForeignKey(User, related_name='sent_transactions')
    receiver = models.ForeignKey(User, related_name='received_transactions')
    amount = models.FloatField()
    transaction_type = models.IntegerField(choices=TRANSACTION_CHOICES)
    transaction_hash = models.CharField(max_length=1024, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


class PaymentRequest(models.Model):
    user = models.ForeignKey(User, related_name='requested_payments')
    payee = models.ForeignKey(User, related_name='received_payments')
    amount = models.FloatField()
    order = models.ForeignKey(Order, related_name='payments', null=True, blank=True)
    transaction = models.OneToOneField(Transaction, related_name='payment', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
