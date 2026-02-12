from django.shortcuts import render

# --- Datos de los cursos (sin base de datos, todo en Python) ---

CURSOS = [
    {
        'id': 1,
        'nombre': 'Desarrollo Web Full Stack',
        'descripcion': 'Aprende HTML, CSS, JavaScript y React desde cero.',
        'duracion': '12 semanas',
        'nivel': 'Principiante',
        'precio': '$1.500.000 CLP',
        'temario': [
            'HTML5 y CSS3',
            'JavaScript',
            'React.js',
            'Node.js',
        ],
    },
    {
        'id': 2,
        'nombre': 'Python y Django',
        'descripcion': 'Crea aplicaciones web con Python y Django.',
        'duracion': '10 semanas',
        'nivel': 'Intermedio',
        'precio': '$1.200.000 CLP',
        'temario': [
            'Fundamentos de Python',
            'Programacion orientada a objetos',
            'Django Framework',
            'Django REST Framework',
        ],
    },
    {
        'id': 3,
        'nombre': 'Data Science con Python',
        'descripcion': 'Analiza datos y crea modelos de machine learning.',
        'duracion': '14 semanas',
        'nivel': 'Intermedio',
        'precio': '$1.800.000 CLP',
        'temario': [
            'NumPy y Pandas',
            'Visualizacion de datos',
            'Machine Learning',
            'Proyectos con datos reales',
        ],
    },
]


# --- Funciones para las vistas---

def home(request):
    """Pagina de bienvenida."""
    return render(request, 'cursos/home.html', {
        'total_cursos': len(CURSOS),
    })


def lista_cursos(request):
    """Listado de todos los cursos."""
    return render(request, 'cursos/lista_curso.html', {
        'cursos': CURSOS,
    })


def detalle_curso(request, curso_id):
    """Detalle de un curso especifico."""
    curso = None
    for c in CURSOS:
        if c['id'] == curso_id:
            curso = c
            break

    return render(request, 'cursos/detalle_curso.html', {
        'curso': curso,
    })


def about(request):
    """Informacion sobre el bootcamp."""
    return render(request, 'cursos/about.html')
