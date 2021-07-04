from django.conf.urls import url
from django.urls.conf import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('<int:id_b>/create/', views.create, name='create_path'),
    path('<int:id_c>/delete', views.delete, name='delete_path'),
]
