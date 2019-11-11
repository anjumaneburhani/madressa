from django.shortcuts import render
from mbnjattend.models import (Course, Faculty, Grade, Information,
                                Performance, Roster, Student, Transaction)
from .forms import NewStudentForm
# Create your views here.
from django.views.generic import (ListView, CreateView, DetailView,
                                  UpdateView, TemplateView)
from mbnjattend import forms, models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

#use sourcetree for code management

def load_attend(request):
    return render(request, 'mbnjattend/attend_splash.html',)


def check_attend(request, year, pk):
    roster = Roster.objects.filter(course=pk)
    stu_list = []
    for r in roster:
        student = Student.objects.get(id=r.student.id)
        stu_list.append(student)

    return render(request, 'mbnjattend/attend_check.html', {'student':stu_list, 'year':year, 'id':pk})
    #return render(request, 'mbnjattend/attend_check.html', {'form': form, 'stu_list':stu_list})

def submit(request, year, pk):
    if request.method == 'POST':
        absent = request.POST.getlist('absent[]')
        informed = request.POST.getlist('informed[]')
        tardy = request.POST.getlist('tardy[]')

        print(request.user, absent, informed, tardy)
        for stu in absent:
            inf="Informed" if stu in informed else None
            stu_id = Student.objects.get(id=int(stu))
            #admin_id  = Faculty.objects.get(username=request.user)
            '''
            t = Transaction.objects.get_or_create(type='absent',
                                                  status=inf,
                                                  student=stu_id,
                                                  admin=admin_id)
            '''
    return render(request,'mbnjattend/submit.html')


def select_year(request, year):
    print('The selected year is ' + str(year))
    courses = Course.objects.filter(cal_year=year)

    return render(request, 'mbnjattend/courses.html',{'year':year, 'courses':courses})


class IndexView(TemplateView):
    template_name = 'mbnjattend/index.html'
