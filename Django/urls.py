
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webexample/', include('webexample.urls')),
    path('mainshablon/', include('mainshablon.urls')),
    path('', include('emmet.urls')),
]
