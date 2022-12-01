from django.urls import path
from AppFinal import views

urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('reserva/', views.reserva,name='reserva'),
    path('reservaApi/', views.reservaApi),
    path('contactoApi/', views.contactoApi),
    path('trabajoApi/', views.trabajoApi),
    path('pagina3/', views.pagina3),
    path('busquedaReserva/', views.buscarreserva,name='buscarreserva'),
    path('buscar/', views.buscar,),
    path('contacto/', views.contacto,name='contacto'),
    path('trabajo/', views.trabajo,name='trabajo'),
]
