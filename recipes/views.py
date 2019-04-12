from django.shortcuts import render
from .models import Recipe


def recipes_list_view(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list": recipes
    }

    return render(request, 'recipes_list.html', context)
