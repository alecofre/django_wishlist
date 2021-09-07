from django.contrib import admin
from .models import User
from wishes_app.models import *

# Register your models here.
admin.site.register(User)
# admin.site.register(User, Item)