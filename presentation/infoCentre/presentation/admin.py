from django.contrib import admin

# Register your models here.
from .models import User,Question,Choice

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User)

