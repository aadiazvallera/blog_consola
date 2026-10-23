# datos.py

# Diccionario con el perfil del autor
perfil_autor = {
    "nombre": "Alejandro Díaz",
    "bio": "Analista de Impuestos, estudiante de Licenciatura en Economía y de Data Science",
    "especialidad": "Gestión de compras, pagos y análisis impositivo",
    "redes_sociales": ["@alediazvallera", "@laleitor_30"]
}

# Tupla con los estados posibles de un post
estados_post = ("borrador", "publicado", "archivado")

# Set de etiquetas (se repite "Python" para comprobar que no se duplica)
etiquetas_blog = {"Python", "Data Science", "Pandas", "Web", "Backend", "Python"}

# Lista de posts (el post 4 tiene errores a propósito para probar la validación)
posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python.",
        "autor": perfil_autor,
        "categoria": "Programación",
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Introducción a Pandas",
        "contenido": "Pandas es una librería para analizar datos en Python.",
        "autor": perfil_autor,
        "categoria": "Data Science",
        "tags": ["Python", "Pandas", "Data Science"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con diccionarios",
        "contenido": "Los diccionarios permiten guardar datos con pares clave-valor.",
        "autor": perfil_autor,
        "categoria": "Programación",
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