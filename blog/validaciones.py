# validaciones.py
# Reglas lógicas para validar la estructura de los posts

# Claves obligatorias que debe tener cada post
CLAVES_OBLIGATORIAS = ("id", "titulo", "contenido", "autor", "tags", "estado")


def validar_post(post, estados_validos):
    """Valida la estructura de un post (diccionario).
    Retorna (True, mensaje) o (False, mensaje de error)."""
    # Debe ser un diccionario
    if not isinstance(post, dict):
        return False, "el post no es un diccionario"

    # Deben existir todas las claves obligatorias
    for clave in CLAVES_OBLIGATORIAS:
        if clave not in post:
            return False, f'falta la clave "{clave}"'

    # titulo y contenido no pueden estar vacíos
    if not str(post["titulo"]).strip():
        return False, 'el "titulo" está vacío'
    if not str(post["contenido"]).strip():
        return False, 'el "contenido" está vacío'

    # autor debe ser un diccionario con la clave "nombre"
    if not isinstance(post["autor"], dict):
        return False, 'el "autor" no es un diccionario'
    if "nombre" not in post["autor"]:
        return False, 'el autor no tiene la clave "nombre"'

    # tags debe ser una lista
    if not isinstance(post["tags"], list):
        return False, 'los "tags" no son una lista'

    # estado debe estar entre los estados definidos
    if post["estado"] not in estados_validos:
        return False, f'el estado "{post["estado"]}" no es válido'

    return True, "válido"