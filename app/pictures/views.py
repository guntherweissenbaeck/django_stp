from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Picture
from bird.models import FallenBird


@login_required(login_url="account_login")
def pictures_all(request):
    pictures = Picture.objects.all()
    context = {"pictures": pictures}
    return render(request, "pictures/pictures_all.html", context)


@login_required(login_url="account_login")
def pictures_single(request, id):
    pictures = Picture.objects.all().filter(fallenbird=id)
    bird = FallenBird.objects.get(id=id)
    if not pictures:
        pictures = []
    context = {"pictures": pictures, "bird": bird}
    return render(request, "pictures/pictures_single.html", context)


@login_required(login_url="account_login")
def pictures_delete(request, id):
    pictures = Picture.objects.all().filter(id=id)
    if request.method == "POST":
        pictures.delete()
    if not pictures:
        pictures = []
    context = {"pictures": pictures}
    return render(request, "pictures/pictures_delete.html", context)

#  @login_required(login_url="account_login")
#  def pictures_edit(request, id):
    #  picture = Picture.objects.all().get(id=id)
    #  context = {"picture": picture}
    #  return render(request, "pictures/pictures_edit.html", context)
