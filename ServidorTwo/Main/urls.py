from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'main'

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('', views.IndexView, name="IndexView"),

    path('articulo/<str:url>/<int:id>', views.ArticuloView, name="ArticuloView"),
    path("all/", views.allView, name="all"),  
]
