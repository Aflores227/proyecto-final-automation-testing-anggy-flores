# Proyecto Final Automatización

## Propósito del Proyecto

Este repositorio contiene un conjunto de pruebas automatizadas (UI y API) implementadas con el patrón Page Object Model (POM). Las pruebas verifican el flujo de login, agregar/eliminar productos del carrito y el proceso de checkout en la demo de ejemplo, además de pruebas de API de ejemplo.

El proyecto fue desarrollado con fines de aprendizaje, explorando buenas prácticas en pruebas automatizadas utilizando las herramientas Selenium y Pytest.

## Tecnologías Utilizadas

- **Python 3.x**
- **Selenium** 
- **Pytest** 
- **WebDriver Manager (`webdriver-manager`) — descarga automática del chromedriver**
- **Pytest HTML (`pytest-html`) — generación de reportes HTML**
- **Requests (`requests`) — para pruebas de API (ejemplos)**

## Estructura del proyecto
- `page/` — clases POM:
  - [`page.login_page.LoginPage`](page/login_page.py)
  - [`page.inventory_page.InventoryPage`](page/inventory_page.py)
  - [`page/cart_page.CartPage`](page/cart_page.py)
  - [`page.checkout_page.CheckoutPage`](page/checkout_page.py)
- `test/` — tests Pytest (e.g. `test_login_page.py`, `test_cart_page.py`, `test_inventory_page.py`, `test_checkout_page.py`)
- `utils/` — helpers (p. ej. [`utils/helpers.py`](utils/helpers.py))
- `data/` — datos de prueba: [`data/login.json`](data/login.json) y loader [`data/login.py`](data/login.py)
- `reports/` — reportes HTML (`reports/report.html`)
- `screenshots/` — capturas tomadas por el hook en [`conftest.py`](conftest.py) cuando un test falla


## Instalación

1. **Clona este repositorio:**

```bash
git clone https://github.com/Aflores227/proyecto-final-automation-testing-anggy-flores.git
cd proyecto-final-automation-testing-anggy-flores
```

2. **Instalar dependencias necesarias:**

```bash
pip install selenium webdriver-manager pytest pytest-html requests
```

## Comando para ejecutar las pruebas

```bash
python -m pytest -v
```

Si desea ejecutar un sólo test, usar:
```bash
python -m pytest test/test_login_page.py::test_login_user -q
```

Interpretación de los reportes generados
- El reporte HTML principal se genera en reports/report.html (ver configuración en pytest.ini).
- El reporte muestra resumen de pruebas (pasadas, falladas, duraciones) y entradas por test.
- Para tests fallidos:
  - El hook en conftest.py guarda una captura en la carpeta screenshots/ (screenshots/<test_name>_YYYY_MM_DD_HH-MM-SS.png). Ver carpeta: screenshots/
  - El HTML incluye detalles y logs para cada test; abrir reports/report.html en un navegador para ver la vista completa.

## Autora

[Anggy Flores](anggymartina@gmail.com)
