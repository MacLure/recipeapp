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
