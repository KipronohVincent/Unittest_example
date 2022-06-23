import unittest
from Employees import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('Dan', 'Job', 50000)
        self.emp_2 = Employee('Mark', 'Dan', 60000)

    def test_email(self):
        emp_1 = Employee('Dan', 'Job', 50000)
        emp_2 = Employee('Mark', 'Dan', 60000)

        self.assertEqual(emp_1.email, 'Dan Job@gmail.com')
        self.assertEqual(emp_2.email, 'Mark Dan@gmail.com')

        emp_1.first = 'Mary'
        emp_2.first = 'Ann'

        self.assertEqual(emp_1.email, 'Mary Job@gmail.com')
        self.assertEqual(emp_2.email, 'Ann Dan@gmail.com')

    def test_fullname(self):
        emp_1 = Employee('Dan', 'Job', 50000)
        emp_2 = Employee('Mark', 'Dan', 60000)

        self.assertEqual(self.emp_1.fullname, 'Dan Job')
        self.assertEqual(self.emp_2.fullname, 'Mark Dan')

        emp_1.first = 'Mary'
        emp_2.first = 'Ann'

        self.assertEqual(emp_1.fullname, 'Mary Job')
        self.assertEqual(emp_2.fullname, 'Ann Dan')

    def test_apply_raise(self):
        emp_1 = Employee('Dan', 'Job', 50000)
        emp_2 = Employee('Mark', 'Dan', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()