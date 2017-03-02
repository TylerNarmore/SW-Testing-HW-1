#Wrote by Tyler Narmore
from menu import *
import pytest
import mock


class TestMain:
    def test_Menu_Empty_Input(self,capfd):
        with pytest.raises(SystemExit):
            with mock.patch('builtins.input', side_effect =
                            ['','5']):
                main()
        out,err = capfd.readouterr()
        assert "Error, select option 1-5" in out


    def test_Menu_Invalid_Input(self,capfd):
        with pytest.raises(SystemExit):
           
            with mock.patch('builtins.input', side_effect =
                            ['a','5']):
                main()
        out,err = capfd.readouterr()
        assert "Error, select option 1-5" in out

    def test_Valid_Option_1(self):
        with pytest.raises(SystemExit):
            with mock.patch('builtins.input', side_effect =
                            ['1','6','0','170','5']):
                main()
                
    def test_Invalid_Option_1(self):
        with pytest.raises(SystemExit):
            with mock.patch('builtins.input', side_effect =
                            ['1','a','6','0','170','5']):
                main()

                
    def test_Option_2(self):
        with pytest.raises(SystemExit):
            with mock.patch('builtins.input', side_effect =
                            ['2','20','100000','10','50000','5']):
                main()
                
    def test_Option_2_Not_Able(self):
        with pytest.raises(SystemExit):
            with mock.patch('builtins.input', side_effect =
                            ['2','20','100000','.10','5000','5']):
                main()
    
                
    def test_Option_3_Pass(self):
        with pytest.raises(SystemExit):
            with mock.patch('builtins.input', side_effect =
                            ['3','1','1','1','1','5']):
                main()
    
    def test_Option_3_Fail(self):
        with pytest.raises(SystemExit):
            with mock.patch('builtins.input', side_effect =
                            ['3','a','3','1','1','1','1','5']):
                main()
    
    def test_Option_4_Valid(self):
        with pytest.raises(SystemExit):
            with mock.patch('builtins.input', side_effect =
                            ['4','tyler@narmore.net','5']):
                main()

    def test_Option_4_Invalid(self):
        with pytest.raises(SystemExit):
            with mock.patch('builtins.input', side_effect =
                            ['4','@narmore.net','5']):
                main()
