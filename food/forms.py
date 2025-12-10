from django import forms
from .models import Reservation
from datetime import date,datetime
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from mysite import settings


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
    time_slot = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["date"].widget.attrs["min"] = date.today().isoformat()

        selected_date = None

        if "date" in self.data:
            selected_date = self.data.get("date")
        else:
            selected_date = date.today().isoformat()

        max_per_slot = getattr(settings, "RESERVATION_MAX_PER_SLOT", 5)

        available_slots = []

        current_time = datetime.now().time()
        current_hour = current_time.hour

        for slug, label in TIME_SLOTS:

            start_hour = int(slug.split("-")[0])
            if selected_date == date.today().isoformat():
                if start_hour <= current_hour:
                    continue

            count = Reservation.objects.filter(date=selected_date, time_slot=slug).count()
            if count < max_per_slot:
                available_slots.append((slug, label))

        self.fields["time_slot"].choices = available_slots

    def clean(self):
        cleaned_data = super().clean()
        selected_date = cleaned_data.get("date")
        selected_time = cleaned_data.get("time_slot")

        if selected_date and selected_time:

            count = Reservation.objects.filter(
                date=selected_date,
                time_slot=selected_time
            ).count()

            MAX = getattr(settings, "RESERVATION_MAX_PER_SLOT", 5)

            if count >= MAX:
                raise ValidationError(
                    f"Time slot {selected_time} is fully booked. Please choose another time."
                )

    def clean_time_slot(self):
        time_slot = self.cleaned_data["time_slot"]

        start_hour = int(time_slot.split("-")[0])

        if start_hour < 8 or start_hour >= 24:
            raise ValidationError("The selected time is outside of allowed reservation hours.")

        return time_slot

    def clean_date(self):
        selected_date = self.cleaned_data["date"]
        if selected_date < date.today():
            raise ValidationError("You cannot select a past date.")
        return selected_date

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


class ReservationAdminForm(forms.ModelForm):
    def clean_time_slot(self):
        time_slot = self.cleaned_data["time_slot"]
        start_hour = int(time_slot.split("-")[0])

        if start_hour < 8 or start_hour >= 24:
            raise ValidationError("Invalid time slot.")
        return time_slot

    def clean(self):
        cleaned_data = super().clean()
        selected_date = cleaned_data.get("date")
        selected_time = cleaned_data.get("time_slot")

        if selected_date and selected_time:
            count = Reservation.objects.filter(
                date=selected_date,
                time_slot=selected_time
            ).count()

            MAX = getattr(settings, "RESERVATION_MAX_PER_SLOT", 5)

            if count >= MAX:
                raise ValidationError("This time slot is fully booked.")
    class Meta:
        model = Reservation
        fields = "__all__"
        widgets = {
            "date": AdminDateWidget(),
            "time_slot": AdminTimeWidget(),
        }

    def clean_date(self):
        selected_date = self.cleaned_data["date"]
        if selected_date < date.today():
            raise ValidationError("You cannot select a past date.")
        return selected_date