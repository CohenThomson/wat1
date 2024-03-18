from django.core import serializers
from django.shortcuts import render
from .models import Card

from django.views.generic import (
    ListView,
)

from .models import Card

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")

#this code sets up a view (CardListView) that will render a list of Card objects from the database, ordered first by the "box" attribute and then by the "date_created" attribute. 
#This view can be used to display a list of flashcards or any other content associated with the Card model.