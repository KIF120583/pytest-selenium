Outlines
 - Preparation
 - Configure
 - Execution
 - Check results
 - Restrictions

-----------------------------------------------------------------------

- Preparation :

  1. Run Install_python_packages.bat to install the required python packages

-----------------------------------------------------------------------

- Configure :

  1. config/config.ini

  2. config/elements.ini
     Correct format : Help_open = //*[@id="launcher"]
     Wrong   format : Help_open = //*[@id='launcher']
                      Help_open=//*[@id="launcher"]

-----------------------------------------------------------------------

- Execution :
  
  1. Run all test cases : python main.py 

  2. Run single test case : python main.py -c test_1.py

-----------------------------------------------------------------------

- Check results :

  1. Check the log and report files in logs folder
     logs/[date]/img/        : sceenshot pics folder
     logs/[date]/logger.log  : log from logging     
     logs/[date]/pytest.html : pytest report
     logs/[date]/pytest.log  : pytest log
     logs/[date]/trd.log     : case and result

-----------------------------------------------------------------------

- Restrictions :

  1. Only support chrome 
  2. Can't see the running steps in console , just in log folder

-----------------------------------------------------------------------