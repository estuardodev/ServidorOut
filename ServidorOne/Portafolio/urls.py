from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500

from Main.views import AtributionView, Error404View, Error500View

app_name = 'portafolio'

urlpatterns = [
    path('estuardodev_admin_site/', admin.site.urls),
    path('', include('Main.urls')),
    path('terceros/', AtributionView.as_view()),
]

# Error 404
handler404 = Error404View.as_view()

# Error 500
handler500 = Error500View.as_view()