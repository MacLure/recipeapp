from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def account_view(request):
    return HttpResponse("account")


def signup_view(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log user in
            return redirect('recipes:list')
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})


# def recipe_create_view(request):
#     form = NewRecipeForm()
#     if request.method == "POST":
#         form = NewRecipeForm(request.POST)
#         if form.is_valid():
#             Recipe.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         "form": form
#     }
#     return render(request, 'recipe_create.html', context)
