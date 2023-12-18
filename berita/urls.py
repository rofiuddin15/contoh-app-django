from django.urls import path
from .views import berita_view

urlpatterns = [
    path('berita', berita_view, name='berita')
]
