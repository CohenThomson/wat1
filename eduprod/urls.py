from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("create_card", views.create_card, name="create_card"),
    # path("", views. , name=""),
]
