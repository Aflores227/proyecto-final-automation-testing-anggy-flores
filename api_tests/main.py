# Este archivo abarca el ejercicio 2. Pruebas de API (Requests)

#pip install requests - Para que puedan correr los tests se debe instalar la librería requests primero 

import requests

URL_API = "https://jsonplaceholder.typicode.com/"
NOT_FOUND_CODE = 404
CREATED_CODE = 201
SUCCESS_CODE = 200

# En este método se obtiene info de los posts
def get_posts():
  print('Get Posts')
  response = requests.get(URL_API + "posts")
  print(response.status_code)
  assert response.status_code == SUCCESS_CODE
  data = response.json()
  print(data)

# En este método se crea un nuevo post de ejemplo
def post_post():
  print('Create a new post')
  new_post = {
    "userId": 1,
    "title": "Post Automatización Ejemplo",
    "body": "Este es un ejemplo de un nuevo post"
  }
  response = requests.post(URL_API + "posts", new_post)
  # En esta linea verificamos que el post se creó correctamente
  # antes de avanzar a mostrar el resultado del post
  assert response.status_code == CREATED_CODE
  print(response.status_code)
  data = response.json()
  print(data)

# En este método se elimina un post
def delete_post():
  print("Delete a post")
  post_id = "100"
  response = requests.delete(URL_API + "posts/" + post_id)
  print(response.status_code)
  assert response.status_code != NOT_FOUND_CODE, "Error al eliminar el post"

get_posts()
# post_post()
# delete_post()