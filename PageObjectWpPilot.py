import selenium
from time import sleep
from PageObjectWP import PageObjectWP
from credentials import testPassword, testUsername

class PageObjectWpPilot(PageObjectWP):

    def __init__(self, webdriver):
        PageObjectWP.__init__(self, webdriver)
        PageObjectWP.ExecuteTest(self)

    def ExecuteTest(self):
        self.btnWpPilot.click()
        # # go to login page
        # btnLogin = self.webdriver.find_element_by_xpath("//*[contains(text(), 'Logowanie')]")
        # btnLogin.click()

        # # log in
        # formUsername = self.webdriver.find_element_by_xpath("//*[contains(@id, 'login-field')]")
        # formUsername.send_keys(testUsername + '@wp.pl')
        # sleep(2)
        # formPassword = self.webdriver.find_element_by_xpath("//*[contains(@id, 'login-password-field')]")
        # formPassword.send_keys(testPassword)
        # sleep(2)
        # formCaptcha = self.webdriver.find_element_by_xpath("//*[contains(@class, 'g-recaptcha')]")
        # action = selenium.webdriver.common.action_chains.ActionChains(self.webdriver)
        # action.move_to_element_with_offset(formCaptcha, 26, 37)
        # action.click().perform()
        # sleep(5)
        # formSubmit = self.webdriver.find_element_by_xpath("//*[contains(@type, 'submit')]")
        # formSubmit.click()

        # # enter profile
        # btnProfile = self.webdriver.find_element_by_xpath("//*[contains(@class, 'logged-in']/[contains(text(), 'Profil')]")
        # btnProfile.click()

