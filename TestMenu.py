from menu import *
import warnings
import pytest
import mock


class TestMain:
    def test_Menu_Empty_Input(self):
        with pytest.raises(SystemExit):
            with pytest.warns(UserWarning) as record:
                with mock.patch('builtins.input', side_effect =
                                ['','5']):
                    main()
        assert len(record) == 1

    def test_Menu_Invalid_Input(self):
        with pytest.raises(SystemExit):
            with pytest.warns(UserWarning) as record:
                with mock.patch('builtins.input', side_effect =
                                ['a','5']):
                    main()
        assert len(record) == 1

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
                            ['2','20','100000','.10','50000','5']):
                test = main() == 0
                
