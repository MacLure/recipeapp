from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from recipeapp import views
from recipes import views as recipe_views

urlpatterns = [
    path('', recipe_views.recipes_list_view, name="home"),
    path('admin/', admin.site.urls),
    path('recipes/', include('recipes.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
