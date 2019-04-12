from django.shortcuts import render
from .models import Recipe


def recipes_list_view(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list": recipes
    }

    return render(request, 'recipes_list.html', context)


def recipe_details_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {
        "recipe": recipe
    }

    return render(request, 'recipe_details.html', context)
