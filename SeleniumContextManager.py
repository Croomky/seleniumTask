import selenium

class SeleniumContextManager:
    def __init__(self):
        self.webdriver = selenium.webdriver.Firefox(executable_path='C:\\Users\\Konrad\\Documents\\Projects\\VSCode\\seleniumTask\\geckodriver.exe')

    def __enter__(self):
        return self.webdriver

    def __exit__(self, type, value, traceback):
        # Print exception info
        if type != None:
            print('Exception type: {0}\nException value: {1}'.format(type, value))
        else:
            print('Webdriver closing without exceptions')

        # Safely close webdriver
        try:
            self.webdriver.close()
            self.webdriver.quit()
        except:
            pass