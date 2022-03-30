from selenium import webdriver
from datetime import datetime
from libs.logging_handler import getlogger
from libs.ini import *

mylogger = getlogger(logname=log_path , loggername="web_api.py")

import time
import os

class WebConnection():

    def __init__(self , browser_type , browser_location):
        if browser_type == "chrome":
            self.driver = webdriver.Chrome(browser_location)
            self.driver.maximize_window()

    def scroll_to_element(self):
        try:
            #from selenium.webdriver.common.action_chains import ActionChains
            #actions = ActionChains(self.driver)
            #actions.move_to_element(self.inputElement).perform()
            self.driver.execute_script("return arguments[0].scrollIntoView();", self.inputElement)
        except Exception as error:
            mylogger.error(error)

    def locate_frame(self):
        try:
            self.driver.switch_to.frame(self.inputElement)
        except Exception as error:
            mylogger.error(error)
		
    def default_frame(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as error:
            mylogger.error(error)
            
    def script_click(self):
        try:
            self.driver.execute_script("arguments[0].click();", self.inputElement)
            mylogger.debug("Click script element : {}".format(self.inputElement))
            return True
        except Exception as error:
            mylogger.error(error)
            return False
            
    
    def open(self , get_url=None):
        try:
            self.driver.get(get_url)
        except Exception as error:
            mylogger.error(error)

    def screenshot(self , delay = 3):
        try:
            delays(delay)
            now = datetime.now()
            current_time = now.strftime("%Y_%m_%d_%H_%M_%S")
            self.driver.get_screenshot_as_file(img_path+current_time+".jpg")
            mylogger.debug("Take a screenshot : {}".format(img_path+current_time+".jpg"))
        except Exception as error:
            mylogger.error(error)
            
    def wait_element(self , element):
        try:
            for i in range(10):
                mylogger.debug("Wait for locating element : {}".format(element))
                delays(3)

                if self.locate_xpath(xpath=element):
                    self.scroll_to_element()
                    mylogger.debug("Found element : {}".format(self.inputElement))
                    return True
        except Exception as error:
            mylogger.error(error)
            
            return False

    def locate_xpath(self,xpath):
        try:
            self.inputElement = self.driver.find_element_by_xpath(xpath)
            
            return True
        except Exception as error:
            mylogger.error(error)
            return False

    def close(self):
        try:
            self.driver.quit()
        except Exception as error:
            mylogger.error(error)

    def refresh(self):
        try:
            self.driver.refresh()
        except Exception as error:
            mylogger.error(error)

    def locate_xpath(self,xpath):
        try:
            self.inputElement = self.driver.find_element_by_xpath(xpath)
            return True
        except Exception as error:
            mylogger.error(error)
            return False

    def click_button(self):
        try:
            self.inputElement.click()
            mylogger.debug("Click element : {}".format(self.inputElement))
            return True
        except Exception as error:
            mylogger.error(error)
            return False

    def send_keys(self,keys):
        try:
            self.inputElement.send_keys(keys)
        except Exception as error:
            mylogger.error(error)

    def label_get(self):
        try:
            self.value =self.inputElement.text
            return self.value
        except Exception as error:
            mylogger.error(error)

def delays(seconds, reason = ""):
    if seconds > 3:
        if reason == "":
            print("Waiting for %d seconds..." %seconds)
        else:
            print("Waiting for %d seconds due to %s..." %(seconds, reason))

        current = seconds
        while current > 0:
            time.sleep(1)
            current -= 1
            second_str = "%d seconds...\r" %current
            print(second_str, end='')
        print("")
    else:
        time.sleep(seconds)

if web_type == "chrome":
    browser_location = driver_chrome
    os.system("taskkill /f /im chromedriver.exe")

web_test = WebConnection(browser_type = web_type , browser_location = browser_location)

def Web_Open():
    web_test.open(get_url=test_url)

def Web_Click(element):
    state = web_test.wait_element(element)
    if state:
        click_state = web_test.click_button()
        web_test.screenshot()
        if click_state:
            return True
        else:
            return False
    else:
        return False

def Web_Script_Click(element):
    state = web_test.wait_element(element)
    if state:
        click_state = web_test.script_click()
        web_test.screenshot()
        if click_state:
            return True
        else:
            return False
    else:
        return False
        
def Web_Close():
    web_test.close()

def Web_Input(element , input_data):
    state = web_test.wait_element(element)
    if state:
        web_test.send_keys(input_data)
        web_test.screenshot()

def Web_Get_Text(element):
    ret = None
    state = web_test.wait_element(element)
    if state:
        ret = web_test.label_get()
        web_test.screenshot()

    return ret

def Web_Select_Frame(element):
    state = web_test.wait_element(element)
    if state:
        ret = web_test.locate_frame()
        web_test.screenshot()
    
    
def Web_Default_Frame():
    web_test.default_frame()
