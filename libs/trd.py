from libs.logging_handler import getlogger
from libs.ini import *

mylogger = getlogger(logname=log_path , loggername="trd.py")

def write_trd(trd_file_path = trd_path , script_case_id = None , test_case_id = None , test_result = None):
    with open(trd_file_path, "a") as trd_file:
        trd_file.write(script_case_id + "," + test_case_id + "," + test_result + "\n")

