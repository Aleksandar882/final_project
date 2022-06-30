from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(null=True, blank=True)
    image=models.ImageField(upload_to="cover_images/", null=True, blank=True)

    def __str__(self):
        return self.name



class Quiz(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    CorrectAnswer = models.CharField(max_length=100)

    def __str__(self):
        return self.Question

class Badge(models.Model):
    name=models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    has_badge=models.BooleanField()