from django.conf.urls import url
from TaskManage import views

urlpatterns = [
    url(r'^place/$', views.place_list, name='place_list'),
    url(r'^place/add/$', views.place_edit, name='place_add'),
    url(r'^place/edit/(?P<place_id>\d+)/$', views.place_edit, name='place_edit'),
    url(r'^place/(?P<place_id>\d+)/$', views.place_detail.as_view(), name='place_detail'),
    url(r'^place/del/(?P<place_id>\d+)/$', views.place_del, name="place_del"),
    url(r'^task/(?P<place_id>\d+)/add/$', views.task_edit, name='task_add'),
    url(r'^task/edit/(?P<place_id>\d+)/(?P<task_id>\d+)/$', views.task_edit, name='task_edit'),
    url(r'^task/del/(?P<place_id>\d+)/(?P<task_id>\d+)/$', views.task_del, name='task_del'),
]