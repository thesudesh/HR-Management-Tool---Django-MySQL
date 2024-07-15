from django.shortcuts import render
from hiring.models import Employee
from hiring import models

def gender_hiring_stats(request):
    stats = Employee.objects.values('gender').annotate(count= models.Count('gender'))
    return render(request, 'hiring/templates/gender_hiring_stats.html', {'stats': stats})
