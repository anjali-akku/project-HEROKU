from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("hello")
def myhome(request):
    return HttpResponse("welcome")
def welcome(request):
    return render (request,'welcome.html')
def medcare(request):
    return render(request,'medcare.html')
def patientregistration(request):
    return render(request,'patient registration.html')