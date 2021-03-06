from django import forms
from .models import Email, Us
from django.core.mail import EmailMessage


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email', 'attach','subject' ,'message']


    def _clean_email(self):
        email = self.cleaned_data.get('email')
        return email


    def _clean_subject(self):
        subject = self.cleaned_data.get('subject')
        return subject


    def _clean_message(self):
        message = self.cleaned_data.get('message')
        return message

    def _clean_attach(self):
        attach = self.cleaned_data.get('attach')
        return attach

class Usform(forms.ModelForm):
    class Meta:
        model= Us
        fields = ['user','password','valid']
