from django.urls import path, re_path
from mbnjattend import views

#TEMPLATE TAGGING
app_name = 'mbnjattend'

urlpatterns =[
        path('mbnjattend/<int:year>/<int:pk>/submit/', views.attend_submit, name='submit'),
        path('mbnjattend/<int:year>/<int:pk>/', views.check_attend, name='attend_check'),
        path('mbnjattend/<int:year>/', views.select_year, name='year'),
        #path(r'mbnjattend/submit/', views.submit, name='submit'),
        path('mbnjattend/', views.load_attend, name='attend_splash'),

]
