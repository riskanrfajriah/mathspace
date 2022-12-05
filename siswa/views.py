from django.shortcuts import render
from siswa.models import datasiswa
from siswa.forms import FormSiswa

# Create your views here.
def registsiswa(request):
    form = FormSiswa()

    konteks = {
        'form': form,
    }

    return render(request, 'registsiswa.html', konteks)