# library/forms.py
from django import forms

from .models import (
    Composer,
    Arranger,
    Genre,
    Publisher,
    LendingOrganization,
    BorrowingOrganization,
    RentingOrganization,
    Music,
)


class ComposerForm(forms.ModelForm):
    class Meta:
        model = Composer
        fields = "__all__"

        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
            "death_date": forms.DateInput(attrs={"type": "date"}),
        }


class ArrangerForm(forms.ModelForm):
    class Meta:
        model = Arranger
        fields = "__all__"

        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
            "death_date": forms.DateInput(attrs={"type": "date"}),
        }


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ("name",)


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"


class LendingOrganizationForm(forms.ModelForm):
    class Meta:
        model = LendingOrganization
        fields = "__all__"


class BorrowingOrganizationForm(forms.ModelForm):
    class Meta:
        model = BorrowingOrganization
        fields = "__all__"


class RentingOrganizationForm(forms.ModelForm):
    class Meta:
        model = RentingOrganization
        fields = "__all__"


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = "__all__"

        widgets = {
            "difficulty": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "date_acquired": forms.DateInput(attrs={"type": "date"}),
            "lend_start_date": forms.DateInput(attrs={"type": "date"}),
            "expected_return_date": forms.DateInput(attrs={"type": "date"}),
            "rental_start_date": forms.DateInput(attrs={"type": "date"}),
            "rental_end_date": forms.DateInput(attrs={"type": "date"}),
            "borrowing_start_date": forms.DateInput(attrs={"type": "date"}),
            "expected_borrowing_return_date": forms.DateInput(attrs={"type": "date"}),
            "duration": forms.TextInput(attrs={"placeholder": "mm:ss"}),
        }
