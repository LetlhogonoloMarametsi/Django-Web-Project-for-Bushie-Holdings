from django import forms
from django.forms import ModelForm
from .models import Contact

#create a class for form


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
