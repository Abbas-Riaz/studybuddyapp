from django.shortcuts import render, redirect
from .models import Room, User, Topic
from django.contrib import messages
from .forms import RoomForm
from django.http import HttpResponse

"""for authentication"""
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required

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


@login_required(login_url="/login")
def create_room(request):
    if request.method == "POST":
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    form = RoomForm()
    return render(request, "base/room_form.html", {"form": form})


@login_required(login_url="/login")
def update_room(request, pk):

    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("you are not allowed here")

    context = {"form": form}

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)

        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "base/room_form.html", context)


@login_required(login_url="/login")
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("you are not allowed here")
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete_room.html")


def login_page(request):
    page = "login"
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            messages.add_message(request, messages.ERROR, "User does not exist")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.add_message(
                request, messages.ERROR, "User name or pass is wrong exist"
            )

    context = {"page": page}
    return render(request, "base/login_register.html", context)


def logout_user(request):

    logout(request)
    return redirect("home")


def register_user(request):
    page = "register"
    return render(request, "base/login_register.html")


# def login_page(request):

#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         try:
#             user = User.objects.get(username=username)
#         except:
#             messages.add_messagee
#             messages.add_message(request, messages.ERROR, "User does not exist")


#     context = {}
#     return render(request, "base/login_register.html", context)
