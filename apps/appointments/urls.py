from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.default),
    url(r'^add$', views.add),
    url(r'^(?P<a_id>\d+)/delete$', views.delete_task),
    url(r'^(?P<a_id>\d+)/edit$', views.show_edit),
    url(r'^(?P<a_id>\d+)/update$', views.update)
]