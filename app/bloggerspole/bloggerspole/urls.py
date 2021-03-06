from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blogs/comments/', include('comments.urls')),
    path('blogs/', include('blogs.urls')),
    url('', views.landing, name='landing_path'),
]