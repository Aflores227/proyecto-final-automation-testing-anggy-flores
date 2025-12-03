from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_SECONDS = 10

class CartPage:
  def __init__(self, driver):
    self.driver = driver
    self.cart_button = (By.CLASS_NAME, 'shopping_cart_badge')
    self.cart_item = (By.CLASS_NAME, 'cart_item')

  def goToCart(self):
    WebDriverWait(self.driver, WAIT_SECONDS).until(EC.element_to_be_clickable(self.cart_button)).click()

  def getCartItemsCount(self):
    items = self.driver.find_elements(*self.cart_item)
    return len(items)