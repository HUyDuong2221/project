from email.policy import default
from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class baiviet(models.Model):
    tieude= models.CharField(max_length=100,blank=False)
    noidung = QuillField()
    def __str__(self):
        return self.tieude