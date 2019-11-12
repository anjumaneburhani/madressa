from django.urls import path, re_path
from mbnjreport import views

#TEMPLATE TAGGING
app_name = 'mbnjattend'

urlpatterns =[
        
        path(r'mbnjreport/', views.load_report, name='splash'),
]
