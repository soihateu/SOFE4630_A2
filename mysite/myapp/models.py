from django.db import models

def user_directory_path(instance, filename):
    return '{0}'.format(filename)

class Post(models.Model):
    desc = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.date
