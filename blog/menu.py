# menu.py


def mostrar_menu():
    """Muestra el menú y retorna la opción elegida como número entero (o None si es inválida)."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    try:
        return int(input("Elegí una opción: "))
    except ValueError:
        # Si el usuario escribe texto en lugar de un número
        print("Error: ingresá un número del 1 al 5.")
        return None


def pedir_texto(mensaje):
    """Pide un texto por consola y lo retorna sin espacios sobrantes."""
    return input(mensaje).strip()