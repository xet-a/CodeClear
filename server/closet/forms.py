from django import forms
from .models import Closet

class ClosetCreateForm(forms.ModelForm):
    class Meta:
        model = Closet
        fields = ['clothes_name', 'clothes_category', 'clothes_color', 'clothes_image']