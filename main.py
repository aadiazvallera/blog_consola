# main.py

from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import (
    listar_posts,
    buscar_por_titulo,
    filtrar_por_tag,
    mostrar_resultados,
)
from blog.validaciones import validar_post


def validar_todos(lista):
    """Recorre la lista y muestra si cada post es válido o tiene errores."""
    print("\nValidación de posts:")
    for indice, post in enumerate(lista, start=1):
        es_valido, mensaje = validar_post(post)
        if es_valido:
            print(f"Post {indice}: válido")
        else:
            print(f"Post {indice}: error - {mensaje}")


if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = pedir_texto("Buscar por titulo: ")
            if termino == "":
                print("La búsqueda no puede estar vacía.")
            else:
                print("\nResultados de la búsqueda:")
                mostrar_resultados(buscar_por_titulo(posts, termino),
                                   "No se encontraron posts con ese título.")

        elif opcion == 3:
            tag = pedir_texto("Ingresá un tag: ")
            if tag == "":
                print("El tag no puede estar vacío.")
            else:
                print(f"\nPosts con el tag {tag}:")
                mostrar_resultados(filtrar_por_tag(posts, tag),
                                   "No se encontraron posts con ese tag.")

        elif opcion == 4:
            validar_todos(posts)

        elif opcion == 5:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        elif opcion is not None:
            # Número fuera de rango (si es None, el error ya se mostró en el menú)
            print("Opción inválida, intenta de nuevo")