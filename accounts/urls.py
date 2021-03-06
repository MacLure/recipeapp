from django.contrib import admin
from django.urls import path
from . import views

from .views import (
    account_view,
    signup_view,
    login_view,
    logout_view
)

app_name = 'accounts'


urlpatterns = [
    path('account/', account_view),
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),


]
