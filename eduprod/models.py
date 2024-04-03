from django.db import models
from django.contrib.auth.models import User
#Imports necessary modules for Django models and User authentication.

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)
#Sets up the number of boxes for organizing flashcards.

class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
#Declares a Django model called Card representing flashcards. Fields: question: Stores the question on the flashcard. answer: Stores the answer to the question. box: Represents the box number where the card belongs. date_created: Stores the creation date of the flashcard. 
# Methods: __str__(): Specifies how instances of the model should be represented as strings, returning the question.