#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Dec 29, 2019

@author: Tatyana
'''
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    COMPOSE_BUTTON_XPATH = "//*[@class='compose-button__wrapper']"
    COMPOSE_BUTTON = (By.XPATH, COMPOSE_BUTTON_XPATH)
    LOADING_WINDOW = (By.ID, "app-loader")
    SEARCH_INPUT_CLASS_NAME = "search-panel-button__text"
    EVOLVED_SEARCH_IMPUT_XPATH = "//*[@class='react-async search-panel__layer']//input"

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    SEARCH_RESULT_LIST_XPATH = "//*[@class='dataset__items']/a/div[@class='llc__container']"
    SENT_LABEL ='Отправленные'

class LoginPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
    MAILBOX_LOGIN = "mailbox:login"
    MAILBOX_PASSWORD = "mailbox:password"

class CreateLetterWindowLocators(object):
    """A class for create letter window locators. All create letter window locators should come here"""
    CONFIRMATION_WINDOW = (By.XPATH, "//*[@class='layer-window__container']")
    TO_FIELD_XPATH = "//*[@data-type='to']//input"
    SUBJECT_XPATH = "//input[@name='Subject']"
    TEXT_EDITOR_XPATH = "//*[@role='textbox']"
    SEND_BUTTON_XPATH = "//div[@class='compose-app__buttons']/span[1]"
