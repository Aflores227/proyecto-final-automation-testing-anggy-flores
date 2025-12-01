import time
from page.checkout_page import CheckoutPage
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from data.login import USERS

def test_go_to_checkout(driver):
  username, password, login_bool = USERS[0]
  loginPage = LoginPage(driver)
  inventoryPage = InventoryPage(driver)
  checkoutPage = CheckoutPage(driver)
  cartPage = CartPage(driver)

  # Login
  loginPage.openLoginPage()
  loginPage.loginUser(username, password)

  # Agrega un producto al carrito y va a la página de carrito
  inventoryPage.addProductToCart(0)
  cartPage.goToCart()

  # Redirige a la página de checkout
  checkoutPage.goToCheckout()
  assert "checkout-step-one.html" in driver.current_url

  # Redirige a la segunda página de checkout ingresando la información requerida
  checkoutPage.enterCheckoutInformation("Anggy", "Flores", "12345")
  checkoutPage.continueToStepTwo()
  assert "checkout-step-two.html" in driver.current_url
  