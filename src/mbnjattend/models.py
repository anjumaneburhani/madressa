from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
gender_choices = (('male','Male'),('female', 'Female'))
mbrid_choices = (('its', 'ITS'), ('other', 'Other'))

class Course(models.Model):
    name = models.CharField(max_length = 90, verbose_name='Course Name')
    catnum = models.CharField(max_length = 90, verbose_name='Catalog Number')
    desc = models.CharField(max_length = 255, verbose_name='Course Description', null=True, blank=True)
    cal_year = models.FloatField()
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Faculty(models.Model):
    fname = models.CharField(max_length = 90, verbose_name='First Name')
    lname = models.CharField(max_length = 90, verbose_name='Last Name')
    facid = models.CharField(max_length = 90, verbose_name='Faculty ID', unique=True)
    facidtype = models.CharField(max_length = 90, choices = mbrid_choices, verbose_name='ID Type')
    role = models.CharField(max_length = 90, verbose_name='Faculty Role')
    contact1 = models.CharField(max_length = 90, verbose_name='Contact 1')
    c1phone = models.CharField(max_length = 12, verbose_name='Phone 1')
    c1desc = models.CharField(max_length = 90, verbose_name='Desc 1')
    contact2 = models.CharField(max_length = 12, verbose_name='Contact 2', null=True, blank=True)
    c2phone = models.CharField(max_length = 12, verbose_name='Phone 2', null=True, blank=True)
    c2desc = models.CharField(max_length = 90, verbose_name='Desc 2', null=True, blank=True)
    address = models.CharField(max_length = 255, verbose_name='Address')
    city = models.CharField(max_length = 90, verbose_name='City')
    state = models.CharField(max_length = 90, verbose_name='State')
    zipcode =  models.CharField(max_length = 90, verbose_name='Type')
    gender = models.CharField(max_length = 90, choices=gender_choices, verbose_name='Gender')

    def __str__(self):
        return str(self.lname) + ', ' + str(self.fname)


class Grade(models.Model):
    name = models.CharField(max_length = 90, verbose_name='Grade')
    desc = models.CharField(max_length = 255, verbose_name='Description', null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Information(models.Model):
    infotype = models.CharField(max_length = 90, verbose_name='Type')
    desc = models.CharField(max_length = 90, verbose_name='Description', null=True, blank=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.infotype)


class Performance(models.Model):
    eval = models.CharField(max_length = 90, verbose_name='Evaluation')
    desc = models.CharField(max_length = 255, verbose_name='Description')
    score = models.FloatField(blank=True)
    totalscore = models.FloatField(blank=True)
    lettergrade = models.CharField(max_length = 2, verbose_name='Letter Grade', blank=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    admin = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.eval) + ' > ' + str(Studentid)


class Roster(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.course) + ' > ' + str(self.student)


class Student(models.Model):
    fname = models.CharField(max_length = 90, verbose_name='First Name')
    lname = models.CharField(max_length = 90, verbose_name='Last Name')
    stuid = models.CharField(max_length = 90, verbose_name='Student ID', unique=True)
    stuidtype = models.CharField(max_length = 90, choices = mbrid_choices, verbose_name='ID Type')
    type = models.CharField(max_length = 90, verbose_name='Student Type', null=True, blank=True)
    contact1 = models.CharField(max_length = 90, verbose_name='Contact 1')
    c1phone = models.CharField(max_length = 12, verbose_name='Phone 1')
    c1desc = models.CharField(max_length = 90, verbose_name='Desc 1')
    contact2 = models.CharField(max_length = 12, verbose_name='Contact 2', null=True, blank=True)
    c2phone = models.CharField(max_length = 12, verbose_name='Phone 2', null=True, blank=True)
    c2desc = models.CharField(max_length = 90, verbose_name='Desc 2', null=True, blank=True)
    address = models.CharField(max_length = 255, verbose_name='Address')
    city = models.CharField(max_length = 90, verbose_name='City')
    state = models.CharField(max_length = 90, verbose_name='State')
    zipcode =  models.CharField(max_length = 90, verbose_name='Type')
    gender = models.CharField(max_length = 90, choices=gender_choices, verbose_name='Gender')
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE, verbose_name='Grade')

    def __str__(self):
        return str(self.lname) + ', ' + str(self.fname)


class Transaction(models.Model):
    type = models.CharField(max_length = 90, verbose_name='Type')
    transdate = models.DateTimeField(verbose_name='Transaction Date',
                                      auto_now_add=True)
    status = models.CharField(max_length = 90, verbose_name='Status', blank=True, null=True)
    desc = models.CharField(max_length = 90, verbose_name='Description', blank=True, null=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    admin = models.ForeignKey('Faculty', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.type) + ' > ' + str(self.Student)
