from django.contrib import admin

# Register your models here.
from .models import baiviet

admin.site.register(baiviet)

class quill(admin.ModelAdmin):
    pass