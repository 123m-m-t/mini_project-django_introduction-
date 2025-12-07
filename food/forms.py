from django import forms
from .models import Reservation

TIME_SLOTS = [
    ("08-10", "8 AM TO 10 AM"),
    ("10-12", "10 AM TO 12 PM"),
    ("12-14", "12 PM TO 2 PM"),
    ("14-16", "2 PM TO 4 PM"),
    ("16-18", "4 PM TO 6 PM"),
    ("18-20", "6 PM TO 8PM"),
    ("20-22", "8 PM TO 10 PM"),
    ("22-24", "10 PM TO 12 AM"),
]

class ReservationForm(forms.ModelForm):
    time_slot = forms.ChoiceField(choices=TIME_SLOTS)

    class Meta:
        model = Reservation
        fields = ["name", "email", "persons", "phone", "date", "time_slot", "note"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name *"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email address *"}),
            "persons": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Persons *", "min": 1}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone number *"}),
            "date": forms.DateInput(attrs={"class": "form-control", "placeholder": "Date *", "type": "date"}),
            "note": forms.Textarea(attrs={"class": "form-control", "placeholder": "Your Note", "rows": 4}),
        }
