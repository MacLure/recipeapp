from django.contrib import admin
from django.urls import path

from .views import recipes_list_view

app_name = 'recipes'

urlpatterns = [
    path('', recipes_list_view),
]
