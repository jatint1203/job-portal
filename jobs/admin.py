from django.contrib import admin
from .models import Job, Application, User

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location',)
    search_fields = ('title', 'company', 'location')
    list_per_page = 25

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'status')
    search_fields = ('user__username', 'job__title', 'status')
    list_per_page = 25

admin.site.register(User)
admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
