from django import forms
from django.contrib.auth.models import User
from mbnjattend.models import (Course, Faculty, Grade, Information,
                                Performance, Roster, Student, Transaction)

class NewStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ()

class NewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ( 'first_name', 'last_name','username', 'email', 'password',)
