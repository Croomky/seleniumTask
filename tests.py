import unittest
from selenium import webdriver 
from PageObjectWP import PageObjectWP
from PageObjectMail import PageObjectMail
from PageObjectWpPilot import PageObjectWpPilot

class WpTest(unittest.TestCase):

    def setUp(self):
        self.webdriver = webdriver.Firefox(executable_path='C:\\Users\\Konrad\\Documents\\Projects\\VSCode\\seleniumTask\\geckodriver.exe')
        self.mainPage = PageObjectWP(self.webdriver)

    def testMainPage(self):
        self.assertEqual(self.mainPage.webdriver.title, 'Wirtualna Polska - Wszystko co ważne - www.wp.pl')

    def tearDown(self):
        self.webdriver.close()
        self.webdriver.quit()

class WpMailTest(unittest.TestCase):

    def setUp(self):
        self.webdriver = webdriver.Firefox(executable_path='C:\\Users\\Konrad\\Documents\\Projects\\VSCode\\seleniumTask\\geckodriver.exe')
        self.mailPage = PageObjectMail(self.webdriver)
        self.mailPage.ExecuteTest()

    def testMailPage(self):
        self.assertIn('WP Poczta', self.webdriver.title)

    def tearDown(self):
        self.webdriver.close()
        self.webdriver.quit()

class WpPilotTest(unittest.TestCase):

    def setUp(self):
        self.webdriver = webdriver.Firefox(executable_path='C:\\Users\\Konrad\\Documents\\Projects\\VSCode\\seleniumTask\\geckodriver.exe')
        self.pilotPage = PageObjectWpPilot(self.webdriver)
        self.pilotPage.ExecuteTest()

    def testPilotPage(self):
        self.assertIn('online', self.webdriver.title)

    def tearDown(self):
        self.webdriver.close()
        self.webdriver.quit()