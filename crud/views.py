from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .forms import FamilyForm, StudentForm
from .models import Student


from django.shortcuts import render, redirect
from .models import Family, Student
from .forms import FamilyForm


def create_family(request):

    if request.method == "POST":
        family_form = FamilyForm(request.POST)
        if family_form.is_valid():
            family = family_form.save()

        names = request.POST.getlist("student_name[]")
        classes = request.POST.getlist("student_class[]")
        for name, cls in zip(names, classes):

            data = {"student_name": name, "student_class": cls}

            # Student.objects.create(family=family, student_name=name, student_class=cls)
            student_form = StudentForm(data)

            if student_form.is_valid():
                student = student_form.save(commit=False)
                student.family = family
                student.save()

        return redirect("/home")

    else:

        family_form = FamilyForm()

    return render(request, "crud/index.html", {"family_form": family_form})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Family, Student
from .forms import FamilyForm, StudentForm


def edit_family(request, family_id):
    family = get_object_or_404(Family, id=family_id)
    students = Student.objects.filter(family=family)

    if request.method == "POST":
        family_form = FamilyForm(request.POST, instance=family)
        if family_form.is_valid():
            family_form.save()

            # --- Handle existing students ---
            existing_ids = request.POST.getlist("existing_id[]")
            existing_names = request.POST.getlist("existing_name[]")
            existing_classes = request.POST.getlist("existing_class[]")

            for sid, name, cls in zip(existing_ids, existing_names, existing_classes):
                student = Student.objects.get(id=sid)
                student.student_name = name
                student.student_class = cls
                student.save()

            # --- Handle new students ---
            new_names = request.POST.getlist("student_name[]")
            new_classes = request.POST.getlist("student_class[]")

            for name, cls in zip(new_names, new_classes):
                if name:  # skip empty
                    Student.objects.create(
                        family=family, student_name=name, student_class=cls
                    )

            return redirect("/home")
    else:
        family_form = FamilyForm(instance=family)

    return render(
        request,
        "crud/edit_family.html",
        {"family_form": family_form, "students": students},
    )


def create_family1(request):
    if request.method == "POST":
        family_form = FamilyForm(request.POST)
        if family_form.is_valid():
            family = family_form.save()  # save family first
            print(family)
            print(request.POST)

            # Get all students from POST arrays
            names = request.POST.getlist("student_name[]")
            classes = request.POST.getlist("student_class[]")
            print(names)
            print(classes)

            # Save each student
            for name, cls in zip(names, classes):
                if name:  # skip empty inputs
                    Student.objects.create(
                        family=family, student_name=name, student_class=cls
                    )

            return redirect("/home")  # redirect to a list page
    else:
        family_form = FamilyForm()

    return render(request, "crud/index.html", {"family_form": family_form})


def edit_family(request, family_id):
    family = get_object_or_404(Family, id=family_id)
    students = Student.objects.filter(family=family)

    if request.method == "POST":
        # Update family info
        family_form = FamilyForm(request.POST, instance=family)
        if family_form.is_valid():
            family_form.save()

            # Update existing students
            existing_ids = request.POST.getlist("existing_id[]")
            existing_names = request.POST.getlist("existing_name[]")
            existing_classes = request.POST.getlist("existing_class[]")

            for sid, name, cls in zip(existing_ids, existing_names, existing_classes):
                student = Student.objects.get(id=sid)
                student.student_name = name
                student.student_class = cls
                student.save()

            # Add new students
            new_names = request.POST.getlist("student_name[]")
            new_classes = request.POST.getlist("student_class[]")

            for name, cls in zip(new_names, new_classes):
                if name:  # skip empty rows
                    Student.objects.create(
                        family=family, student_name=name, student_class=cls
                    )

            return redirect("/home")  # or redirect to family detail page

    else:
        family_form = FamilyForm(instance=family)

    return render(
        request,
        "crud/edit_family.html",
        {"family_form": family_form, "students": students},
    )
