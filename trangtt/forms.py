from dataclasses import fields
from django_quill.forms import QuillFormField
from django import forms
from .models import baiviet

class baivietform(forms.Form):
    body = QuillFormField()
    
class thembaiviet(forms.ModelForm):
    class Meta:
        model = baiviet
        fields = ('tieude', 'noidung',)