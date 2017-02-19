import pytest
from Retirement import *


class TestRetirement:

    #Tests the retirement with given criteria to see if the program
    #calcualtes it correctly
    def test_if_correct(self):
        assert retirement(20,100000,.10,50000/2)==22

    #Tests if the program catches that the retirement goal is not possible
    def test_if_not_possible(self):
        assert (retirement(50,1000,.5,1000000/2))==0

    #A final test to check if the program calculates retirement correctly
    def test_longer_saving_time(self):
        assert (retirement(13,50000,.20,500000/2))==38

