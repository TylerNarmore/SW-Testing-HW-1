#Author: Brandon Stone
import pytest
import mock

from bmiCalculator import *

class TestBMI:

    #Tests Inches
    def test_inches(self):
        with mock.patch('builtins.input', side_effect =
                        ['7','a','19','5','90']):
            bmi,cate = bodyMassIndex()
            assert bmi == 8.18
            assert cate == "Underweight"

    #Tests Feet and Inches
    def test_feet_inches(self):
        with mock.patch('builtins.input', side_effect =
                        ['a','300','7','a','19','5','90']):
            bmi,cate = bodyMassIndex()
            assert bmi == 8.18
            assert cate == "Underweight"

    #Tests Wieght
    def test_weight(self):
        with mock.patch('builtins.input', side_effect =
                        ['5','9','800','aksk','167']):
            bmi,cate = bodyMassIndex()
            assert bmi == 25.26
            assert cate == "Overweight"

    #Tests everything else
    def test_feet(self):
        with mock.patch('builtins.input', side_effect =
                        ['-1','3','4','7100','-122','89/','120']):
            bmi,cate = bodyMassIndex()
            assert cate == "Obese"
