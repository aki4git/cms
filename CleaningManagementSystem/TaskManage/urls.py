from django.conf.urls import url
from TaskManage import views

urlpatterns = [
    url(r'^place/$', views.place_list, name='place_list'),
    url(r'^place/(?P<place_id>\d+)/$', views.place_detail.as_view(), name='place_detail'),
]