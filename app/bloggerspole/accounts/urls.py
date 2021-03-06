from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url('signup/', views.signup_account, name='signup_path'),
    url('login/', views.login_account, name='login_path'),
    url('logout/', views.logout_account, name='logout_path'),
]