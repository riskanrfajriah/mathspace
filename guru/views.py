from django.shortcuts import render
from guru.models import dataguru
from guru.forms import FormGuru

# Create your views here.
def loginguru(request):
    form = FormGuru()

    konteks = {
        'form': form,
    }

    return render(request, 'loginguru.html', konteks)