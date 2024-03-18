from django.db import models

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

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
#This code provides the data structure for storing flashcards in the web app's database. 
#Each Card instance represents a single flashcard with a question, answer, box number, and creation date.