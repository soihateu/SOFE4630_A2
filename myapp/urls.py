from django.urls import path
from myapp.views import Upload

urlpatterns = [
    path('', Upload.as_view(), name='upload'),
]
