from django.db import models

# Create your models here.
class MataKuliah(models.Model):  
    nama = models.CharField(max_length=250)
    dosen = models.CharField(max_length=250)
    sks = models.IntegerField()
    deskripsi = models.TextField()
    semester = models.CharField(max_length=9)
    tahun_ajar = models.CharField(max_length=250)

class Tugas(models.Model):
    name = models.CharField(max_length=250, default='none')
    deadline = models.DateField()
    mataKuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE, default='none', null=True, blank=True)

    class Meta:
        ordering = ['name']
