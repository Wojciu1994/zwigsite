# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DocumentForm(forms.Form):
    docfile = forms.FileField()

class MailForm (forms.Form):
	name = forms.EmailField()
	id = forms.IntegerField()
