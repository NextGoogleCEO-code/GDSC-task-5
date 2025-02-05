from django.contrib import admin
from .models import Postmodel

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','date_created')
admin.site.register(Postmodel,PostModelAdmin)