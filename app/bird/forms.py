from datetime import date

from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Bird, FallenBird
from pictures.models import Picture


class DateInput(forms.DateInput):
    input_type = "date"


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ["image"]


class BirdAddForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        widgets = {
            "date_found": DateInput(
                format="%Y-%m-%d", attrs={"value": date.today}
            ),
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
            "status_mediation",
            "diagnosis_finding",
            "diagnosis_doctor",
            "comment",
            "picture",
        ]
        labels = {
            "bird_identifier": _("Kennung"),
            "bird": _("Taubenart"),
            "age": _("Alter"),
            "sex": _("Geschlecht"),
            "date_found": _("Funddatum"),
            "place": _("Fundort"),
            "status": _("Status"),
            "status_mediation": _("Vermittlung"),
            "finder": _("Finder"),
            "find_circumstances": _("Fundumstände"),
            "comment": _("Bemerkung"),
            "picture": _("Bild"),
        }

    def __init__(self, *args, **kwargs):
        super(BirdAddForm, self).__init__(*args, **kwargs)
        self.fields["bird"].initial = Bird.objects.get(name="Stadttaube")
        self.fields["picture"].widget.attrs["multiple"] = True
        self.fields["picture"].label = _("Bilder")


class BirdEditForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

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
            "status_mediation",
            "status_changed",
            "diagnosis_finding",
            "diagnosis_doctor",
            "comment",
            "picture",
        ]
        labels = {
            "bird_identifier": _("Kennung"),
            "bird": _("Taubenart"),
            "age": _("Alter"),
            "sex": _("Geschlecht"),
            "date_found": _("Funddatum"),
            "place": _("Fundort"),
            "status": _("Status"),
            "status_mediation": _("Vermittlung"),
            "finder": _("Finder"),
            "find_circumstances": _("Fundumstände"),
            "comment": _("Bemerkung"),
            "picture": _("Bild"),
        }

    def __init__(self, *args, **kwargs):
        super(BirdEditForm, self).__init__(*args, **kwargs)
        self.fields["picture"].widget.attrs["multiple"] = True
        self.fields["picture"].label = _("Bilder")
