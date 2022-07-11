from django.db import models

# Create your models here.
class send_mail(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.CharField(max_length=1000)
    
    