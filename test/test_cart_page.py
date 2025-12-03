from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from data.login import USERS

def test_add_product_to_cart(driver):
  username, password, login_bool = USERS[0]
  loginPage = LoginPage(driver)
  inventoryPage = InventoryPage(driver)
  cartPage = CartPage(driver)

  # Login
  loginPage.openLoginPage()
  loginPage.loginUser(username, password)
  # Agrega producto al carrito y verifica que se haya agregado
  inventoryPage.addProductToCart(0)
  cartPage.goToCart()
  assert cartPage.getCartItemsCount() == 1

def test_remove_product_from_cart(driver):
  username, password, login_bool = USERS[0]
  loginPage = LoginPage(driver)
  inventoryPage = InventoryPage(driver)
  cartPage = CartPage(driver)

  # Login
  loginPage.openLoginPage()
  loginPage.loginUser(username, password)

  # Agrega producto al carrito y verifica que se haya agregado
  inventoryPage.addProductToCart(0)
  # Redirige a la página de Cart y verifica que el producto esté ahí
  cartPage.goToCart()
  assert cartPage.getCartItemsCount() == 1

  # Remueve el producto del carrito desde la página de Cart y verifica que se haya removido
  inventoryPage.removeProduct(0)
  assert cartPage.getCartItemsCount() == 0

def test_add_product_to_cart_failed(driver):
  username, password, login_bool = USERS[0]
  loginPage = LoginPage(driver)
  inventoryPage = InventoryPage(driver)
  cartPage = CartPage(driver)

  # Login
  loginPage.openLoginPage()
  loginPage.loginUser(username, password)
  # Agrega producto al carrito
  inventoryPage.addProductToCart(0)
  cartPage.goToCart()
  # Este test está diseñado para fallar
  assert cartPage.getCartItemsCount() == 0