from django.forms import ModelForm
from django import forms
from .models import Image

class ImageUpload(ModelForm):
    class Meta:
        model= Image
        fields = ('Name','File')