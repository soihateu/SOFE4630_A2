from django.shortcuts import render
from django.http import HttpResponse
from .forms import AcneForm
import requests
from django.core.mail import send_mail
from AcneTracker.settings import EMAIL_HOST_USER

def index(request):
    # Weather
    url = "http://api.openweathermap.org/data/2.5/weather?q=Oshawa&appid=d00cc69b87932b4a5d38f466031643c7"
    oshawaWeather = requests.get(url.format("Oshawa")).json()
    humidity = oshawaWeather["main"]["humidity"]

    # Form
    form = AcneForm(request.POST, request.FILES)
    
    if form.is_valid():
        form.save()
        print("form saved successfully")
        # Send e-mail
        subject = "New entry to Acne Tracker calendar"
        message = "A new entry has been submitted for " + form['date'].value() + "\n\n"
        message += "Your description is as follows:\n"
        message += form['desc'].value()
        recipient = form['email'].value()
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently = False)
    else:
        print(form.errors)

    return render(request, 'index.html', {'form': form, 'humidity': humidity})
