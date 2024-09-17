from django.contrib import admin

from  .models import Student
from  .models import Group
from  .models import Question
from  .models import Exam
from  .models import Student_exam
from  .models import Option
from  .models import Subject
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(Student_exam)
admin.site.register(Option)
admin.site.register(Subject)
