import selenium
from time import sleep
from SeleniumContextManager import SeleniumContextManager

class PageObjectWP():

    def __init__(self, webdriver):
        #SeleniumContextManager.__init__(self)
        #self.webdriver = selenium.webdriver.Firefox(executable_path='C:\\Users\\Konrad\\Documents\\Projects\\VSCode\\seleniumTask\\geckodriver.exe')
        self.webdriver = webdriver
        self.webdriver.get('https://www.wp.pl')
        #self.btnSerwisy = self.webdriver.find_element_by_xpath("//a[contains(@class, 'sc-1ug11d0-4 keIEdq')]")
        self.btnExitCookieModal = self.webdriver.find_element_by_xpath("//*[contains(text(), '×')]")
        self.btnMail = self.webdriver.find_element_by_xpath("//*[contains(text(), 'Poczta')]")
        self.btnWpPilot = self.webdriver.find_element_by_xpath("//*[contains(text(), 'WP Pilot')]")

    def ExecuteTest(self):
        # enter mail sub-page
        self.btnExitCookieModal.click()
        sleep(2)
