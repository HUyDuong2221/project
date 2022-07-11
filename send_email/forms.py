import email
from django import forms
from .models import send_mail

class contactForm(forms.ModelForm):
    class Meta:
        model = send_mail
        fields = ('name', 'email','content',)