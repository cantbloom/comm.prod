"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

## Test cases
content = """

a btb 'parse this' comm.prod

or

abtb "parse that" commprod

and

btb "then this" comm prod

BTB "comm" commprod

ABTB  COMMPROD

a btb "a btb in the middle comm prod" comm.prod

a btb "a btb 'in the middle' comm prod" comm.prod

"""
prod = ["parse this", "parse that", "then this", "comm", "",
         "a btb in the middle comm prod",
         "a btb 'in the middle' comm prod"]

#assert(parseProd(content)== prod)