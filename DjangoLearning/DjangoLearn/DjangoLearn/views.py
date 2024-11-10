from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to DjangoLearn home page")

def about(request):
    return HttpResponse("Welcome to DjangoLearn about page")

def contact(request):
    return HttpResponse("Welcome to DjangoLearn contact page")
