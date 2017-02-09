from django.conf.urls import url

from . import views

app_name = 'omdb_demo'
urlpatterns = [
	url(r'^$', views.series, name='series'),
	url(r'^get_season$', views.get_season, name='get_season'),
]
