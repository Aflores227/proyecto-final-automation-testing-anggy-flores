import pytest
from utils.helpers import get_driver

@pytest.fixture(scope="function")
def driver():
    """Proporciona un WebDriver y cierra la sesión al final de la prueba."""
    driver = get_driver()
    yield driver
    try:
        driver.quit()
    except Exception:
        pass