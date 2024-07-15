from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    date_of_birth = models.DateField()
    hire_date = models.DateField(null=True, blank=True)
    rehire_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Terminated', 'Terminated'), ('Rehired', 'Rehired')])

    def __str__(self):
        return self.name

class Industry(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=255)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_date = models.DateField()
    closed_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    application_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Applied', 'Applied'), ('Hired', 'Hired'), ('Rejected', 'Rejected')])

    def __str__(self):
        return f"{self.employee.name} - {self.job.title}"
