from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('company/<int:company_id>/', views.company_profile, name='company_profile'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('seeker/<int:seeker_id>/', views.job_seeker_profile, name='job_seeker_profile'),
    path('search/', views.search_jobs, name='search_jobs'),
    path('apply/<int:job_id>/', views.apply_to_job, name='apply_to_job'),
]