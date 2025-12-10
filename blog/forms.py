from django import forms

from food.models import Reservation
from .models import Comment,Post
from django.contrib.admin.widgets import AdminDateWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "subject", "message"]

        widgets = {
            "message": forms.Textarea(attrs={
                "class": "form-control w-100",
                "cols": 30,
                "rows": 9,
                "placeholder": "Write Comment"
            }),
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email"
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subject"
            }),
        }

    def clean_subject(self):
        subject = self.cleaned_data.get("subject", "")
        if not subject:
            return "No subject"
        return subject


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "updated_date": AdminDateWidget(),
        }