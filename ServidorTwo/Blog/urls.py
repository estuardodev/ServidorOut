from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from Main import views

urlpatterns = [
    path('estuardodev_admin_site/', admin.site.urls),
    path('', include('Main.urls'))
]


# Error 404
handler404 = views.Error404View.as_view()

# Error 500
handler500 = views.Error500View.as_view()