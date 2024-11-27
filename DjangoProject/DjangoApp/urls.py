from django.urls import path
from . import views

urlpatterns = [
    path('DjangoApp/',views.home,name='home'),
]
