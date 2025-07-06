from django.contrib import admin
from .models import MainUser, Trainer, Trainee
# Register your models here.

admin.site.register(MainUser)
admin.site.register(Trainer)
admin.site.register(Trainee)