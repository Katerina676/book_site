from django import forms
from .models import Mail


class MailForm(forms.ModelForm):

    class Meta:
        model = Mail
        fields = ("email",)
        widgets = {
            "email": forms.TextInput(attrs={"class": "editContent", "placeholder": "Your Email..."})
        }
        labels = {
            "email": ''
        }