# common/forms.py
# forms shared between apps

from django import forms
from common.models import PersonBase


class PersonBaseForm(forms.ModelForm):
    """
    Form for creating and updating PersonBase instances.
    """

    class Meta:
        # Set the model dynamically in  __init__
        fields = [
            "first_name",
            "last_name",
            "comment",
            "types",
            "title",
            "middle_initial",
            "birth_date",
            "death_date",
        ]
        widgets = {
            "types": forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        # Extract the model class from kwargs, if provided
        self.person_model = kwargs.pop("model", None)

        # If no model is explicitly provided, use the one from Meta
        if not self.person_model and hasattr(self.Meta, "model"):
            self.person_model = self.Meta.model

        if not self.person_model:
            raise ValueError("You must set Meta.model in subclasses of PersonBaseForm")

        # Dynamically set the form's model
        self._meta.model = self.person_model

        super().__init__(*args, **kwargs)
        # Hide conductor-specific fields unless 'conductor' is selected
        data = self.data or self.initial
        types = (
            data.getlist("types") if hasattr(data, "getlist") else data.get("types", [])
        )
        # Accept both initial and POST data
        if not types:
            if self.instance.pk:
                types = self.instance.types.values_list("name", flat=True)

        # Only set th widget if the field actually exists in this form/model
        conductor_fields = ["title", "middle_initial"]
        composer_arranger_fields = ["birth_date", "death_date"]

        if "conductor" not in types and "conductor" not in [str(t) for t in types]:
            for f in conductor_fields:
                if f in self.fields:
                    self.fields[f].widget = forms.HiddenInput()
        if ("composer" not in types and "composer" not in [str(t) for t in types]) or (
            "arranger" not in types and "arranger" not in [str(t) for t in types]
        ):
            for f in composer_arranger_fields:
                if f in self.fields:
                    self.fields[f].widget = forms.HiddenInput()
