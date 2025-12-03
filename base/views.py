from django.shortcuts import render

from .models import Room, User, Topic

from django.http import HttpResponse


# rooms = [
#     {"id": 1, "name": "lets learn python"},
#     {"id": 2, "name": "lets learn django"},
#     {"id": 2, "name": "lets learn djano"},
# ]


def home(request):

    rooms = Room.objects.all()
    context = {"rooms": rooms}

    # return HttpResponse("home")
    return render(request, "base/home.html", context)


def room(request, pk):
    room = None
    # id  = int(pk)
    room = Room.objects.get(id=pk)
    user = User.objects.get(id=pk)
    context = {"room": room, "user": user}

    # return HttpResponse("thi is room")
    # render method is work wiht rendering templates
    return render(request, "base/room.html", context)


# Create your views here.
