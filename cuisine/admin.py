from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Cuisine)
admin.site.register(models.Comment)
admin.site.register(models.Contact)