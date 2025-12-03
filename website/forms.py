from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            "message": forms.Textarea(attrs={
                "class": "form-control w-100",
                "placeholder": "Enter Message",
                "cols": 30,
                "rows": 9,
            }),
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email address",
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Subject",
            }),
        }

    def clean_subject(self):
        subject = self.cleaned_data.get("subject")
        if not subject or subject.strip() == "":
            return "No Subject"
        return subject
