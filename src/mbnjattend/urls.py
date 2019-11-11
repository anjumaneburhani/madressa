from django.urls import path, re_path
from mbnjattend import views

#TEMPLATE TAGGING
app_name = 'mbnjattend'

urlpatterns =[
        path('', views.IndexView.as_view(), name='index'),
        path(r'mbnjattend/<int:year>/<int:pk>/submit/', views.submit, name='submit'),
        path(r'mbnjattend/<int:year>/<int:pk>/', views.check_attend, name='attend_check'),
        path(r'mbnjattend/<int:year>/', views.select_year, name='year'),
        #path(r'mbnjattend/submit/', views.submit, name='submit'),
        path(r'mbnjattend/', views.load_attend, name='attend_splash'),
]
