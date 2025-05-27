# common/forms.py
# forms shared between apps

from django import forms
from common.models import PersonBase


class PersonBaseForm(forms.ModelForm):
    """
    Form for creating and updating PersonBase instances.
    """

    class Meta:
        model = PersonBase
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
        if "conductor" not in types and "conductor" not in [
            str(t) for t in types
        ]:  # Hide conductor-specific fields
            self.fields["title"].widget = forms.HiddenInput()
            self.fields["middle_initial"].widget = forms.HiddenInput()
        elif (
            "composer" not in types and "composer" not in [str(t) for t in types]
        ) or ("arranger" not in types and "arranger" not in [str(t) for t in types]):
            # Hide composer/arranger-specific fields
            self.fields["birth_date"].widget = forms.HiddenInput()
            self.fields["death_date"].widget = forms.HiddenInput()
