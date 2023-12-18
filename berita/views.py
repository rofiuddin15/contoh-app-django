from django.shortcuts import render
from .forms import BeritaForm

# Create your views here.
def berita_view(request):
    context = {
        'form': BeritaForm()
    }
    return render(request, 'form-berita.html', context)