# URLs
from django.urls import path

from jobs.job_views.job_portal_view import ApplicationListView, JobListView
from jobs.job_views.login_view import LoginView, RegisterView, WelcomeView




urlpatterns = [
   path('api/welcome/', WelcomeView.as_view(), name='welcome'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),

    path('api/jobs/', JobListView.as_view(), name='job-list-create'),
    path('api/applications/', ApplicationListView.as_view(), name='application-list-create'),
]
