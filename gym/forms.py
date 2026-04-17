from django import forms

from .models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'input-field')

    class Meta:
        model = ContactRequest
        fields = ['full_name', 'phone', 'branch', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон'}),
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Например: хочу узнать про абонемент, тренера или филиал'}),
        }
