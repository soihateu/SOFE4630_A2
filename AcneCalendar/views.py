from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):
    return render(request, 'index.html', {})

def submitForm(request):
    dateInput = request.POST.get('date')
    imageInput = request.POST.get('image')
    descInput = request.POST.get('desc')

    print("date: ", dateInput)
    print("desc: ", descInput)
    print("image: ", imageInput)
    
    responseData = {}
    
    #form = Form(request.POST)
    #form.save()
    
    responseData['result'] = "Form submit successful!"
    
    return HttpResponse(json.dumps(responseData), content_type="application/json")
