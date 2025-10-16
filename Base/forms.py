from django import forms
from Base.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = ['name', 'email', 'phone', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+91'
            }),
            'message': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message...'
            }),
        }
