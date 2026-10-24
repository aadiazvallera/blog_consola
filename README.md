# Blog por consola (POO + JSON)

Sistema de blog por consola en Python, organizado en módulos y paquetes, que usa clases (Programación Orientada a Objetos) y guarda los posts en un archivo JSON.

## Cómo ejecutarlo

Desde la carpeta raíz del proyecto (la que contiene `main.py`):

```
python main.py
```

Requiere Python 3. No usa librerías externas.

## Estructura del proyecto

```
blog_consola/
├── main.py
├── README.md
├── posts.json          (se genera al guardar desde el menú)
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    └── validaciones.py
```

## Responsabilidad de cada archivo

- `main.py`: punto de entrada. Carga los posts, crea la instancia de `Blog` y conecta las opciones del menú con sus métodos.
- `blog/modelos.py`: clases `Autor`, `Post` y `Blog`.
- `blog/datos.py`: datos base y persistencia: carga y guarda los posts en `posts.json`.
- `blog/menu.py`: muestra el menú y maneja la entrada del usuario.
- `blog/validaciones.py`: reglas para validar la estructura de un post.
- `blog/__init__.py`: marca la carpeta `blog` como paquete de Python.

## Clases principales

- `Autor`: representa a la persona autora (nombre, bio, especialidad, redes sociales).
- `Post`: representa una publicación (id, título, contenido, tags, estado). Su atributo `autor` es una instancia de `Autor`.
- `Blog`: centraliza la lógica del sistema. Tiene una lista de objetos `Post` y métodos para listar, buscar por título, filtrar por tag, crear y validar posts.

## Cómo funciona la persistencia con JSON

- JSON no puede guardar objetos de Python directamente, por eso cada clase tiene un método `to_dict()` que convierte el objeto en un diccionario, y un método `from_dict()` que reconstruye el objeto a partir de un diccionario.
- Al iniciar, `cargar_posts()` lee `posts.json` y convierte cada diccionario en un objeto `Post`.
- Al elegir "Guardar posts en JSON", `guardar_posts()` convierte cada `Post` a diccionario y escribe el archivo.
- Si `posts.json` no existe, está vacío o tiene contenido inválido, el programa avisa y carga unos posts iniciales sin cerrarse. Si un elemento del JSON está incompleto, se omite con un aviso.
- Los posts nuevos se guardan solo cuando se elige la opción 6 del menú.

## Menú

1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Crear nuevo post
5. Validar posts
6. Guardar posts en JSON
7. Salir

Las búsquedas y filtros no distinguen mayúsculas de minúsculas. Entre los posts iniciales hay uno con datos incorrectos a propósito para probar la validación.

## Qué cambió respecto al checkpoint anterior

- Los autores y posts pasaron de ser diccionarios a ser objetos (`Autor` y `Post`), y el blog es una clase (`Blog`) que centraliza la lógica.
- Se agregó `blog/modelos.py` y se eliminó `blog/operaciones.py`, porque sus funciones ahora son métodos de `Blog`.
- `blog/datos.py` ahora carga y guarda los posts en `posts.json`.
- El menú tiene dos opciones nuevas: crear un post y guardar en JSON.
- `validar_post` ahora recibe los estados válidos por parámetro, para evitar imports circulares.