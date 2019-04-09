from django.shortcuts import render


def recipes_list_view(request):
    return render(request, 'recipes_list.html')
