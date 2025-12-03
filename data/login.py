import json
from pathlib import Path

DEFAULT_USERS = [
  ("standard_user", "secret_sauce", True),
  ("locked_out_user", "secret_sauce", False),
  ("problem_user", "bad_password", False),
]

# Obtiene el directorio de los datos
DATA_DIR = Path(__file__).parent
# Nombre del archivo JSON
JSON_PATH = DATA_DIR / "login.json"

def loadFromJson(path):
  with path.open(encoding="utf-8") as new_file:
    data = json.load(new_file)
  users = []
  for item in data:
    username = item.get("username")
    password = item.get("password")
    should_login = item.get("login_bool")
    if username and password:
      users.append((username, password, should_login))
  return users

if JSON_PATH.exists():
    USERS = loadFromJson(JSON_PATH)
else:
    USERS = DEFAULT_USERS