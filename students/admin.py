from django.contrib import admin
from .models import Profile, Question, Reason

admin.site.register(Profile)
admin.site.register(Reason)
admin.site.register(Question)