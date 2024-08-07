# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Applications(models.Model):
    applicationid = models.AutoField(db_column='ApplicationID', primary_key=True)  # Field name made lowercase.
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    jobid = models.ForeignKey('Jobs', models.DO_NOTHING, db_column='JobID', blank=True, null=True)  # Field name made lowercase.
    applicationdate = models.DateField(db_column='ApplicationDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applications'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employees(models.Model):
    employeeid = models.AutoField(db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth')  # Field name made lowercase.
    hiredate = models.DateField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    rehiredate = models.DateField(db_column='RehireDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employees'


class HiringApplication(models.Model):
    id = models.BigAutoField(primary_key=True)
    application_date = models.DateField()
    status = models.CharField(max_length=20)
    employee = models.ForeignKey('HiringEmployee', models.DO_NOTHING)
    job = models.ForeignKey('HiringJob', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hiring_application'


class HiringEmployee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    hire_date = models.DateField(blank=True, null=True)
    rehire_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'hiring_employee'


class HiringIndustry(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'hiring_industry'


class HiringJob(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_date = models.DateField()
    closed_date = models.DateField(blank=True, null=True)
    industry = models.ForeignKey(HiringIndustry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hiring_job'


class Hiringstatistics(models.Model):
    statisticid = models.AutoField(db_column='StatisticID', primary_key=True)  # Field name made lowercase.
    industryid = models.ForeignKey('Industries', models.DO_NOTHING, db_column='IndustryID', blank=True, null=True)  # Field name made lowercase.
    monthlyhiringcount = models.IntegerField(db_column='MonthlyHiringCount', blank=True, null=True)  # Field name made lowercase.
    revenuegenerated = models.DecimalField(db_column='RevenueGenerated', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    averagerecruitmenttime = models.IntegerField(db_column='AverageRecruitmentTime', blank=True, null=True)  # Field name made lowercase.
    recordedmonth = models.IntegerField(db_column='RecordedMonth', blank=True, null=True)  # Field name made lowercase.
    recordedyear = models.IntegerField(db_column='RecordedYear', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hiringstatistics'


class Industries(models.Model):
    industryid = models.AutoField(db_column='IndustryID', primary_key=True)  # Field name made lowercase.
    industryname = models.CharField(db_column='IndustryName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'industries'


class Jobs(models.Model):
    jobid = models.AutoField(db_column='JobID', primary_key=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='JobTitle', max_length=255)  # Field name made lowercase.
    industryid = models.ForeignKey(Industries, models.DO_NOTHING, db_column='IndustryID', blank=True, null=True)  # Field name made lowercase.
    monthlysalary = models.DecimalField(db_column='MonthlySalary', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    posteddate = models.DateField(db_column='PostedDate', blank=True, null=True)  # Field name made lowercase.
    closeddate = models.DateField(db_column='ClosedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jobs'
