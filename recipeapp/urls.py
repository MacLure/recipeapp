from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from recipeapp import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('admin/', admin.site.urls),
    path('recipes/', include('recipes.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
