from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blogs/comments/', include('comments.urls')),
    path('blogs/', include('blogs.urls')),
    url('', views.landing, name='landing_path'),
]
