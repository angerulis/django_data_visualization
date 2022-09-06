from django.db import models
from django.forms import ModelForm
from django import forms
import designer.models
from designer.models import Indicateur, TypeIndicateur, Modele


class LayoutForm(forms.Form):
    modele_title = forms.CharField(max_length=100, widget=forms.HiddenInput)
    layout_dict = forms.JSONField(widget=forms.HiddenInput)

