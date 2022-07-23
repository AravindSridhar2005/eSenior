

# Register your models here.
from django.contrib import admin
from .models import Reminder

class ReminderAdmin(admin.ModelAdmin):
    fields = ('date', 'text')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
        
admin.site.register(Reminder) 
