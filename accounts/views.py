from django.shortcuts import render
from django.http import HttpResponse


def account_view(request):
    return HttpResponse("account")
