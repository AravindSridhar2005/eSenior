from django.db import models
from django.contrib import admin
from datetime import date
from django.conf import settings
# Create your models here.
class Reminder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reminders_user')
    date = models.DateTimeField()
    text = models.TextField(default="")

    def __str__(self):
        return self.name

class ReminderAdmin(admin.ModelAdmin):
    fields = ('date', 'text')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()