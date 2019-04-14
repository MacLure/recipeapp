from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import NewRecipeForm
from django.contrib.auth.decorators import login_required


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


@login_required(login_url="/accounts/login/")
def recipe_create_view(request):
    form = NewRecipeForm()
    if request.method == "POST":
        form = NewRecipeForm(request.POST)
        if form.is_valid():
            Recipe.objects.create(**form.cleaned_data)
            return redirect('recipes:list')

        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, 'recipe_create.html', context)
