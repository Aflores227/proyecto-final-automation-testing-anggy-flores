import pytest
from data.login import USERS
from page.login_page import LoginPage

@pytest.mark.parametrize("username, password, login_bool", USERS)
def test_login_user(driver, username, password, login_bool):
  loginPage = LoginPage(driver)
  loginPage.openLoginPage()
  loginPage.loginUser(username, password)

  if login_bool:
    assert "inventory.html" in driver.current_url
  else:
      assert "inventory.html" not in driver.current_url