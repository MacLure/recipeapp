from django.contrib import admin
from django.urls import path

from .views import account_view

app_name = 'accounts'


urlpatterns = [
    path('accounts/', account_view),
]
