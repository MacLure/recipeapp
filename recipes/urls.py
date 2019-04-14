from django.contrib import admin
from django.urls import path

from .views import (
    recipes_list_view,
    recipe_details_view,
    recipe_create_view,
)

app_name = 'recipes'

urlpatterns = [
    path('', recipes_list_view, name="list"),
    path('<int:recipe_id>/', recipe_details_view, name="recipe"),
    path('new/', recipe_create_view, name="recipe_create")

]
