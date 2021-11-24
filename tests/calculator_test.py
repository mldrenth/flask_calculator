import unittest
from modules.calculator import *

class TestCalculator(unittest.TestCase):
    def test_can_add_two_integers(self):
        self.assertEqual(5,add(2,3))
    
    def test_can_subtract_two_integers(self):
        self.assertEqual(2,subtract(5,3))
    
    def test_can_multiply_two_integers(self):
        self.assertEqual(10,multiply(2,5))
    
    def test_can_divide_two_integers(self):
        self.assertEqual(7,divide(14,2))