from django.contrib import admin
from django.urls import path

from .views import recipes_list_view
from .views import recipe_details_view

app_name = 'recipes'

urlpatterns = [
    path('', recipes_list_view),
    path('<int:recipe_id>/', recipe_details_view, name="recipe")
]
