import requests
import json

SG1_SERIES_RESPONSE = '''
{"Title":"Stargate SG-1","Year":"1997–2007","Rated":"TV-14","Released":"27 Jul 1997","Runtime":"44 min","Genre":"Action, Adventure, Drama","Director":"N/A","Writer":"Jonathan Glassner, Brad Wright","Actors":"Amanda Tapping, Christopher Judge, Michael Shanks, Richard Dean Anderson","Plot":"General Hammond summons Colonel Jack O'Neill out of retirement to embark on a secret rescue mission. O'Neill confesses that he disobeyed orders to destroy the Stargate on Planet Abydos, and that scientist Daniel Jackson may still be alive. Arriving on Abydos with his team, O'Neill meets up once again with the scientist, who has discovered a giant elaborate cartouche in hieroglyphics. All signs point to the fact that this is a map of many Stargates that exist throughout the galaxy - a development that makes the dream of the SG-1 team to travel throughout the universe in time a reality.","Language":"English","Country":"USA, Canada","Awards":"Nominated for 9 Primetime Emmys. Another 18 wins & 88 nominations.","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTc3MjEwMTc5N15BMl5BanBnXkFtZTcwNzQ2NjQ4NA@@._V1_SX300.jpg","Metascore":"N/A","imdbRating":"8.4","imdbVotes":"66,651","imdbID":"tt0118480","Type":"series","totalSeasons":"10","Response":"True"}'''

SG1_SEASON_1_RESPONSE='''
{"Title":"Stargate SG-1","Season":"1","totalSeasons":"10","Episodes":[{"Title":"Children of the Gods","Released":"1997-07-27","Episode":"1","imdbRating":"8.3","imdbID":"tt0234794"},{"Title":"The Enemy Within","Released":"1997-08-01","Episode":"2","imdbRating":"7.7","imdbID":"tt0709185"},{"Title":"Emancipation","Released":"1997-08-08","Episode":"3","imdbRating":"6.2","imdbID":"tt0709075"},{"Title":"The Broca Divide","Released":"1997-08-15","Episode":"4","imdbRating":"7.2","imdbID":"tt0709181"},{"Title":"The First Commandment","Released":"1997-08-22","Episode":"5","imdbRating":"6.8","imdbID":"tt0709188"},{"Title":"Cold Lazarus","Released":"1997-08-29","Episode":"6","imdbRating":"7.6","imdbID":"tt0709059"},{"Title":"The Nox","Released":"1997-09-12","Episode":"7","imdbRating":"8.2","imdbID":"tt0709194"},{"Title":"Brief Candle","Released":"1997-09-19","Episode":"8","imdbRating":"7.5","imdbID":"tt0709052"},{"Title":"Thor's Hammer","Released":"1997-09-26","Episode":"9","imdbRating":"8.2","imdbID":"tt0709209"},{"Title":"The Torment of Tantalus","Released":"1997-10-03","Episode":"10","imdbRating":"8.4","imdbID":"tt0709205"},{"Title":"Bloodlines","Released":"1997-10-10","Episode":"11","imdbRating":"7.4","imdbID":"tt0709051"},{"Title":"Fire and Water","Released":"1997-10-17","Episode":"12","imdbRating":"7.2","imdbID":"tt0709091"},{"Title":"Hathor","Released":"1997-10-24","Episode":"13","imdbRating":"7.6","imdbID":"tt0709101"},{"Title":"Singularity","Released":"1997-10-31","Episode":"14","imdbRating":"7.8","imdbID":"tt0709172"},{"Title":"Cor-ai","Released":"1998-01-23","Episode":"15","imdbRating":"7.3","imdbID":"tt0709061"},{"Title":"Enigma","Released":"1998-01-30","Episode":"16","imdbRating":"8.2","imdbID":"tt0709079"},{"Title":"Solitudes","Released":"1998-02-06","Episode":"17","imdbRating":"8.3","imdbID":"tt0709175"},{"Title":"Tin Man","Released":"1998-02-13","Episode":"18","imdbRating":"7.8","imdbID":"tt0709212"},{"Title":"There But for the Grace of God","Released":"1998-02-20","Episode":"19","imdbRating":"8.7","imdbID":"tt0709207"},{"Title":"Politics","Released":"1998-02-27","Episode":"20","imdbRating":"6.3","imdbID":"tt0709142"},{"Title":"Within the Serpent's Grasp","Released":"1998-03-06","Episode":"21","imdbRating":"8.6","imdbID":"tt0709219"}],"Response":"True"}'''

