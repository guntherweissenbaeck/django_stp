import csv
from datetime import date

from bird.models import FallenBird
from costs.models import Costs
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


today = date.today().strftime("%Y-%m-%d")


@login_required(login_url="account_login")
def site_exports(request):
    return render(request, "export/overview.html")


@login_required(login_url="account_login")
def export_costs(request):
    costs = Costs.objects.all().values_list(
        "id_bird__bird_identifier", "costs", "created", "comment", "user__username"
    )
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f"attachment, filename=stp_costs_{today}.csv"
    writer = csv.writer(response)
    writer.writerow(
        ["Vogel", "Betrag in Euro", "Gebucht am", "Kommentar", "Gebucht von"]
    )
    for single_costs in costs:
        writer.writerow(single_costs)
    return response


@login_required(login_url="account_login")
def export_birds(request):
    birds = FallenBird.objects.all().values_list(
        "bird_identifier",
        "bird__name",
        "age",
        "sex",
        "date_found",
        "place_found",
        "place_found_other",
        "created",
        "updated",
        "find_circumstances",
        "diagnosis_finding",
        "user__username",
        "status",
        "status_changed",
    )
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f"attachment, filename=stp_birds_{today}.csv"
    writer = csv.writer(response)
    writer.writerow(
        [
            "Patienten Alias",
            "Vogel",
            "Alter",
            "Geschlecht",
            "gefunden am",
            "Fundort",
            "Fundort (andere)",
            "Pateient angelegt am",
            "Pateient aktualisiert am",
            "Fundumstände",
            "Diagnose",
            "Benutzer",
            "Status",
            "Status geändert am",
        ]
    )
    for bird in birds:
        writer.writerow(bird)
    return response
