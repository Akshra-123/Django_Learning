from django.db import models
from django.contrib.auth.models import User

# Job Types
JOB_TYPE_CHOICES = (
    ('Full-time', 'Full-time'),
    ('Part-time', 'Part-time'),
    ('Contract', 'Contract'),
    ('Internship', 'Internship'),
)

# Job Categories
CATEGORY_CHOICES = (
    ('Engineering', 'Engineering'),
    ('Marketing', 'Marketing'),
    ('Design', 'Design'),
    ('Sales', 'Sales'),
    ('Finance', 'Finance'),
    ('Human Resources', 'Human Resources'),
)

# Company Profile Model
class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    location = models.CharField(max_length=255)
    website = models.URLField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.company_name

# Job Post Model
class JobPost(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='job_posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    posted_date = models.DateTimeField(auto_now_add=True)
    closing_date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    def is_active(self):
        return self.closing_date > timezone.now()

# Candidate Profile Model
class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    resume = models.FileField(upload_to='candidate_resumes/')
    skills = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Job Application Model
class JobApplication(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='applications')
    applied_on = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending')
    
    def __str__(self):
        return f"{self.candidate} applied for {self.job.title} on {self.applied_on}"
    
    def is_pending(self):
        return self.status == 'Pending'

