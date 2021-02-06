from django import forms

from front.models import FeedbackModel


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = FeedbackModel
        fields = ['name', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Сообщение'}), }
