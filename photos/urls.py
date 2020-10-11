from django.urls import path
from . import views

urlpatterns = [
    path("", views.photo_index, name="photo_index"),
    path("<int:pk>/", views.photo_details, name="photo_details"),
]