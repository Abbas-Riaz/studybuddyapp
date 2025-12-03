from . import views

from django.urls import path

urlpatterns = [
    path("", views.create_family, name="createstudent"),
]
