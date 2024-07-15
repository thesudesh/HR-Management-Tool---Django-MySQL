from django.shortcuts import render
from hiring.models import Employee, Job, Application

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'hiring/employee_list.html', {'employees': employees})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'hiring/job_list.html', {'jobs': jobs})

def application_list(request):
    applications = Application.objects.all()
    return render(request, 'hiring/application_list.html', {'applications': applications})
