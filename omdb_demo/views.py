#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render

from . import omdb

def index(request):
	series = omdb.get_series(title='Stargate SG-1', year='1997')
	context = {'series': series}
	return render(request, 'omdb_demo/index.html', context)
