# Generated by Django 4.2.16 on 2024-11-27 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CandidateProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("resume", models.FileField(upload_to="candidate_resumes/")),
                ("skills", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="candidate_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CompanyProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_name", models.CharField(max_length=255)),
                ("company_description", models.TextField()),
                (
                    "company_logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="company_logos/"
                    ),
                ),
                ("location", models.CharField(max_length=255)),
                ("website", models.URLField(blank=True, max_length=255, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="company_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("requirements", models.TextField()),
                (
                    "salary",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("location", models.CharField(max_length=255)),
                (
                    "job_type",
                    models.CharField(
                        choices=[
                            ("Full-time", "Full-time"),
                            ("Part-time", "Part-time"),
                            ("Contract", "Contract"),
                            ("Internship", "Internship"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Engineering", "Engineering"),
                            ("Marketing", "Marketing"),
                            ("Design", "Design"),
                            ("Sales", "Sales"),
                            ("Finance", "Finance"),
                            ("Human Resources", "Human Resources"),
                        ],
                        max_length=50,
                    ),
                ),
                ("posted_date", models.DateTimeField(auto_now_add=True)),
                ("closing_date", models.DateTimeField()),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_posts",
                        to="DjangoApp.companyprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("applied_on", models.DateTimeField(auto_now_add=True)),
                ("cover_letter", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Accepted", "Accepted"),
                            ("Rejected", "Rejected"),
                        ],
                        default="Pending",
                        max_length=50,
                    ),
                ),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="DjangoApp.candidateprofile",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="DjangoApp.jobpost",
                    ),
                ),
            ],
        ),
    ]