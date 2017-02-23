import pytest
import sys

from distanceForm import *

class TestClassDistance:

    def testZero(self):
        assert (distance(5, 5, 5, 5)) == '0.00'

    def testWholeNumbers(self):
    	assert (distance(1, 2, 3, 4)) == '2.83'

    def testDecimals(self):
    	assert (distance(1.2, 2.3, 3.4, 4.5)) == '3.11'