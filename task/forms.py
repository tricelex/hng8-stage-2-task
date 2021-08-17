from django.forms import forms, ModelForm, Textarea, TextInput, EmailInput

from task.models import ContactResponse


class ContactResponseForm(ModelForm):
    class Meta:
        model = ContactResponse
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Message'}),
        }
