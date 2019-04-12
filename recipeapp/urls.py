from django.contrib import admin
from django.urls import include, path

from recipeapp import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('admin/', admin.site.urls),
    path('recipes/', include('recipes.urls')),
    path('accounts/', include('accounts.urls')),
]
