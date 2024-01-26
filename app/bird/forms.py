from datetime import date

from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Bird, FallenBird


class DateInput(forms.DateInput):
    input_type = "date"


class BirdAddForm(forms.ModelForm):
    class Meta:
        widgets = {
            "date_found": DateInput(format="%Y-%m-%d", attrs={"value": date.today}),
            "diagnosis_finding": forms.Textarea(attrs={"rows": 3}),
            "diagnosis_doctor": forms.Textarea(attrs={"rows": 3}),
            "comment": forms.Textarea(attrs={"rows": 3}),
        }
        model = FallenBird
        fields = [
            "bird_identifier",
            "bird",
            "age",
            "sex",
            "date_found",
            "place_found",
            "place_found_other",
            "finder",
            "find_circumstances",
            "find_circumstances_other",
            "status",
            "diagnosis_finding",
            "diagnosis_doctor",
            "comment",
        ]
        labels = {
            "bird_identifier": _("Kennung"),
            "bird": _("Taubenart"),
            "age": _("Alter"),
            "sex": _("Geschlecht"),
            "date_found": _("Funddatum"),
            "place": _("Fundort"),
            "status": _("Status"),
            "finder": _("Finder"),
            "find_circumstances": _("Fundumstände"),
            "comment": _("Bemerkung"),
        }

    def __init__(self, *args, **kwargs):
        super(BirdAddForm, self).__init__(*args, **kwargs)
        self.fields["bird"].initial = Bird.objects.get(name="Stadttaube")


class BirdEditForm(forms.ModelForm):
    class Meta:
        widgets = {
            "date_found": DateInput(format="%Y-%m-%d"),
            "status_changed": DateInput(format="%Y-%m-%d"),
            "diagnosis_finding": forms.Textarea(attrs={"rows": 3}),
            "diagnosis_doctor": forms.Textarea(attrs={"rows": 3}),
            "comment": forms.Textarea(attrs={"rows": 3}),
        }
        model = FallenBird
        fields = [
            "bird_identifier",
            "bird",
            "age",
            "sex",
            "date_found",
            "place_found",
            "place_found_other",
            "finder",
            "find_circumstances",
            "find_circumstances_other",
            "status",
            "status_changed",
            "diagnosis_finding",
            "diagnosis_doctor",
            "comment",
        ]
        labels = {
            "bird_identifier": _("Kennung"),
            "bird": _("Taubenart"),
            "age": _("Alter"),
            "sex": _("Geschlecht"),
            "date_found": _("Funddatum"),
            "place": _("Fundort"),
            "status": _("Status"),
            "finder": _("Finder"),
            "find_circumstances": _("Fundumstände"),
            "comment": _("Bemerkung"),
        }
