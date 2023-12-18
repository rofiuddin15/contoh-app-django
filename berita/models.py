from django.db import models

# Create your models here.
class Berita(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.CharField(max_length=100)