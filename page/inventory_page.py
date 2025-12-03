from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_SECONDS = 10

class InventoryPage:
  def __init__(self, driver):
    self.driver = driver
    self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
    self.add_product_to_cart = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    self.remove_product = (By.XPATH, "//button[contains(text(), 'Remove')]")

  def getAllProducts(self):
    products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
    return len(products)

  def addProductToCart(self, product_index = 0):
    add_to_cart_buttons = self.driver.find_elements(*self.add_product_to_cart)
    if add_to_cart_buttons and product_index < len(add_to_cart_buttons):
      add_to_cart_buttons[product_index].click()

  def removeProduct(self, product_index = 0):
    remove_buttons = self.driver.find_elements(*self.remove_product)
    if remove_buttons and product_index < len(remove_buttons):
      remove_buttons[product_index].click()
  
  def getSelectedProducts(self):
    selected_products = self.driver.find_elements(*self.remove_product)
    return len(selected_products)