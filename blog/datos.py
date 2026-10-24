# datos.py
# Datos base del blog y persistencia en JSON (carga y guardado de posts.json)

import json
import os

from .modelos import Autor, Post

# Ruta de posts.json: siempre en la carpeta raíz del proyecto (donde está main.py)
RUTA_JSON = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "posts.json"
)

# ---------------------------------------------------------
# DATOS BASE (se mantienen de los módulos anteriores)
# ---------------------------------------------------------

# Perfil del autor como diccionario (sirve para construir el objeto Autor)
perfil_autor = {
    "nombre": "Alejandro Díaz",
    "bio": "Analista de Impuestos, estudiante de Licenciatura en Economía y de Data Science",
    "especialidad": "Gestión de compras, pagos y análisis impositivo",
    "redes_sociales": ["@alediazvallera", "@laleitor_30"]
}

# Objeto Autor principal, usado para crear posts nuevos desde el menú
autor_principal = Autor.from_dict(perfil_autor)

# Tupla con los estados posibles de un post
estados_post = ("borrador", "publicado", "archivado")

# Set de etiquetas (se repite "Python" para comprobar que no se duplica)
etiquetas_blog = {"Python", "Data Science", "Pandas", "Web", "Backend", "Python"}

# Posts iniciales: se usan si posts.json no existe o no se puede leer
# (el post 4 tiene errores a propósito para probar la validación)
posts_iniciales = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Introducción a Pandas",
        "contenido": "Pandas es una librería para analizar datos en Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Pandas", "Data Science"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con diccionarios",
        "contenido": "Los diccionarios permiten guardar datos con pares clave-valor.",
        "autor": perfil_autor,
        "tags": ["Python", "Diccionarios"],
        "estado": "archivado"
    },
    {
        "id": 4,
        "titulo": "Post con errores",
        "contenido": "",                # error: contenido vacío
        "autor": perfil_autor,
        "tags": "Python",               # error: tags no es una lista
        "estado": "pendiente"           # error: estado no válido
    }
]

# ---------------------------------------------------------
# PERSISTENCIA JSON
# ---------------------------------------------------------


def convertir_a_posts(lista_dicts):
    """Convierte una lista de diccionarios en objetos Post.
    Los diccionarios incompletos se omiten mostrando un mensaje."""
    posts = []
    for indice, datos in enumerate(lista_dicts, start=1):
        try:
            posts.append(Post.from_dict(datos))
        except ValueError as error:
            print(f"Aviso: se omitió el elemento {indice} de posts.json ({error}).")
    return posts


def cargar_posts(ruta=RUTA_JSON):
    """Carga los posts desde el archivo JSON y retorna una lista de objetos Post.
    Si el archivo no existe, está vacío o es inválido, usa los posts iniciales."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)
    except FileNotFoundError:
        print("Aviso: no se encontró posts.json. Se cargan los posts iniciales.")
        return convertir_a_posts(posts_iniciales)
    except json.JSONDecodeError:
        print("Aviso: posts.json está vacío o tiene contenido inválido. Se cargan los posts iniciales.")
        return convertir_a_posts(posts_iniciales)
    except OSError as error:
        print(f"Aviso: no se pudo leer posts.json ({error}). Se cargan los posts iniciales.")
        return convertir_a_posts(posts_iniciales)

    # El JSON debe contener una lista de posts
    if not isinstance(contenido, list):
        print("Aviso: posts.json no contiene una lista de posts. Se cargan los posts iniciales.")
        return convertir_a_posts(posts_iniciales)

    return convertir_a_posts(contenido)


def guardar_posts(posts, ruta=RUTA_JSON):
    """Convierte los posts (objetos) a diccionarios y los guarda en el archivo JSON.
    Retorna True si se guardó bien, False si hubo un error."""
    try:
        lista_dicts = [post.to_dict() for post in posts]
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(lista_dicts, archivo, indent=4, ensure_ascii=False)
        return True
    except (OSError, TypeError, AttributeError) as error:
        print(f"Error: no se pudieron guardar los posts ({error}).")
        return False