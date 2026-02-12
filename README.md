# Ejercicio con Django para bootcamp Python Full Stack de Talento Digital 


# Contexto del problema:

El bootcamp necesita una pequeña aplicación web interna para mostrar la oferta de cursos disponibles a futuros estudiantes.
Actualmente, la información se encuentra dispersa y se requiere una solución simple, clara y mantenible que permita:

- Mostrar una página de bienvenida
- Listar los cursos disponibles
- Ver el detalle de cada curso
- Mostrar información general del bootcamp

Tu tarea será desarrollar esta aplicación utilizando Django, aplicando correctamente el enrutado, las vistas y los templates,
además de integrar Bootstrap para el diseño del frontend.

# Objetivo del ejercicio

Desarrollar una mini aplicación Django que resuelva el problema planteado, demostrando comprensión de:

- Enrutado (urls.py)
- Vistas (views.py)
- Templates HTML
- Paso de contexto desde vistas a templates
- Herencia de templates
- Uso de Bootstrap para el frontend

# Requisitos técnicos

- Django 4 o superior
- Crear una app llamada 'cursos'
- No utilizar base de datos (los datos estarán en Python)
- Uso obligatorio de Bootstrap (CDN)

# Estructura

bootcamp_project/
│
├── bootcamp_project/
│   └── urls.py
│
├── cursos/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── cursos/
│           ├── base.html
│           ├── home.html
│           ├── lista_curso.html
│           ├── detalle_curso.html
│           └── about.html
│
└── manage.py


