from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('estuardodev_admin_site/', admin.site.urls),
    path('', include('Main.urls'))
]
