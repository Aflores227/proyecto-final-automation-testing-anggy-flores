import pytest
import time
from utils.helpers import get_driver
from pathlib import Path

# Directorio donde se guardarán las capturas
SCREENSHOTS_DIR = Path(__file__).parent / "screenshots"
SCREENSHOTS_DIR.mkdir(exist_ok=True, parents=True)

@pytest.fixture(scope="function")
def driver():
    """Proporciona un WebDriver y cierra la sesión al final de la prueba."""
    driver = get_driver()
    yield driver
    try:
        driver.quit()
    except Exception:
        pass

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para tomar capturas de pantalla en caso de fallo de la prueba."""
    outcome = yield
    result = outcome.get_result()

    # Revisa si el test falló
    if result.when == "call" and result.failed:
        driver = item.funcargs.get('driver')
        if driver:
            timestamp = time.strftime("%Y_%m_%d_%H-%M-%S")
            screenshot_filename = f"{item.name}_{timestamp}.png"
            screenshot_path = SCREENSHOTS_DIR / screenshot_filename
            try:
                driver.save_screenshot(str(screenshot_path))
            except Exception as e:
                print(f"No se pudo guardar la captura de pantalla: {e}")
