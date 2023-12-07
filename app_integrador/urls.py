from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('libros/', views.LibroListView.as_view(), name='libros'),
    # path('libros/create/', views.LibroCreateView.as_view(), name='libro_create'),
    # path('libros/<int:pk>/', views.LibroDetailView.as_view(), name='libro_detail'),
    # path('libros/<int:pk>/delete/', views.LibroDeleteView.as_view(), name='libro_delete'),
    # path('libros/<int:pk>/update/', views.LibroUpdateView.as_view(), name='libro_update'),
]