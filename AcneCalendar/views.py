from django.shortcuts import render
from django.http import HttpResponse
from .forms import AcneForm

def index(request):
    form = AcneForm(request.POST, request.FILES)
    
    if form.is_valid():
        form.save()
        print("form success")
    else:
        print("form invalid")
        print(form.errors)

    return render(request, 'index.html', {'form': form})
