from django.db import models

# Create your models here.
# class Dojo(models.Model):
#     name = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     state = models.CharField(max_length=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Ninja(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     dojos = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"name: {self.name} teaching: {self.subject}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.DecimalField(max_digits=10, decimal_places=3)
    classes = models.ManyToManyField(Teacher, related_name="teachers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)