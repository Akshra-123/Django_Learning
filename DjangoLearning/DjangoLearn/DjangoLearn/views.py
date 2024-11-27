from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    #return HttpResponse("Welcome to DjangoLearn home page")
    return render(request , 'index.html')
def about(request):
    return HttpResponse("Welcome to DjangoLearn about page")

def contact(request):
    return HttpResponse("Welcome to DjangoLearn contact page")
