from django.urls import path
from . import views

app_name = 'eduprod'

urlpatterns = [

    path("", views.index, name="index"),
    path("create_card/", views.create_card, name="create_card"),
    path("create_subject/", views.create_subject, name="create_subject"),
    path("study_subject/<int:subject_id>/", views.study_subject, name="study_subject"),
]
