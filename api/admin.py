from django.contrib import admin

from .models import Todos, Users

admin.site.register(Users)
admin.site.register(Todos)
