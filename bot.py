from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
from secret import username, pw

binary = FirefoxBinary(r'C:\\Program Files\\Firefox Developer Edition\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)

class InstaBot:
  def __init__(self, username, pw):
    self.driver = driver
    self.driver.get('https://instagram.com')
    sleep(2)
    self.driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]')\
      .click()
    sleep(2)
    # login into account
    self.login()
    # dissmiss notification
    try:
      self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]')\
        .click()
    except:
      self.driver.find_element_by_xpath('//button[contains(text(), "Agora não")]')\
        .click()
    

  def login(self):
    self.driver.find_element_by_name('username')\
      .send_keys(username)
    self.driver.find_element_by_name('password')\
      .send_keys(pw)
    self.driver.find_element_by_xpath('//button[@type="submit"]')\
      .click()
    sleep(4)

my_bot = InstaBot(username, pw)