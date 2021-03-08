from django import forms
from .models import MataKuliah, Tugas

import datetime

TAHUN_CHOICES = []
for i in range((datetime.datetime.now().year), 2002, -1):
    TAHUN_CHOICES.append((str(i) +'/'+str(i+1), str(i) +'/'+str(i+1)))

SEMESTER_CHOICES = [('Genap','Genap'), ('Ganjil', 'Ganjil')]

class MataKuliah_Form(forms.ModelForm):
    class Meta:
        model = MataKuliah
        fields = ['nama', 'dosen', 'sks', 'deskripsi', 'semester', 'tahun_ajar']

    nama = forms.CharField(label='Nama Mata Kuliah', label_suffix="", required=True, max_length=250)
    dosen = forms.CharField(label='Dosen', label_suffix="", required=True, max_length=250)
    sks = forms.IntegerField(label='Jumlah SKS', label_suffix="", required=True)
    deskripsi = forms.CharField(label='Deskripsi', label_suffix="", required=True, widget=forms.Textarea(attrs={'type':'text', 'style':'width:75%'}))
    semester = forms.CharField(label='Semester', label_suffix="", required=True, widget=forms.Select(choices=SEMESTER_CHOICES))
    tahun_ajar = forms.CharField(label='Tahun Ajar', label_suffix="", required=True, widget=forms.Select(choices=TAHUN_CHOICES))

class Tugas_Form(forms.ModelForm):
    class Meta:
        model = Tugas
        fields = ['name', 'deadline']

    name = forms.CharField(label='Nama Tugas', label_suffix="", required=True, max_length=250)
    deadline = forms.DateField(label='Deadline', label_suffix="", required=True, widget=forms.DateInput(attrs={'type': 'date'}))
