from django.urls import path
from memetrivia import views

urlpatterns = [
    path("", views.trivia_index, name="trivia_index"),
]
