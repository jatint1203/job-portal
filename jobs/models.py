import os
from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(auto_created=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_created=True, null=True, blank=True)
    delete_flag = models.BooleanField(default=False)
    additional_field = models.JSONField(null=True, blank=True)

    class Meta:
        abstract = True 

class User(BaseModel, AbstractUser,PermissionsMixin):
    is_recruiter = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username

class Job(BaseModel):
    FULL_TIME = 'Full-time'
    PART_TIME = 'Part-time'
    CONTRACT = 'Contract'
    JOB_TYPES = [(FULL_TIME, 'Full-time'), (PART_TIME, 'Part-time'), (CONTRACT, 'Contract')]

    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, default=FULL_TIME)
    salary_range = models.CharField(max_length=50, blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    posted_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.company}"

class Application(BaseModel):
    PENDING = 'Pending'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    STATUS_CHOICES = [(PENDING, 'Pending'), (ACCEPTED, 'Accepted'), (REJECTED, 'Rejected')]
    
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    reviewed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.applicant.username} applied for {self.job.title}"
