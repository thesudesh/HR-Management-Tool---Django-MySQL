from django.urls import path
from hiring import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('jobs/', views.job_list, name='job_list'),
    path('applications/', views.application_list, name='application_list'),
]
