from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kuk/', include('kuk.urls')),
    path('quack/', include('quack.urls')),
    path('', include('kek.urls')),
]
