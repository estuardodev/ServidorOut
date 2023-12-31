from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

from django.contrib.sitemaps.views import sitemap
from .sitemaps import MapaDeSitio

sitemaps = {
    'blog': MapaDeSitio
}


app_name = 'main'

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('', views.IndexView, name="IndexView"),
    path('articulo/<str:url>/<int:id>', views.ArticuloView, name="ArticuloView"),
    path("all/", views.allView, name="all"),  
    path('feed/', views.RssView.as_view(), name='ultimas_noticias_feed'),
    path('ads.txt', TemplateView.as_view(template_name="ads.txt", content_type="text/plain")),
    path('app-ads.txt', TemplateView.as_view(template_name="app-ads.txt", content_type="text/plain")),
    path('BingSiteAuth.xml', TemplateView.as_view(template_name="BingSiteAuth.xml", content_type="text/xml")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
