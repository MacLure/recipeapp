from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Recipe
from .forms import NewRecipeForm


def recipes_list_view(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list": recipes
    }

    return render(request, 'recipes_list.html', context)


def recipe_details_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe = Recipe.objects.get(id=recipe_id)
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404
    context = {
        "recipe": recipe
    }

    return render(request, 'recipe_details.html', context)


def recipe_create_view(request):
    form = NewRecipeForm()
    context = {
        "form": form
    }
    return render(request, 'recipe_create.html', context)
