from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listado', views.LibroListView.as_view(), name='libros_listado'),
    path('create', views.LibroCreateView.as_view(), name='libro_crear'),
    path('detalle/<int:pk>', views.LibroDetailView.as_view(), name='libro_detalle'),
    path('modificar/<int:pk>', views.LibroUpdateView.as_view(), name='libro_update'),
    path('borrar/<int:pk>', views.LibroDeleteView.as_view(), name='libro_borrar'),
]