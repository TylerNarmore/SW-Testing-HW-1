#Author: Brandon Stone
import pytest

from bmiCalculator import *

class TestBMI:

    #Tests if the BMI Calculator works
    def test_correct(self):
        assert bodyMassIndex(5, 9, 167)==25.26

    #Tests that it will not allow incorrect inputs
    def test_incorrect(self):
        assert bodyMassIndex(0,222,9)==0

    #Last 2 Tests are for checking other vaules
    def test_overweight(self):
        assert bodyMassIndex(6,7,500)>=30

    def test_underweight(self):
        assert bodyMassIndex(5,7,100)<18
    
