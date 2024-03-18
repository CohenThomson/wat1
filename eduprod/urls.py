from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.CardListView.as_view(),
        name="card_list"
    ),
]

#this code sets up a URL pattern that maps requests with an empty path to the CardListView class-based view, allowing users to access a list of cards. The 