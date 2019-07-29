from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url('admin/', admin.site.urls),
    url('api-auth/', include('rest_framework.urls')),
    url('api/', include('parlamento.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
