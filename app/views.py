from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def f1(request):
    return render(request,'home.html')


def f2(request):
    return render(request,'h2.html')

def f3(request):
    return HttpResponse('hii, helloo how are you ')

def f4(request):
    return HttpResponse('<h2>this is django python based web frame work<br> for creating dynamic web application</h2>')
