from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'description', 'job_type', 'salary_range', 'requirements', 'deadline']
