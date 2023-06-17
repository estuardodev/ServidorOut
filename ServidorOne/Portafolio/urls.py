from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.views.generic.base import TemplateView

from Main.views import AtributionView, Error404View, Error500View

app_name = 'portafolio'

urlpatterns = [
    path('estuardodev_admin_site/', admin.site.urls),
    path('', include('Main.urls')),
    path('terceros/', AtributionView.as_view()),

    path('robots.txt', TemplateView.as_view(template_name="main/robots.txt", content_type="text/plain")),
    path('sitemap.xml', TemplateView.as_view(template_name="main/sitemap.xml", content_type="text/xml")),
    path('BingSiteAuth.xml', TemplateView.as_view(template_name="main/BingSiteAuth.xml", content_type="text/xml")),
]

# Error 404
handler404 = Error404View.as_view()

# Error 500
handler500 = Error500View.as_view()