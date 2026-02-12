from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.home, name='home'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('about/', views.about, name='about'),
]
