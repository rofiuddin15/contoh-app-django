from django import forms

CHOICES =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
)

class BeritaForm(forms.Form):
    judul = forms.CharField(help_text='tulis judul disini', max_length=100)
    konten = forms.CharField(max_length=100)