from django.contrib import admin
from django.urls import path, include # added include for including app URLs - L.Llanto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),  # connect posts app URLs L.Llanto
]
