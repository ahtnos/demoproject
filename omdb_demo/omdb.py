import requests
import json

SERIES_TEST_RESPONSE = '''
{"Title":"Stargate SG-1","Year":"1997–2007","Rated":"TV-14","Released":"27 Jul 1997","Runtime":"44 min","Genre":"Action, Adventure, Drama","Director":"N/A","Writer":"Jonathan Glassner, Brad Wright","Actors":"Amanda Tapping, Christopher Judge, Michael Shanks, Richard Dean Anderson","Plot":"A secret military team, SG-1, is formed to explore the recently discovered Stargates.","Language":"English","Country":"USA, Canada","Awards":"Nominated for 9 Primetime Emmys. Another 18 wins & 88 nominations.","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTc3MjEwMTc5N15BMl5BanBnXkFtZTcwNzQ2NjQ4NA@@._V1_SX300.jpg","Metascore":"N/A","imdbRating":"8.4","imdbVotes":"66,651","imdbID":"tt0118480","Type":"series","totalSeasons":"10","Response":"True"}
'''

OMDB_API_BASE_URL = 'http://www.omdbapi.com'

def get_series(title, year=''):
	params={'type': 'series', 'r': 'json', 't': title, 'y': year}
	#response = requests.get(OMDB_API_BASE_URL, params)
	#return response.json()
	return json.loads(SERIES_TEST_RESPONSE)


