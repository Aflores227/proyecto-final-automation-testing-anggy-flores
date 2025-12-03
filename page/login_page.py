from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import URL

WAIT_SECONDS = 5

class LoginPage:
  def __init__(self, driver):
    self.driver = driver

    self.username = (By.NAME, "user-name")
    self.password = (By.NAME, "password")
    self.login_button = (By.NAME, "login-button")

  def openLoginPage(self):
    self.driver.get(URL)

  def loginUser(self, username, password):
    WebDriverWait(self.driver, WAIT_SECONDS).until(EC.element_to_be_clickable(self.username)
      ).send_keys(username)

    WebDriverWait(self.driver, WAIT_SECONDS).until(EC.element_to_be_clickable(self.password)
      ).send_keys(password)
  
    WebDriverWait(self.driver, WAIT_SECONDS).until(EC.element_to_be_clickable(self.login_button)
    ).click()