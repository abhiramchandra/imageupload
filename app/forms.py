from django import forms 

from app.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'