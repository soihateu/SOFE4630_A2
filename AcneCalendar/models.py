from django.db import models

def user_directory_path(instance, filename):
    return '{0}'.format(filename)

class AcneModel(models.Model):
    class Meta:
        app_label = 'AcneCalendar.models'

    email = models.EmailField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to=user_directory_path)
    desc = models.TextField(max_length=1028)

    def __str__(self):
        return self.date
