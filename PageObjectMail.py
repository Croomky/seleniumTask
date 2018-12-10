from PageObjectWP import PageObjectWP

class PageObjectMail(PageObjectWP):

    def __init__(self, webdriver):
        PageObjectWP.__init__(self, webdriver)
        PageObjectWP.ExecuteTest(self)

    def ExecuteTest(self):
        self.btnMail.click()
        formLogin = self.webdriver.find_element_by_name('login_username')
        formPassword = self.webdriver.find_element_by_name('password')
        btnLogin = self.webdriver.find_element_by_id('btnSubmit')

        # login to test acc
        formLogin.click()
        formLogin.send_keys('doej1')
        formPassword.click()
        formPassword.send_keys('johnny88')
        btnLogin.click()

    def GetTitle(self):
        return self.webdriver.title