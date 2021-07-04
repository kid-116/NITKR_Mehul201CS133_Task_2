from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'blogs'

urlpatterns = [
    url('create/', views.create, name='create_path'),
    url('index/', views.index, name='index_path'),
    path('<int:id_b>/read/', views.read, name='read_path'),
    path('<int:id_b>/update/', views.update, name='update_path'),
    path('<int:id_b>/delete/', views.delete, name='delete_path'),
    path('<int:id_b>/upvote/', views.upvote, name='upvote_path'),
    path('<int:id_b>/downvote/', views.downvote, name='downvote_path'),
]