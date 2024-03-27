from django.db import models
from django.contrib.auth.models import User

class Flashcard(models.Model):
    question = models.CharField(max_length=255, default='')
    answer = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='flashcard_images', blank=True, null=True)
    subject = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)