from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'template_name': 'accounts/logged_out.html'}, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
]