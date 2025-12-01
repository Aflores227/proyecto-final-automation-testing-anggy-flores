from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from data.login import USERS

def test_shown_products(driver):
  username, password, login_bool = USERS[0]
  loginPage = LoginPage(driver)
  inventoryPage = InventoryPage(driver)

  # Login
  loginPage.openLoginPage()
  loginPage.loginUser(username, password)

  # Obtiene la lista de productos visibles
  products = inventoryPage.getAllProducts()
  assert products > 0

def test_add_product_to_cart(driver):
  username, password, login_bool = USERS[0]
  loginPage = LoginPage(driver)
  inventoryPage = InventoryPage(driver)

  # Login
  loginPage.openLoginPage()
  loginPage.loginUser(username, password)

  # Agrega producto al carrito y verifica que se haya agregado
  inventoryPage.addProductToCart(0)
  assert inventoryPage.getSelectedProducts() == 1

def test_remove_product(driver):
  username, password, login_bool = USERS[0]
  loginPage = LoginPage(driver)
  inventoryPage = InventoryPage(driver)

  # Login
  loginPage.openLoginPage()
  loginPage.loginUser(username, password)

  # Agrega producto al carrito
  inventoryPage.addProductToCart(0)
  assert inventoryPage.getSelectedProducts() == 1

  # Remueve el producto del carrito desde la página de productos y verifica que se haya removido
  inventoryPage.removeProduct(0)
  assert inventoryPage.getSelectedProducts() == 0
