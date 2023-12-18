from django import forms

class BeritaForm(forms.Form):
    judul = forms.CharField(help_text='tulis judul disini', max_length=100)
    konten = forms.CharField(max_length=100)