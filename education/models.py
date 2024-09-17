from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Group(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Subject(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey(Group,on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
class Exam(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject,models.SET_NULL,null=True)
    def __str__(self):
        return self.name
class Student_exam(models.Model):
    exam = models.IntegerField()
    student = models.ForeignKey(Student,on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.exam
class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Option (models.Model):
    name = models.CharField(max_length=200)
    is_correct = models.DateField()
    question = models.ForeignKey(Question, on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name