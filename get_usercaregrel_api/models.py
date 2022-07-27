from django.db import models
from django.conf import settings
from datetime import date

# Create your models here.
class UserCareRel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='usercarerel_user',
        on_delete=models.CASCADE,
    )
    caregiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='usercarerel_careg',
        on_delete=models.CASCADE,
    )
    moneyowed = models.DecimalField(max_digits=7, decimal_places=2)
    timeworked = models.TimeField()