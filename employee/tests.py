

# Create your tests here.

from django.test import TestCase


class EmployeeTest(TestCase):

    def test_addition(self):
        self.assertEqual(10 + 20, 30)

    def test_string(self):
        self.assertEqual("employee".upper(), "EMPLOYEE")
