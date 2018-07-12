from django.contrib import admin

# Register your models here.
from .models import Session, Cycle

admin.site.register(Session)
admin.site.register(Cycle)