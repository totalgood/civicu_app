from django import forms
from .models import Image


class ImageUploadForm(forms.Form):
    imagefile = forms.FileField(
        label='Select an image file',
    )


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('caption', 'file', 'uploaded_by')
