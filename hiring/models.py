from django.db import models

class Industry(models.Model):
    industry_name = models.CharField(max_length=255)

    def __str__(self):
        return self.industry_name

class Employee(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Terminated', 'Terminated'),
        ('Rehired', 'Rehired'),
    ]
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    hire_date = models.DateField(null=True, blank=True)
    rehire_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

class Job(models.Model):
    job_title = models.CharField(max_length=255)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_date = models.DateField()
    closed_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.job_title

class Application(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Hired', 'Hired'),
        ('Rejected', 'Rejected'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    application_date = models.DateField()
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.employee} - {self.job}"

class HiringStatistics(models.Model):
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    monthly_hiring_count = models.IntegerField()
    revenue_generated = models.DecimalField(max_digits=15, decimal_places=2)
    average_recruitment_time = models.IntegerField()  # In days
    recorded_month = models.IntegerField()
    recorded_year = models.IntegerField()

    def __str__(self):
        return f"{self.industry} - {self.recorded_month}/{self.recorded_year}"
