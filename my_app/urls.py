
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('a',views.myhome,name='myhome'),
    path('welcome',views.welcome,name='welcome'),
    path('medcare',views.medcare,name='medcare'),
    path('patientreg',views.patientregistration,name='patientregistration')
]