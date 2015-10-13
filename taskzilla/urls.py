from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^tasks/(?P<task_id>[0-9]+)/$', views.task_page, name='task_page'),
	url(r'^login/$', views.login_page, name='login_page'),
	url(r'^logout/$', views.logout_page, name='logout_page'),
	url(r'^subscribe/(?P<task_id>[0-9]+)/$', views.subscribe, name='subscribe'),
	url(r'^unsubscribe/(?P<task_id>[0-9]+)/$', views.unsubscribe, name='subscribe'),
]
