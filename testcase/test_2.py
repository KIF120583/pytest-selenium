from libs.logging_handler import getlogger
from libs.ini import *
from libs.trd import *
mylogger = getlogger(logname=log_path , loggername="test_2.py")

def test_0004():
    mylogger.debug('test_eggs debug')
    write_trd(trd_file_path = trd_path , script_case_id = "test_0004" , test_case_id = "Register_00004" , test_result = "P")
    assert True
    
def test_0005():
    mylogger.debug('test_0002 debug')
    write_trd(trd_file_path = trd_path , script_case_id = "test_0005" , test_case_id = "Register_00005" , test_result = "P")
    assert "a" == "a"
    
def test_0006():
    mylogger.debug('test_0003 debug')
    write_trd(trd_file_path = trd_path , script_case_id = "test_0006" , test_case_id = "Register_00006" , test_result = "F")
    assert "a" == "b"    