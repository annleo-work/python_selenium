from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from  fixture.direction import DirectionHelper
class Application:
    def __init__(self):
        self.wd = WebDriver()
        #self.wd.implicitly_wait(90)
        self.session = SessionHelper(self)
        self.direction = DirectionHelper(self)

    def open(self):
        wd = self.wd
        wd.get("https://ioblik.com/")

    def destroy(self):
        self.wd.quit()