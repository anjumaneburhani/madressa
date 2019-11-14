from django.shortcuts import render
from mbnjattend.models import (Course, Faculty, Grade, Information,
                                Performance, Roster, Student, Transaction)
from .forms import NewStudentForm, NewUserForm
# Create your views here.
from django.views.generic import (ListView, CreateView, DetailView,
                                  UpdateView, TemplateView)
from mbnjattend import forms, models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect

#use sourcetree for code management
@login_required
def load_attend(request):
    return render(request, 'mbnjattend/attend_splash.html',)

@login_required
def check_attend(request, year, pk):
    roster = Roster.objects.filter(course=pk)
    stu_list = []
    for r in roster:
        student = Student.objects.get(id=r.student.id)
        stu_list.append(student)

    return render(request, 'mbnjattend/attend_check.html', {'student':stu_list, 'year':year, 'id':pk})
    #return render(request, 'mbnjattend/attend_check.html', {'form': form, 'stu_list':stu_list})


def user_register(request):
    print('I got to register page')
    registered = False
    if request.method == 'POST':
        user_form = NewUserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = NewUserForm()
    return render(request, 'register.html', { 'user_form':user_form,
                                                'registered':registered} )


def user_login(request):
    print('I got into user login')
    if request.method == 'POST':
        username=request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse('Account is not active')
        else:
            print('Someone tried to login and failed')
            print('Username: {} and password {}'.format(username, password))
            return HttpResponse('Invalid login details supplied!')
    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def attend_submit(request, year, pk):
    if request.method == 'POST':
        absent = request.POST.getlist('absent[]')
        informed = request.POST.getlist('informed[]')
        tardy = request.POST.getlist('tardy[]')

        print(request.user, absent, informed, tardy)
        for stu in absent:
            inf="Informed" if stu in informed else None
            stu_id = Student.objects.get(id=int(stu))
            admin_id = Faculty.objects.get(user=request.user)
            t = Transaction.objects.get_or_create(type='absent',
                                                  status=inf,
                                                  student=stu_id,
                                                  admin=admin_id)

    return render(request,'mbnjattend/submit.html')

@login_required
def select_year(request, year):
    print('The selected year is ' + str(year))
    courses = Course.objects.filter(cal_year=year)

    return render(request, 'mbnjattend/courses.html',{'year':year, 'courses':courses})


class IndexView(TemplateView):
    template_name = 'index.html'
