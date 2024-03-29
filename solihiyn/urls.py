from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .schema import swagger_patterns
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/logout/', LogoutView.as_view(), name='logout'),
    path('api/v1/', include('apps.zikrs.urls')),
    path('api/v1/', include('apps.accounts.urls')),
]

urlpatterns += swagger_patterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
