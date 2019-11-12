from django.shortcuts import render
from mbnjattend.models import (Course, Faculty, Grade, Information,
                                Performance, Roster, Student, Transaction)
#from .forms import NewStudentForm
# Create your views here.
from django.views.generic import (ListView, CreateView, DetailView,
                                  UpdateView, TemplateView)
#from mbnjattend import forms, models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

#use sourcetree for code management

def load_report(request):
    return render(request, 'mbnjreport/splash.html',)



class IndexView(TemplateView):
    template_name = 'mbnjreport/index.html'
