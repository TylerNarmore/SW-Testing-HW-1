#Author: Brannon Jordan
import pytest
import mock
from Retirement import *


class TestRetirement:

    #Tests the retirement with given criteria to see if the program
    #calcualtes it correctly
    def test_if_correct(self):
        assert retirement(20,100000,.10,50000/2)==22

    #Tests if the program catches that the retirement goal is not possible
    def test_if_not_possible(self):
        assert (retirement(50,1000,.5,1000000/2))==0

   #Test that the age input works correctly using mock to simulate a user
    def test_age_input(self):
        with mock.patch('builtins.input', side_effect =
                        ['a','12','13','100000','10','5000']):
            age,salary,savings,goal = retirementInput()
            assert age == 13
            assert (retirement(age,salary,savings,goal))==13
            
    #Test that the salary input works correctly using mock to simulate a user
    def test_salary_input(self):
        with mock.patch('builtins.input', side_effect =
                        ['15','a','-500','10000','20','5000']):
            age,salary, savings, goal = retirementInput()
            assert salary == 10000
            assert (retirement(age,salary,savings,goal))==16

    #Test that the savings input works correctly using mock to simulate a user            
    def test_savings_input(self):
        with mock.patch('builtins.input',side_effect =
                        ['20','100000','k','-5','1000','20','20000']):
            age,salary,savings,goal = retirementInput()
            assert savings == .2
            assert (retirement(age,salary,savings,goal)) == 20

   #Test that the goal input works correctly using mock to simulate a user            
    def test_goal_input(self):
        with mock.patch('builtins.input', side_effect =
                        ['25','500000','5','no goal','-500','1000000']):
            age, salary, savings, goal = retirementInput()
            assert goal == 500000
            assert (retirement(age,salary,savings,goal)) == 45
