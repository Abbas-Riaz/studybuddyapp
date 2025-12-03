from django.forms import ModelForm
from django.forms import inlineformset_factory
from .models import Family, Student


class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = ["family_id", "name"]


class StudentForm:
    class Meta:
        model = Family

    fields = ["student_name", "student_class"]
