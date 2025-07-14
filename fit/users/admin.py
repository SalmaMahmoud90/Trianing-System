from django.contrib import admin
from .models import MainUser, Trainer, Trainee, Course, Enrollment
# Register your models here.

admin.site.register(MainUser)
admin.site.register(Trainer)
admin.site.register(Trainee)
admin.site.register(Course)
admin.site.register(Enrollment)