SG1_SEASON_2_RESPONSE='''
{"Title":"Stargate SG-1","Season":"2","totalSeasons":"10","Episodes":[{"Title":"The Serpent's Lair","Released":"1998-06-26","Episode":"1","imdbRating":"8.8","imdbID":"tt0709199"},{"Title":"In the Line of Duty","Released":"1998-07-03","Episode":"2","imdbRating":"8.0","imdbID":"tt0709107"},{"Title":"Prisoners","Released":"1998-07-10","Episode":"3","imdbRating":"7.4","imdbID":"tt0709144"},{"Title":"The Gamekeeper","Released":"1998-07-17","Episode":"4","imdbRating":"7.3","imdbID":"tt0709192"},{"Title":"Need","Released":"1998-07-24","Episode":"5","imdbRating":"6.9","imdbID":"tt0709127"},{"Title":"Thor's Chariot","Released":"1998-07-31","Episode":"6","imdbRating":"8.5","imdbID":"tt0709208"},{"Title":"Message in a Bottle","Released":"1998-08-07","Episode":"7","imdbRating":"7.5","imdbID":"tt0709123"},{"Title":"Family","Released":"1998-08-14","Episode":"8","imdbRating":"6.9","imdbID":"tt0709090"},{"Title":"Secrets","Released":"1998-08-21","Episode":"9","imdbRating":"7.9","imdbID":"tt0709164"},{"Title":"Bane","Released":"1998-09-25","Episode":"10","imdbRating":"7.2","imdbID":"tt0709045"},{"Title":"The Tok'ra: Part 1","Released":"1998-10-02","Episode":"11","imdbRating":"8.1","imdbID":"tt0709202"},{"Title":"The Tok'ra: Part 2","Released":"1998-10-11","Episode":"12","imdbRating":"8.3","imdbID":"tt0709203"},{"Title":"Spirits","Released":"1998-10-23","Episode":"13","imdbRating":"7.4","imdbID":"tt0709177"},{"Title":"Touchstone","Released":"1998-10-30","Episode":"14","imdbRating":"7.7","imdbID":"tt0709213"},{"Title":"The Fifth Race","Released":"1999-01-22","Episode":"15","imdbRating":"9.1","imdbID":"tt0709187"},{"Title":"A Matter of Time","Released":"1999-01-29","Episode":"16","imdbRating":"8.7","imdbID":"tt0709033"},{"Title":"Holiday","Released":"1999-02-05","Episode":"17","imdbRating":"7.6","imdbID":"tt0709104"},{"Title":"Serpent's Song","Released":"1999-02-12","Episode":"18","imdbRating":"7.9","imdbID":"tt0709166"},{"Title":"One False Step","Released":"1999-02-19","Episode":"19","imdbRating":"6.9","imdbID":"tt0709134"},{"Title":"Show and Tell","Released":"1999-02-26","Episode":"20","imdbRating":"7.7","imdbID":"tt0709170"},{"Title":"1969","Released":"1999-03-05","Episode":"21","imdbRating":"8.7","imdbID":"tt0709028"},{"Title":"Out of Mind","Released":"1999-03-12","Episode":"22","imdbRating":"7.4","imdbID":"tt0709137"}],"Response":"True"}'''


OMDB_API_BASE_URL = 'http://www.omdbapi.com'

def get_series(title):
	if title == 'Stargate SG-1':
		return json.loads(SG1_SERIES_RESPONSE)
	params={'r': 'json', 'type': 'series', 't': title, 'plot': 'full'}
	response = requests.get(OMDB_API_BASE_URL, params)
	if response.status_code != 200 or response.json()['Response'] == 'False':
		return None
	return response.json()

def get_season(series_imdb_id, number):
	if series_imdb_id == 'tt0118480':
		if number == 1:
			return json.loads(SG1_SEASON_1_RESPONSE)
		elif number == 2:
			return json.loads(SG1_SEASON_2_RESPONSE)
	params={'i': series_imdb_id, 'season': str(number)}
	response = requests.get(OMDB_API_BASE_URL, params)
	return response.json()

