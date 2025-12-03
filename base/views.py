from django.shortcuts import render, redirect

from .models import Room, User, Topic

from .forms import RoomForm


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
    user = room.host
    context = {"room": room, "user": user}

    # return HttpResponse("thi is room")
    # render method is work wiht rendering templates
    return render(request, "base/room.html", context)


def create_room(request):
    if request.method == "POST":
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    form = RoomForm()
    return render(request, "base/room_form.html", {"form": form})


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    context = {"form": form}

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)

        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "base/room_form.html", context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete_room.html")
