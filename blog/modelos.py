# modelos.py
# Clases principales del sistema: Autor, Post y Blog

from .validaciones import validar_post


class Autor:
    """Representa a una persona autora del blog."""

    def __init__(self, nombre, bio="", especialidad="", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales if redes_sociales is not None else []

    def to_dict(self):
        """Convierte el autor a diccionario (compatible con JSON)."""
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }

    @classmethod
    def from_dict(cls, datos):
        """Crea un Autor a partir de un diccionario. Lanza ValueError si está incompleto."""
        if not isinstance(datos, dict):
            raise ValueError("el autor no es un diccionario")
        if "nombre" not in datos:
            raise ValueError('el autor no tiene la clave "nombre"')
        return cls(
            datos["nombre"],
            datos.get("bio", ""),
            datos.get("especialidad", ""),
            datos.get("redes_sociales", [])
        )


class Post:
    """Representa una publicación del blog. El autor es una instancia de Autor."""

    CLAVES_OBLIGATORIAS = ("id", "titulo", "contenido", "autor", "tags", "estado")

    def __init__(self, id_post, titulo, contenido, autor, tags, estado):
        self.id = id_post
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        """Convierte el post (y su autor) a diccionario compatible con JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def from_dict(cls, datos):
        """Crea un Post a partir de un diccionario. Lanza ValueError si está incompleto."""
        if not isinstance(datos, dict):
            raise ValueError("el post no es un diccionario")
        for clave in cls.CLAVES_OBLIGATORIAS:
            if clave not in datos:
                raise ValueError(f'falta la clave "{clave}"')
        autor = Autor.from_dict(datos["autor"])
        return cls(
            datos["id"],
            datos["titulo"],
            datos["contenido"],
            autor,
            datos["tags"],
            datos["estado"]
        )

    def __str__(self):
        return f"- {self.titulo} | Autor: {self.autor.nombre} | Estado: {self.estado}"


class Blog:
    """Centraliza la lógica principal: maneja la lista de objetos Post."""

    def __init__(self, posts=None):
        self.posts = posts if posts is not None else []

    def obtener_posts(self):
        """Retorna todos los posts cargados."""
        return self.posts

    def mostrar_posts(self, lista, mensaje_vacio):
        """Muestra una lista de posts o un mensaje si está vacía."""
        if lista:
            for post in lista:
                print(post)
        else:
            print(mensaje_vacio)

    def listar_posts(self):
        """Muestra todos los posts del blog."""
        print("\nPosts disponibles:")
        self.mostrar_posts(self.posts, "No hay posts para mostrar.")

    def buscar_por_titulo(self, termino):
        """Retorna los posts cuyo título contiene el término (sin distinguir mayúsculas)."""
        resultados = []
        for post in self.posts:
            if termino.lower() in str(post.titulo).lower():
                resultados.append(post)
        return resultados

    def filtrar_por_tag(self, tag):
        """Retorna los posts que tienen el tag indicado (sin distinguir mayúsculas)."""
        resultados = []
        for post in self.posts:
            # Solo se recorren los tags si realmente es una lista
            if isinstance(post.tags, list):
                for t in post.tags:
                    if str(t).lower() == tag.lower():
                        resultados.append(post)
                        break
        return resultados

    def crear_post(self, titulo, contenido, autor, tags, estado="borrador"):
        """Crea un nuevo Post, lo agrega al blog y lo retorna. Lanza ValueError si hay campos vacíos."""
        if not titulo.strip():
            raise ValueError("el título no puede estar vacío")
        if not contenido.strip():
            raise ValueError("el contenido no puede estar vacío")

        # El nuevo id es el mayor id existente + 1
        mayor_id = 0
        for post in self.posts:
            if isinstance(post.id, int) and post.id > mayor_id:
                mayor_id = post.id

        nuevo = Post(mayor_id + 1, titulo.strip(), contenido.strip(), autor, tags, estado)
        self.posts.append(nuevo)
        return nuevo

    def validar_posts(self, estados_validos):
        """Valida cada post usando validar_post y muestra el resultado."""
        print("\nValidación de posts:")
        for indice, post in enumerate(self.posts, start=1):
            es_valido, mensaje = validar_post(post.to_dict(), estados_validos)
            if es_valido:
                print(f"Post {indice}: válido")
            else:
                print(f"Post {indice}: error - {mensaje}")

    def to_list(self):
        """Convierte todos los posts a una lista de diccionarios (para guardar en JSON)."""
        return [post.to_dict() for post in self.posts]