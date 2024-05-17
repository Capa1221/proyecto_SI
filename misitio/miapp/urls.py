from django.urls import path
from . import views

urlpatterns = [
    path('', views.saludo),
    path("consulta/", views.consulta),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('task/<int:id>', views.tasks),
    path('about/', views.about)
]
