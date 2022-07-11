from django.contrib import admin

# Register your models here.
from .models import send_mail

admin.site.register(send_mail)

class send_mail(admin.ModelAdmin):
    pass