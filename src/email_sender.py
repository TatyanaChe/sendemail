#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Dec 29, 2019

@author: Tatyana
'''
import unittest
import uuid
import page
import os

from selenium import webdriver
from selenium.webdriver import ChromeOptions

class Test(unittest.TestCase):
    
    def setUp(self):
        driver_location = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/driver/chrome/v79/ubuntu/chromedriver"
        print(driver_location)
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(driver_location, chrome_options=options)
        self.driver.implicitly_wait(20)
        self.driver.get('https://mail.ru')
        self.generated_subject = uuid.uuid4().hex # get a random string in a UUID fromat
        self.generated_subject  = self.generated_subject.upper()[0:10] # convert it in a uppercase letter and trim it
        

    def tearDown(self):
        self.driver.close()

    def testSendEmail(self):
        
        login_page = page.LoginPage(self.driver)
        login_page.login("t.che2020", "LtlVfpfq1pfqws")
        
        main_page = page.MainPage(self.driver)
        main_page.click_compose_button()
        
        create_letter_window = page.CreateLetterWindow(self.driver)
        create_letter_window.create_letter("t.che2020@mail.ru", self.generated_subject, "Letter content goes here ...")
        
        main_page.search_for_letter(self.generated_subject)
        search_result_page = page.SearchResultsPage(self.driver)
        is_letter_sent = search_result_page.is_letter_sent(self.generated_subject)
        
        print("Test completed.")
        assert is_letter_sent, "The letter is not sent"

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
