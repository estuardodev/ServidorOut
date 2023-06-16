from django.contrib import admin
from django.urls import path, include

app_name = 'portafolio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Main.urls'))
]
