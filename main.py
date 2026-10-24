# main.py
# Archivo principal: crea la instancia de Blog y coordina el menú

import sys
from pathlib import Path

# Permite importar el paquete `blog` desde la carpeta del proyecto al ejecutar este archivo.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from importlib import import_module

_datos = import_module("blog.datos")
cargar_posts = _datos.cargar_posts
guardar_posts = _datos.guardar_posts
estados_post = _datos.estados_post
autor_principal = _datos.autor_principal

_menu = import_module("blog.menu")
mostrar_menu = _menu.mostrar_menu
pedir_texto = _menu.pedir_texto
pedir_tags = _menu.pedir_tags
Blog = import_module("blog.modelos").Blog


def crear_post_desde_consola(blog):
    """Pide los datos por consola y crea un nuevo post en el blog."""
    titulo = pedir_texto("Título: ")
    contenido = pedir_texto("Contenido: ")
    tags = pedir_tags("Tags (separados por coma): ")
    estado = pedir_texto("Estado (borrador/publicado/archivado) [Enter = borrador]: ").lower()

    if estado == "":
        estado = "borrador"
    if estado not in estados_post:
        print("Error: estado no válido. No se creó el post.")
        return
    if not tags:
        print("Error: ingresá al menos un tag. No se creó el post.")
        return

    try:
        nuevo = blog.crear_post(titulo, contenido, autor_principal, tags, estado)
        print(f"Post creado con id {nuevo.id}. Recordá guardarlo con la opción 6.")
    except ValueError as error:
        print(f"Error: {error}. No se creó el post.")


if __name__ == "__main__":
    # Se cargan los posts desde posts.json y se crea la instancia de Blog
    blog = Blog(cargar_posts())

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            blog.listar_posts()

        elif opcion == 2:
            termino = pedir_texto("Buscar por titulo: ")
            if termino == "":
                print("La búsqueda no puede estar vacía.")
            else:
                print("\nResultados de la búsqueda:")
                blog.mostrar_posts(blog.buscar_por_titulo(termino),
                                   "No se encontraron posts con ese título.")

        elif opcion == 3:
            tag = pedir_texto("Ingresá un tag: ")
            if tag == "":
                print("El tag no puede estar vacío.")
            else:
                print(f"\nPosts con el tag {tag}:")
                blog.mostrar_posts(blog.filtrar_por_tag(tag),
                                   "No se encontraron posts con ese tag.")

        elif opcion == 4:
            crear_post_desde_consola(blog)

        elif opcion == 5:
            blog.validar_posts(estados_post)

        elif opcion == 6:
            if guardar_posts(blog.obtener_posts()):
                print("Posts guardados en posts.json.")

        elif opcion == 7:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        elif opcion is not None:
            # Número fuera de rango (si es None, el error ya se mostró en el menú)
            print("Opción inválida, intenta de nuevo")