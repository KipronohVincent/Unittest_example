#!/usr/bin/python3
class Employee:
    """Defining Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        """getter to return email"""
        return '{} {}@gmail.com'.format(self.first, self.last)


    @property
    def fullname(self):
        """getter to return fullname"""
        return '{} {}'.format(self.first, self.last)

    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)