from django.test import TestCase
from hiring.models import Employee  

class EmployeeModelTest(TestCase):
    def setUp(self):
        Employee.objects.create(name="John Doe", gender="Male", date_of_birth="1980-01-01", status="Active")

    def test_employee_creation(self):
        john = Employee.objects.get(name="John Doe")
        self.assertEqual(john.gender, "Male")
