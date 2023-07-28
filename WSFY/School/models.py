from django.db import models

# Create your models here.
class Subject(models.Model):
    sub_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_name

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.roll_number}"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}: {self.marks_obtained}"