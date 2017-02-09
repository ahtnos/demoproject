from django.conf.urls import url

from . import views

app_name = 'omdb_demo'
urlpatterns = [
	url(r'^$', views.index, name='index'),
]
