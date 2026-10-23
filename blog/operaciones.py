# operaciones.py


def obtener_nombre_autor(post):
    """Retorna el nombre del autor de un post, o un texto por defecto si no se puede obtener."""
    autor = post.get("autor") if isinstance(post, dict) else None
    if isinstance(autor, dict):
        return autor.get("nombre", "Autor desconocido")
    return "Autor desconocido"


def mostrar_post(post):
    """Imprime título, autor y estado de un post."""
    titulo = post.get("titulo", "(sin título)")
    estado = post.get("estado", "sin estado")
    print(f"- {titulo} | Autor: {obtener_nombre_autor(post)} | Estado: {estado}")


def listar_posts(lista):
    """Recibe la lista de posts y muestra título, autor y estado de cada uno."""
    if not lista:
        print("No hay posts para mostrar.")
        return
    print("\nPosts disponibles:")
    for post in lista:
        if isinstance(post, dict):
            mostrar_post(post)
        else:
            print("- (post inválido)")


def buscar_por_titulo(lista, termino):
    """Retorna los posts cuyo título contiene el término (sin distinguir mayúsculas)."""
    resultados = []
    for post in lista:
        if not isinstance(post, dict):
            continue
        titulo = str(post.get("titulo", ""))
        if termino.lower() in titulo.lower():
            resultados.append(post)
    return resultados


def filtrar_por_tag(lista, tag):
    """Retorna los posts que tienen el tag indicado (sin distinguir mayúsculas)."""
    resultados = []
    for post in lista:
        if not isinstance(post, dict):
            continue
        tags_post = post.get("tags", [])
        # Solo se recorren los tags si realmente es una lista
        if isinstance(tags_post, list):
            for t in tags_post:
                if str(t).lower() == tag.lower():
                    resultados.append(post)
                    break
    return resultados


def mostrar_resultados(resultados, mensaje_vacio):
    """Muestra una lista de resultados o un mensaje si está vacía."""
    if resultados:
        for post in resultados:
            mostrar_post(post)
    else:
        print(mensaje_vacio)