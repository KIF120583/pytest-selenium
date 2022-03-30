from libs.logging_handler import getlogger
from libs.ini import *
from libs.trd import *
from libs.system import *
from libs.elements import *
from libs.web_api import *

mylogger = getlogger(logname=log_path , loggername="test_1.py")

def test_0001():

    Web_Open()
    Web_Click(language_confirm_btn)

    # Open Help and close
    Web_Click(Help_open)
    Web_Select_Frame(Help_small_iframe)
    Web_Click(Help_small)
    Web_Default_Frame()
    
    # First Page
    Web_Click(Account_type_menu_open)
    Web_Click(Account_type_menu_personal)
    Web_Click(Country_menu_open)
    Web_Click(Country_menu_taiwan)
    Web_Click(Title_open)
    Web_Click(Title_Dr)
    Web_Input(First_Name_Input_Text_Field , "瑤鋒")
    Web_Input(Middle_Name_Input_Text_Field , "")
    Web_Input(Last_Name_Input_Text_Field , "高")
    Web_Input(Email_Input_Text_Field , random_string() + "@gmail.com")
    Web_Click(Phone_menu_open)
    Web_Click(Phone_menu_taiwan)
    Web_Input(Phone_Input_Text_Field , "983349909")
    Web_Click(Get_verify_code)
    Web_Click(Close)
    Web_Input(Verify_code_Input_Text_Field , "1111")
    state = Web_Click(Next_First_Page)
    if state:
        mylogger.debug("Config first page successfully !!!")
    else:
        mylogger.error("Can't click  Next_First_Page!!!")
        write_trd(trd_file_path = trd_path , script_case_id = "test_0001" , test_case_id = "Register_00001" , test_result = "F")
        assert False        
    
    # Second Page
    Web_Click(Gender_open)
    Web_Click(Gender_male)
    Web_Click(Birthday_day_open)
    Web_Click(Birthday_day_5)
    Web_Click(Birthday_month_open)
    Web_Click(Birthday_month_5)
    Web_Click(Birthday_year_open)
    Web_Click(Birthday_year_1998)
    Web_Input(ID_Input_Text_Field , "F123456789")
    Web_Input(Loc_Input_Text_Field , "3.taipei")
    Web_Input(City_Input_Text_Field , "new taipei city")
    Web_Input(Province_Input_Text_Field , "taiwan")
    Web_Input(Num_Input_Text_Field , "251")
    state = Web_Click(Next_Second_Page)
    if state:
        mylogger.debug("Config second page successfully !!!")
    else:
        mylogger.error("Can't click  Next_Second_Page!!!")
        write_trd(trd_file_path = trd_path , script_case_id = "test_0001" , test_case_id = "Register_00001" , test_result = "F")
        assert False     
        
    # Third Page
    Web_Click(Employment_open)
    Web_Click(Employment_Employed)
    Web_Click(Occupation_open)
    Web_Click(Occupation_Managers)
    Web_Click(Industry_open)
    Web_Click(Industry_Mining)
    Web_Click(Annual_Income_open)
    Web_Click(Annual_Income_29999)
    Web_Click(Total_amount_of_investment_open)
    Web_Click(Total_amount_of_investment_25000)
    Web_Click(Trading_Platform_open)
    Web_Click(Trading_Platform_MetaTrader4)
    Web_Click(Funding_Currency_open)
    Web_Click(Funding_Currency_USD)
    Web_Click(Account_Types_open)
    Web_Click(Account_Types_STANDARD)
    Web_Click(Leverage_open)
    Web_Click(Leverage_150)
    state = Web_Click(Next_Third_Page)
    if state:
        mylogger.debug("Config third page successfully !!!")
    else:
        mylogger.error("Can't click  Next_Third_Page!!!")
        write_trd(trd_file_path = trd_path , script_case_id = "test_0001" , test_case_id = "Register_00001" , test_result = "F")
        assert False 
        
    # Four Page
    Web_Click(P4_Q1)
    Web_Click(P4_Q2)
    Web_Click(P4_Q3)
    Web_Click(P4_Q4)
    Web_Click(P4_Q5)
    Web_Click(Next_Four_Page1)

    Web_Click(P4_Q6)
    Web_Click(P4_Q7)
    Web_Click(P4_Q8)
    Web_Click(P4_Q9)
    Web_Click(P4_Q10)
    Web_Click(Next_Four_Page2)

    mylogger.debug("Config four page successfully !!!")

    # Fifth Page
    Web_Click(P5_Terms_Check_0)
    Web_Click(P5_Terms_Check_1)
    Web_Click(P5_Terms_Check_2)
    Web_Click(Next_Five_Page2)

    mylogger.debug("Config five page successfully !!!")

    # Six Page
    Web_Input(P6_upload_1 , test_data_path+"sample.jpg")
    Web_Input(P6_upload_2 , test_data_path+"sample.jpg")
    Web_Input(P6_upload_3 , test_data_path+"sample.jpg")
    Web_Input(P6_upload_4 , test_data_path+"sample.jpg")
    Web_Click(Next_Six_Page)
    mylogger.debug("Config six page successfully !!!")

    # 谢谢
    message = Web_Get_Text(Finish_message)
    mylogger.debug("-"*50)
    mylogger.debug("message : {}".format(message))
    mylogger.debug("-"*50)

    #Web_Close()

    if message == "谢谢":
        write_trd(trd_file_path = trd_path , script_case_id = "test_0001" , test_case_id = "Register_00001" , test_result = "P")
        assert True
    else:
        write_trd(trd_file_path = trd_path , script_case_id = "test_0001" , test_case_id = "Register_00001" , test_result = "F")
        assert False

def test_0002():
    write_trd(trd_file_path = trd_path , script_case_id = "test_0002" , test_case_id = "Register_00002" , test_result = "P")
    assert "a" == "a"

def test_0003():
    write_trd(trd_file_path = trd_path , script_case_id = "test_0003" , test_case_id = "Register_00003" , test_result = "F")
    assert "a" == "b"