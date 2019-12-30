#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Dec 29, 2019

@author: Tatyana
'''

import time

from locators import MainPageLocators
from locators import CreateLetterWindowLocators
from locators import SearchResultsPageLocators
from locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    def login(self, login, pwd):
        login_field = self.driver.find_element_by_id(LoginPageLocators.MAILBOX_LOGIN)
        print("entering login ...")
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable, login_field)
        login_field.click()
        login_field.send_keys(login)
        login_field.send_keys(Keys.ENTER)
        password_field = self.driver.find_element_by_id(LoginPageLocators.MAILBOX_PASSWORD)
        print("entering password ...")
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable, password_field)
        password_field.click()
        password_field.send_keys(pwd)
        password_field.send_keys(Keys.ENTER)
    
    
class MainPage(BasePage):
    """Home page action methods come here"""

    def click_compose_button(self):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(MainPageLocators.COMPOSE_BUTTON))
        compose_button = self.driver.find_element_by_xpath(MainPageLocators.COMPOSE_BUTTON_XPATH)
        WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located(MainPageLocators.LOADING_WINDOW))
        print("clicking button to create a new letter ...")
        compose_button.click()
        
        
    def search_for_letter(self, subject):
        search_input = self.driver.find_element_by_class_name(MainPageLocators.SEARCH_INPUT_CLASS_NAME)
        print("entering subject to search: " + subject)

        #time.sleep(3)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable, search_input)
        search_input.click()
        evolved_search_input = self.driver.find_element_by_xpath(MainPageLocators.EVOLVED_SEARCH_IMPUT_XPATH)
        evolved_search_input.send_keys(subject)
        
        # wait 3 sec until the mail is sent 
        time.sleep(3)
        evolved_search_input.send_keys(Keys.ENTER)

        

class CreateLetterWindow(BasePage):

    def create_letter(self, to, subject_title, body):
        to_field = self.driver.find_element_by_xpath(CreateLetterWindowLocators.TO_FIELD_XPATH)
        to_field.send_keys(to)
        subject = self.driver.find_element_by_xpath(CreateLetterWindowLocators.SUBJECT_XPATH)
        print("setting random subject: " + subject_title)
        subject.send_keys(subject_title)
        text_editor = self.driver.find_element_by_xpath(CreateLetterWindowLocators.TEXT_EDITOR_XPATH)
        text_editor.send_keys(body)
        first_button = self.driver.find_element_by_xpath(CreateLetterWindowLocators.SEND_BUTTON_XPATH)
        first_button.click()
        WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located(CreateLetterWindowLocators.CONFIRMATION_WINDOW))



class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_letter_sent(self, subject):
        is_letter_sent = False
        # TODO replace sleep with wait until send letter window disappears
        time.sleep(10)
        result_list = self.driver.find_elements_by_xpath(SearchResultsPageLocators.SEARCH_RESULT_LIST_XPATH)
        #WebDriverWait(driver, 60).until(EC.visibility_of, result_list)
        for res in result_list:
            #WebDriverWait(driver, 60).until(EC.visibility_of, res)
            letter_record = res.text
            print(" ---: ")
            print("found record: " + letter_record)
            print(" ---: ")
            if (SearchResultsPageLocators.SENT_LABEL in letter_record) and (subject in letter_record):
                print("Found the sent letter with the subject " + subject + " in sent letters")
                is_letter_sent = True
                break
        return is_letter_sent