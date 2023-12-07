from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Libro
from django.urls import reverse, reverse_lazy

def index(request):
    return render(request, 'app_integrador/index.html', {})


class LibroListView(ListView):
    model = Libro
    context_object_name = 'listado_libros'
    template_name = 'app_integrador/libros_listado.html'

class LibroCreateView(CreateView):
    model = Libro
    template_name = 'app_integrador/libro_crear.html'
    success_url = 'listado'
    fields = '__all__'


class LibroDetailView(DetailView):
    model = Libro
    template_name = 'app_integrador/libro_detalle.html'
    context_object_name = 'libro'

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'app_integrador/libro_borrar.html'
    success_url = reverse_lazy('libros_listado')

class LibroUpdateView(UpdateView):
    model = Libro
    template_name = 'app_integrador/libro_update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('libro_detalle', kwargs={'pk': self.object.pk})