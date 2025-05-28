# library/forms.py
from django import forms

from .models import (
    Composer,
    Arranger,
    Genre,
    Publisher,
    LoaningOrganization,
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


class LoaningOrganizationForm(forms.ModelForm):
    class Meta:
        model = LoaningOrganization
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
            "date_acquired": forms.DateInput(attrs={"type": "date"}),
            "loan_start_date": forms.DateInput(attrs={"type": "date"}),
            "expected_return_date": forms.DateInput(attrs={"type": "date"}),
            "rental_start_date": forms.DateInput(attrs={"type": "date"}),
            "rental_end_date": forms.DateInput(attrs={"type": "date"}),
            "borrowing_start_date": forms.DateInput(attrs={"type": "date"}),
            "expected_borrowing_return_date": forms.DateInput(attrs={"type": "date"}),
        }
