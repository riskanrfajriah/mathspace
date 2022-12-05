from django.shortcuts import render
from siswa.models import datasiswa
from siswa.forms import FormSiswa

# Create your views here.
def loginsiswa(request):
    form = FormSiswa()

    konteks = {
        'form': form,
    }

    return render(request, 'loginsiswa.html', konteks)