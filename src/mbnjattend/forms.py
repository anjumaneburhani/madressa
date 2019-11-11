from django import forms
from mbnjattend.models import (Course, Faculty, Grade, Information,
                                Performance, Roster, Student, Transaction)

class NewStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ()
