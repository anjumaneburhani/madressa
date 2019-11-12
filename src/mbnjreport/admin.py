from django.contrib import admin
from mbnjreport.models import (Course, Faculty, Grade, Information,
                                Performance, Roster, Student, Transaction)

# Register your models here.
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Grade)
admin.site.register(Information)
admin.site.register(Performance)
admin.site.register(Roster)
admin.site.register(Student)
admin.site.register(Transaction)
