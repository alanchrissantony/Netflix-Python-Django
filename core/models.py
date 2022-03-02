from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


AGE_CHOICES=(
    ('All', 'All'),
    ('Kids', 'Kids')
)

MOVIE_CHOICES=(
    ('seasonal', 'Seasonal'),
    ('single', 'Single')
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True)


class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4)

    def __str__ (self):
        return self.name


class PopularMovie(models.Model):
    title=models.CharField(max_length=225)
    description:str=models.TextField()
    content:str=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4)
    type=models.CharField(max_length=10, choices=MOVIE_CHOICES)
    videos=models.TextField()
    image=models.ImageField(upload_to='image')
    flyer=models.ImageField(upload_to='flyers')
    age_limit=models.CharField(max_length=10, choices=AGE_CHOICES)

    def __str__ (self):
        return self.title


class Movie(models.Model):
    title=models.CharField(max_length=225)
    description:str=models.TextField()
    content:str=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4)
    type=models.CharField(max_length=10, choices=MOVIE_CHOICES)
    videos=models.TextField()
    image=models.ImageField(upload_to='image')
    flyer=models.ImageField(upload_to='flyers')
    age_limit=models.CharField(max_length=10, choices=AGE_CHOICES)

    def __str__ (self):
        return self.title
