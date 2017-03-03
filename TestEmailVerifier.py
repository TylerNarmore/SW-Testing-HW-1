#Author: Tyler Narmore

import pytest
from emailVerifier import emailVerifier


class TestClassEmailVerifier:
    def test_Valid(self):
        assert (emailVerifier('tyler@narmore.net')) == True
        
    def test_No_At(self):
        assert (emailVerifier('tylernarmore.net')) == False

    def test_Top_Level_Domain(self):
        assert (emailVerifier('tyler@narmore')) == False
    
    def test_Domain_Name(self):
        assert (emailVerifier('tyler@.net')) == False

    def test_User_Name(self):
        assert (emailVerifier('@narmore.net')) == False
   
    def test_Parenthesis(self):
        assert (emailVerifier('tyler()@narmore.net')) == False

    def test_Brackets(self):
        assert (emailVerifier('tyler[]@narmore.net')) == False

    def test_Curly_Brackets(self):
        assert (emailVerifier('tyler{}@narmore.net')) == False

    def test_Slashes(self):
        assert (emailVerifier('tyler/\\@narmore.net')) == False

    def test_Capitals(self):
        assert (emailVerifier('TylEr@nArmORe.nEt')) == True
    
    def test_Special_Characters(self):
        assert (emailVerifier('t$l3r@narmore.net')) == True
        
    def test_Two_At(self):
        assert (emailVerifier('ty@er@narmore.net')) == True

    def test_Period_In_Domain(self):
        assert (emailVerifier('tyler@na.rmore.net')) == True
