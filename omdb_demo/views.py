import json

from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render

from . import omdb

def series(request):
	title = request.GET.get('title')
	if not title:
		return render(request, 'omdb_demo/index.html', {})
	series = omdb.get_series(title=title)
	if series:
		series['detail_items'] = []
		details = [
			('Actors', series.get('Actors', '')),
			('IMDb Rating', series.get('imdbRating', '')),
			('Metascore', series.get('Metascore', '')),
			('Running years', series.get('Year', '')),
			('Genre', series.get('Genre', '')),
			('Rated', series.get('Rated', ''))
			]
		for detail_header, detail_value in details:
			series['detail_items'].append({'header': detail_header, 'value': detail_value })
		series['season_range'] = range(1, 1+int(series['totalSeasons']))
	context = {'series': series}
	#return HttpResponse(str(series))
	return render(request, 'omdb_demo/index.html', context)

def get_season(request):
	series_imdb_id=request.GET.get('series_imdb_id')
	number=request.GET.get('number')
	json_string = json.dumps(omdb.get_season(series_imdb_id=series_imdb_id, number=number))
	return HttpResponse(json_string)
