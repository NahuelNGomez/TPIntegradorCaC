from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'app_integrador/index.html', {})


# class LibroListView(ListView):
#     pass

# class LibroCreateView(CreateView):
#     pass

# class LibroDetailView(DetailView):
#     pass

# class LibroDeleteView(DeleteView):
#     pass

# class LibroUpdateView():
#     pass