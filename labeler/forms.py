from django import forms


class ImageUploadForm(forms.Form):
    imagefile = forms.FileField(
        label='Select an image file',
    )
