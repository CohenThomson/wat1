from django.urls import path
from . import views

app_name = 'eduprod'

urlpatterns = [
    path('', views.CardListView.as_view(), name='card-list'),
    path('create/', views.CardCreateView.as_view(), name='card-create'),
    path('update/<int:pk>/', views.CardUpdateView.as_view(), name='card-update'),
    path('delete/<int:pk>/', views.CardDeleteView.as_view(), name='card-delete'),
    path("box/<int:box_num>", views.BoxView.as_view(), name="box"), 
]
