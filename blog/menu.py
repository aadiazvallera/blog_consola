# menu.py
# Muestra el menú y maneja la entrada del usuario


def mostrar_menu():
    """Muestra el menú y retorna la opción elegida como número entero (o None si es inválida)."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")
    try:
        return int(input("Elegí una opción: "))
    except ValueError:
        # Si el usuario escribe texto en lugar de un número
        print("Error: ingresá un número del 1 al 7.")
        return None


def pedir_texto(mensaje):
    """Pide un texto por consola y lo retorna sin espacios sobrantes."""
    return input(mensaje).strip()


def pedir_tags(mensaje):
    """Pide tags separados por coma y retorna una lista (ignora los vacíos)."""
    texto = input(mensaje)
    tags = []
    for parte in texto.split(","):
        tag = parte.strip()
        if tag != "":
            tags.append(tag)
    return tags