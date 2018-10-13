from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('Hostel_Inmates.urls')),
    url(r'api-auth/', include('rest_framework.urls')),
]