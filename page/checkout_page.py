from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_SECONDS = 10

class CheckoutPage:
  def __init__(self, driver):
    self.driver = driver

    self.first_name = (By.ID, "first-name")
    self.last_name = (By.ID, "last-name")
    self.postal_code = (By.ID, "postal-code")
    self.continue_button = (By.ID, "continue")
    self.finish_button = (By.ID, "finish")

  def goToCheckout(self):
    self.driver.find_element(By.CLASS_NAME, "checkout_button").click()

  def enterCheckoutInformation(self, first_name, last_name, postal_code):
    self.driver.find_element(*self.first_name).send_keys(first_name)
    self.driver.find_element(*self.last_name).send_keys(last_name)
    self.driver.find_element(*self.postal_code).send_keys(postal_code)

  def continueToStepTwo(self):
    WebDriverWait(self.driver, WAIT_SECONDS).until(EC.element_to_be_clickable(self.continue_button)).click()
