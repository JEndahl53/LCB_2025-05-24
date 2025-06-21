# concerts/forms.py
from django import forms
from .models import Conductor, Guest, Venue, Concert, ConcertProgram


class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = "__all__"


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = "__all__"


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"


class ConcertForm(forms.ModelForm):
    class Meta:
        model = Concert
        fields = ["title", "date", "time", "venue", "poster", "description"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "datetime-local"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes to form fields
        for field_name, field in self.fields.items():
            if field_name == "description":
                field.widget.attrs["class"] = (
                    "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                )
            else:
                field.widget.attrs["class"] = (
                    "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                )


class ConcertProgramForm(forms.ModelForm):
    class Meta:
        model = ConcertProgram
        fields = ["music", "performance_order"]
