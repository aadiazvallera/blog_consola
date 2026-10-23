# Blog por consola

Sistema de blog por consola en Python, organizado en módulos y paquetes. Permite ver posts, buscarlos por título, filtrarlos por tag y validar su estructura.

## Cómo ejecutarlo

Desde la carpeta origen del proyecto (la que contiene `main.py`):


## Estructura del proyecto


blog_consola/
├── main.py
├── README.md
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py


## Responsabilidad de cada archivo

- 'main.py': archivo principal que se ejecuta. Muestra el menú y llama a las funciones según la opción elegida.
- 'blog/__init__.py': marca la carpeta 'blog' como paquete de Python.
- 'blog/datos.py': datos base ('perfil_autor', 'estados_post','etiquetas_blog', 'posts').
- 'blog/menu.py': muestra el menú y maneja la entrada del usuario.
- 'blog/operaciones.py': listar, buscar por título y filtrar por tag.
- 'blog/validaciones.py': reglas para validar la estructura de un post.

## Menú

1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Validar posts
5. Salir

Las búsquedas y filtros no distinguen mayúsculas de minúsculas. El post 4 tiene datos incorrectos a propósito para probar la validación.