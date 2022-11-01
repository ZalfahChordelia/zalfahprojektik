from django.shortcuts import render
from faperta.models import DOSEN
from faperta.models import MAHASISWA
from faperta.models import STAF
from faperta.forms import FormDOSEN
from faperta.forms import FormMAHASISWA
from faperta.forms import FormSTAF

# Create your views here.
def prodi5(request):
    return render(request, 'indexfp.html')

def tambah_dosen(request):
    form = FormDOSEN()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah-dosen.html', konteks)

def tambah_mahasiswa(request):
    form = FormMAHASISWA()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah-mahasiswa.html', konteks)

def tambah_staf(request):
    form = FormSTAF()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah-staf.html', konteks)