from django.shortcuts import render, get_object_or_404
from .models import CompanyProfile, JobPost, JobApplication

# Home page view
def home(request):
    jobs = JobPost.objects.all()  # Fetch all jobs
    return render(request, 'home.html', {'jobs': jobs})

# Company profile view
def company_profile(request, company_id):
    company = get_object_or_404(CompanyProfile, id=company_id)
    return render(request, 'company_profile.html', {'company': company})

# Job details view
def job_detail(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    return render(request, 'job_detail.html', {'job': job})

# Job seeker profile view
def job_seeker_profile(request, seeker_id):
    job_seeker = get_object_or_404(JobApplication, id=seeker_id)
    return render(request, 'job_seeker_profile.html', {'job_seeker': job_seeker})

# Job search results view
def search_jobs(request):
    query = request.GET.get('q')  # Get search query from request
    jobs = JobPost.objects.filter(title__icontains=query) if query else []
    return render(request, 'search_results.html', {'jobs': jobs, 'query': query})

# Job application submission view
def apply_to_job(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    if request.method == 'POST':
        # Logic for applying to a job (e.g., save applicant details)
        # Placeholder logic:
        return render(request, 'application_success.html', {'job': job})
    return render(request, 'apply_to_job.html', {'job': job})



