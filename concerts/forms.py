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
        fields = "__all__"


class ConcertProgramForm(forms.ModelForm):
    class Meta:
        model = ConcertProgram
        fields = ["music", "performance_order"]
