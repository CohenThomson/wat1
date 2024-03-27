from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100, default="Default Subject")  # Add default parameter here
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Flashcard(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    image = models.ImageField(upload_to='flashcard_images', blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

#class Card(models.Model):
    #question = models.CharField(max_length=255)
    #answer = models.CharField(max_length=255)
    #image = models.ImageField(upload_to='flashcard_images', blank=True, null=True)
    #subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
   # user = models.ForeignKey(User, on_delete=models.CASCADE)
