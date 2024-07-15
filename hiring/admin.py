from django.contrib import admin
from hiring.models import Industry, Employee, Job, Application, HiringStatistics

admin.site.register(Industry)
admin.site.register(Employee)
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(HiringStatistics)
