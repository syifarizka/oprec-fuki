from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import MataKuliah, Tugas
from .forms import MataKuliah_Form, Tugas_Form


# Landing page
def home(request):
    matkul = MataKuliah.objects.all()
    tugas = Tugas.objects.all()
    response = {'matkul' : matkul, 'tugas' : tugas, 'MataKuliah_Form' : MataKuliah_Form, 'Tugas_Form' : Tugas_Form}
    return render(request, 'main/home.html', response)

# save isi form mata kuliah
def savematkul(request):
    form = MataKuliah_Form(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/')
    else:
        form = MataKuliah_Form() 
        return render(request,'main/home.html')

#save isi form tugas
def savetugas(request, pk):
    form = Tugas_Form(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        matkul = get_object_or_404(MataKuliah, pk=pk)           # ambil object mata kuliah dari primary keynya
        new_tugas = Tugas()
        new_tugas.name = form.cleaned_data['name']
        new_tugas.deadline = form.cleaned_data['deadline']
        new_tugas.mataKuliah = matkul
        new_tugas.save()
        return HttpResponseRedirect('/')
    else:
        form = Tugas_Form()
        return render(request,'main/home.html')


