from django.db import models

# Create your models here.



class Family(models.Model):
    family_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.family_id} - {self.name}"


class Student(models.Model):
    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, related_name="students"
    )
    student_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)

    
    
    def __str__(self):
        return self.student_name 
