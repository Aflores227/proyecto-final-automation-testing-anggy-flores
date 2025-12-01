import pytest
from utils.helpers import get_driver
from pathlib import Path
from datetime import datetime

try:
    from pytest_html import extras
except Exception:
    extras = None

@pytest.fixture(scope="function")
def driver():
    """Proporciona un WebDriver y cierra la sesión al final de la prueba."""
    driver = get_driver()
    yield driver
    try:
        driver.quit()
    except Exception:
        pass

def pytest_configure(config):
    Path("reports").mkdir(exist_ok=True)
    try:
        if hasattr(config, "_metadata"):
            config._metadata['Project'] = 'Proyecto Final Automation'
            config._metadata['Platform'] = f'{Path().resolve()}'
    except Exception:
        pass

def pytest_html_report_title(report):
    report.title = "Reporte HTML - Proyecto Final Automation"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None and extras is not None:
            try:
                png = driver.get_screenshot_as_base64()
                timestamp = datetime.utcnow().isoformat(timespec='seconds')
                img_html = f'<div><p>Screenshot at {timestamp} (UTC)</p><img src="data:image/png;base64,{png}" alt="screenshot" style="max-width:100%;"></div>'
                extra = getattr(report, "extra", [])
                extra.append(extras.html(img_html))
                report.extra = extra
            except Exception:
                pass