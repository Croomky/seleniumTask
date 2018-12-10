from selenium import webdriver
from time import sleep
from SeleniumContextManager import SeleniumContextManager
from PageObjectMail import PageObjectMail
from PageObjectWpPilot import PageObjectWpPilot


with SeleniumContextManager() as webdriver:
    # pom = PageObjectMail(webdriver)
    # pom.ExecuteTest()

    pop = PageObjectWpPilot(webdriver)
    pop.ExecuteTest()
    
    input()