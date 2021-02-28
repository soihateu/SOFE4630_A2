from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Post
from django.views.generic.edit import FormView
from myapp.forms import Upload

""" def process(request):
    desc = request.POST['desc']
    connection = Connection('') """

class Upload(FormView):
    template_name = 'index.html'
    form_class = Upload
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        print(form.cleaned_data)
        return super().form_valid(form)
