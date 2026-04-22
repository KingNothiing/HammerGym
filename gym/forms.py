import re

from django import forms

from .models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    name_pattern = re.compile(r"^[A-Za-zА-Яа-яЁёІіЇїЄєҐґ' -]+$")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_attrs = {
            "full_name": {
                "autocomplete": "name",
                "maxlength": "120",
                "minlength": "2",
                "aria-describedby": "error-full_name",
            },
            "phone": {
                "autocomplete": "tel",
                "inputmode": "tel",
                "maxlength": "30",
                "aria-describedby": "error-phone",
            },
            "branch": {
                "aria-describedby": "error-branch",
            },
            "message": {
                "aria-describedby": "error-message",
            },
        }

        for name, field in self.fields.items():
            existing_classes = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = " ".join(
                filter(None, [existing_classes, "input-field"])
            )
            for attr_name, value in field_attrs.get(name, {}).items():
                field.widget.attrs.setdefault(attr_name, value)

        if self.is_bound:
            for name in self.errors:
                existing_classes = self.fields[name].widget.attrs.get("class", "")
                self.fields[name].widget.attrs["class"] = " ".join(
                    filter(None, [existing_classes, "error"])
                )
                self.fields[name].widget.attrs["aria-invalid"] = "true"

    class Meta:
        model = ContactRequest
        fields = ["full_name", "phone", "branch", "message"]
        labels = {
            "full_name": "Имя",
            "phone": "Телефон",
            "branch": "Филиал",
            "message": "Комментарий",
        }
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Ваше имя"}),
            "phone": forms.TextInput(attrs={"placeholder": "Например: +373 777 12 345"}),
            "message": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Например: хочу узнать про абонемент, тренера или подходящий филиал",
                }
            ),
        }
        error_messages = {
            "full_name": {
                "required": "Введите имя, чтобы мы понимали, как к вам обращаться.",
            },
            "phone": {
                "required": "Укажите номер телефона для связи.",
            },
        }

    def clean_full_name(self):
        full_name = " ".join(self.cleaned_data["full_name"].split())
        if len(full_name) < 2:
            raise forms.ValidationError("Имя должно содержать минимум 2 символа.")
        if not self.name_pattern.match(full_name):
            raise forms.ValidationError("Используйте только буквы, пробел, апостроф или дефис.")
        return full_name

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        digits_only = "".join(symbol for symbol in phone if symbol.isdigit())
        if len(digits_only) < 5:
            raise forms.ValidationError("Укажите телефон в понятном формате, чтобы мы могли связаться с вами.")
        return phone

    def clean_message(self):
        return self.cleaned_data["message"].strip()
