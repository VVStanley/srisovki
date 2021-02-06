from PIL import Image

from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.core.exceptions import FieldError, ValidationError

from posts.models import Post

User = get_user_model()


class UserSettingsForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['avatar', 'date_birthday', 'city']
        widgets = {
            'city': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ведите ваш город'}
            ),
            'date_birthday': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format=('%Y-%m-%d')),
            'avatar': forms.FileInput(attrs={'class': 'form-control-uniform-custom'})}


class UserAddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image', 'name']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Предложите свое название'}
            ),
            'image': forms.FileInput(
                attrs={'class': 'form-control-uniform-custom'}
            )}
