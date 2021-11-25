# -*- coding: utf-8 -*-
"""
	Thor Add-on
"""

from sys import argv, exit as sysexit
try: #Py2
	from urllib import quote_plus
except ImportError:  #Py3
	from urllib.parse import quote_plus
from resources.lib.modules import control
from resources.lib.modules.trakt import getTraktCredentialsInfo, getTraktIndicatorsInfo


class Navigator:
	def __init__(self):
		self.artPath = control.artPath()
		self.iconLogos = control.setting('icon.logos') != 'Traditional'
		self.indexLabels = control.setting('index.labels') == 'true'
		self.traktCredentials = getTraktCredentialsInfo()
		self.traktIndicators = getTraktIndicatorsInfo()
		self.imdbCredentials = control.setting('imdb.user') != ''
		self.tmdbSessionID = control.setting('tmdb.session_id') != ''
        
	def root(self):
		if control.getMenuEnabled('navi.holidays') == True:        
			self.addDirectoryItem(90157, 'holidaysNavigator', 'holidays.png', 'holidays.png')
		if control.getMenuEnabled('navi.halloween') == True:        
			self.addDirectoryItem(90144, 'halloweenNavigator', 'halloween.png', 'halloween.png')			
		self.addDirectoryItem(32001, 'movieNavigator', 'movies.png', 'DefaultMovies.png')
		self.addDirectoryItem(32002, 'tvNavigator', 'tvshows.png', 'DefaultTVShows.png')
		if control.getMenuEnabled('navi.anime'):
			self.addDirectoryItem('Anime', 'anime_Navigator', 'boxsets.png', 'DefaultFolder.png')
		if control.getMenuEnabled('mylists.widget'):
			self.addDirectoryItem(32003, 'mymovieNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')
			self.addDirectoryItem(32004, 'mytvNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')
		if control.getMenuEnabled('navi.imdbtop250') == True:
			self.addDirectoryItem(90313, 'imdbtop250', 'imdb.png', 'Defaultmovies.png')
		if control.getMenuEnabled('navi.hodgepodge') == True:
			self.addDirectoryItem(90314, 'hodgepodge', 'movies.png', 'Defaultmovies.png')
		if control.getMenuEnabled('navi.hacktheplanet') == True:
			self.addDirectoryItem(90315, 'movies&url=hacktheplanet', 'movies.png', 'playlist.jpg')
		if control.setting('furk.api') != '' and control.getMenuEnabled('navi.furk') : self.addDirectoryItem('Furk.net', 'furkNavigator', 'movies.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.youtube'): self.addDirectoryItem(41002, 'youtube', 'youtube.png', 'youtube.png')
		self.addDirectoryItem(32010, 'tools_searchNavigator', 'search.png', 'DefaultAddonsSearch.png')
		self.addDirectoryItem(32008, 'tools_toolNavigator', 'tools.png', 'DefaultAddonService.png')
		downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
		if downloads: self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')
		if control.getMenuEnabled('navi.prem.services'): self.addDirectoryItem(41003, 'premiumNavigator', 'premium.png', 'DefaultFolder.png')
		if control.getMenuEnabled('navi.news'): self.addDirectoryItem(32013, 'tools_ShowNews', 'icon.png', 'DefaultAddonHelper.png', isFolder=False)
		if control.getMenuEnabled('navi.changelog'): self.addDirectoryItem(32014, 'tools_ShowChangelog', 'icon.png', 'DefaultAddonsUpdates.png', isFolder=False)
		self.endDirectory()

	def furk(self):
		self.addDirectoryItem('User Files', 'furkUserFiles', 'userlists.png', 'DefaultVideoPlaylists.png')
		self.addDirectoryItem('Search', 'furkSearch', 'search.png', 'search.png')
		self.endDirectory()

	def movies(self, lite=False):
		self.count = int(control.setting('page.item.limit'))
		self.addDirectoryItem(32003, 'mymovieliteNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')		
		if control.getMenuEnabled('navi.movie.imdb.intheater'):
			self.addDirectoryItem(32421 if self.indexLabels else 32420, 'movies&url=theaters', 'imdb.png' if self.iconLogos else 'in-theaters.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.tmdb.nowplaying'):
			self.addDirectoryItem(32423 if self.indexLabels else 32422, 'tmdbmovies&url=tmdb_nowplaying', 'tmdb.png' if self.iconLogos else 'in-theaters.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.traktlist') == True:
			self.addDirectoryItem(90051, 'traktlist', 'trakt.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.imdblist') == True:
			self.addDirectoryItem(90141, 'imdblist', 'imdb.png', 'DefaultMovies.png')				
		if control.getMenuEnabled('navi.movie.trakt.anticipated'):
			self.addDirectoryItem(32425 if self.indexLabels else 32424, 'movies&url=traktanticipated', 'trakt.png' if self.iconLogos else 'in-theaters.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.tmdb.upcoming'):
			self.addDirectoryItem(32427 if self.indexLabels else 32426, 'tmdbmovies&url=tmdb_upcoming', 'tmdb.png' if self.iconLogos else 'in-theaters.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.imdb.popular'):
			self.addDirectoryItem(32429 if self.indexLabels else 32428, 'movies&url=mostpopular', 'imdb.png' if self.iconLogos else 'most-popular.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.tmdb.popular'):
			self.addDirectoryItem(32431 if self.indexLabels else 32430, 'tmdbmovies&url=tmdb_popular', 'tmdb.png' if self.iconLogos else 'most-popular.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.trakt.popular'):
			self.addDirectoryItem(32433 if self.indexLabels else 32430, 'movies&url=traktpopular', 'trakt.png' if self.iconLogos else 'most-popular.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.imdb.boxoffice'):
			self.addDirectoryItem(32435 if self.indexLabels else 32434, 'movies&url=imdbboxoffice', 'imdb.png' if self.iconLogos else 'box-office.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.tmdb.boxoffice'):
			self.addDirectoryItem(32436 if self.indexLabels else 32434, 'tmdbmovies&url=tmdb_boxoffice', 'tmdb.png' if self.iconLogos else 'box-office.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.trakt.boxoffice'):
			self.addDirectoryItem(32437 if self.indexLabels else 32434, 'movies&url=traktboxoffice', 'trakt.png' if self.iconLogos else 'box-office.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.imdb.mostvoted'):
			self.addDirectoryItem(32439 if self.indexLabels else 32438, 'movies&url=mostvoted', 'imdb.png' if self.iconLogos else 'most-voted.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.tmdb.toprated'):
			self.addDirectoryItem(32441 if self.indexLabels else 32440, 'tmdbmovies&url=tmdb_toprated', 'tmdb.png' if self.iconLogos else 'most-voted.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.trakt.trending'):
			self.addDirectoryItem(32443 if self.indexLabels else 32442, 'movies&url=trakttrending', 'trakt.png' if self.iconLogos else 'trending.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.trakt.recommended'):
			self.addDirectoryItem(32445 if self.indexLabels else 32444, 'movies&url=traktrecommendations', 'trakt.png' if self.iconLogos else 'highly-rated.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.imdb.featured'):
			self.addDirectoryItem(32447 if self.indexLabels else 32446, 'movies&url=featured', 'imdb.png' if self.iconLogos else 'movies.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.collections'):
			self.addDirectoryItem(32000, 'collections_Navigator', 'boxsets.png', 'DefaultSets.png')
		if control.getMenuEnabled('navi.movie.imdb.oscarwinners'):
			self.addDirectoryItem(32452 if self.indexLabels else 32451, 'movies&url=oscars', 'imdb.png' if self.iconLogos else 'oscar-winners.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.imdb.oscarnominees'):
			self.addDirectoryItem(32454 if self.indexLabels else 32453, 'movies&url=oscarsnominees', 'imdb.png' if self.iconLogos else 'oscar-winners.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.imdb.genres'):
			self.addDirectoryItem(32456 if self.indexLabels else 32455, 'movieGenres', 'imdb.png' if self.iconLogos else 'genres.png', 'DefaultGenre.png')
		if control.getMenuEnabled('navi.movie.imdb.years'):
			self.addDirectoryItem(32458 if self.indexLabels else 32457, 'movieYears', 'imdb.png' if self.iconLogos else 'years.png', 'DefaultYear.png')
		if control.getMenuEnabled('navi.movie.imdb.people'):
			self.addDirectoryItem(32460 if self.indexLabels else 32459, 'moviePersons', 'imdb.png' if self.iconLogos else 'people.png', 'DefaultActor.png')
		if control.getMenuEnabled('navi.movie.imdb.languages'):
			self.addDirectoryItem(32462 if self.indexLabels else 32461, 'movieLanguages', 'imdb.png' if self.iconLogos else 'languages.png', 'DefaultAddonLanguage.png')
		if control.getMenuEnabled('navi.movie.imdb.certificates'):
			self.addDirectoryItem(32464 if self.indexLabels else 32463, 'movieCertificates', 'imdb.png' if self.iconLogos else 'certificates.png', 'DefaultMovies.png')
		if not lite:
			if control.getMenuEnabled('mylists.widget'): self.addDirectoryItem(32003, 'mymovieliteNavigator', 'mymovies.png', 'DefaultMovies.png')
			self.addDirectoryItem(33044, 'moviePerson', 'imdb.png' if self.iconLogos else 'people-search.png', 'DefaultAddonsSearch.png')
			self.addDirectoryItem(33042, 'movieSearch', 'trakt.png' if self.iconLogos else 'search.png', 'DefaultAddonsSearch.png')
		self.endDirectory()

	def mymovies(self, lite=False):
		self.accountCheck()
		self.addDirectoryItem(32039, 'movieUserlists', 'userlists.png', 'DefaultVideoPlaylists.png')
		if self.traktCredentials:
			if self.traktIndicators:
				self.addDirectoryItem(35308, 'moviesUnfinished&url=traktunfinished', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
				self.addDirectoryItem(32036, 'movies&url=trakthistory', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
			self.addDirectoryItem(32683, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True, context=(32551, 'library_moviesToLibrary&url=traktwatchlist&name=traktwatchlist'))
			self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True, context=(32551, 'library_moviesToLibrary&url=traktcollection&name=traktcollection'))
		if self.imdbCredentials: self.addDirectoryItem(32682, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultVideoPlaylists.png', queue=True)
		if not lite:
			self.addDirectoryItem(32031, 'movieliteNavigator', 'movies.png', 'DefaultMovies.png')
			self.addDirectoryItem(33044, 'moviePerson', 'imdb.png' if self.iconLogos else 'people-search.png', 'DefaultAddonsSearch.png')
			self.addDirectoryItem(33042, 'movieSearch', 'search.png' if self.iconLogos else 'search.png', 'DefaultAddonsSearch.png')
		self.endDirectory()

	def tvshows(self, lite=False):
		self.count = int(control.setting('page.item.limit'))
		self.addDirectoryItem(32004, 'mytvliteNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')		
		if control.getMenuEnabled('navi.originals'):
			self.addDirectoryItem(40077 if self.indexLabels else 40070, 'tvOriginals', 'tvmaze.png' if self.iconLogos else 'networks.png', 'DefaultNetwork.png')
		if control.getMenuEnabled('navi.disney+') == True:
			self.addDirectoryItem(90426, 'tvshows&url=https://api.trakt.tv/users/thenapolitan/lists/disneyplus/items?limit=%d ' % self.count, 'disney.png', 'disney.png')
		if control.getMenuEnabled('navi.apple+') == True:
			self.addDirectoryItem(90427, 'tvshows&url=https://api.trakt.tv/users/mediashare2000/lists/apple-tv/items?limit=%d ' % self.count, 'apple.png', 'apple.png')			
		if control.getMenuEnabled('navi.tv.imdb.popular'):
			self.addDirectoryItem(32429 if self.indexLabels else 32428, 'tvshows&url=popular', 'imdb.png' if self.iconLogos else 'most-popular.png', 'DefaultTVShows.png')
		if control.getMenuEnabled('navi.tv.tmdb.popular'):
			self.addDirectoryItem(32431 if self.indexLabels else 32430, 'tmdbTvshows&url=tmdb_popular', 'tmdb.png' if self.iconLogos else 'most-popular.png', 'DefaultTVShows.png')
		if control.getMenuEnabled('navi.tv.trakt.popular'):
			self.addDirectoryItem(32433 if self.indexLabels else 32430, 'tvshows&url=traktpopular', 'trakt.png' if self.iconLogos else 'most-popular.png', 'DefaultTVShows.png', queue=True)
		if control.getMenuEnabled('navi.tv.imdb.mostvoted'):
			self.addDirectoryItem(32439 if self.indexLabels else 32438, 'tvshows&url=views', 'imdb.png' if self.iconLogos else 'most-voted.png', 'DefaultTVShows.png')
		if control.getMenuEnabled('navi.tv.tmdb.toprated'):
			self.addDirectoryItem(32441 if self.indexLabels else 32440, 'tmdbTvshows&url=tmdb_toprated', 'tmdb.png' if self.iconLogos else 'most-voted.png', 'DefaultTVShows.png')
		if control.getMenuEnabled('navi.tv.trakt.trending'):
			self.addDirectoryItem(32443 if self.indexLabels else 32442, 'tvshows&url=trakttrending', 'trakt.png' if self.iconLogos else 'trending.png', 'DefaultTVShows.png')
		if control.getMenuEnabled('navi.tv.imdb.highlyrated'):
			self.addDirectoryItem(32449 if self.indexLabels else 32448, 'tvshows&url=rating', 'imdb.png' if self.iconLogos else 'highly-rated.png', 'DefaultTVShows.png')
		if control.getMenuEnabled('navi.tv.trakt.recommended'):
			self.addDirectoryItem(32445 if self.indexLabels else 32444, 'tvshows&url=traktrecommendations', 'trakt.png' if self.iconLogos else 'highly-rated.png', 'DefaultTVShows.png', queue=True)
		if control.getMenuEnabled('navi.tv.imdb.genres'):
			self.addDirectoryItem(32456 if self.indexLabels else 32455, 'tvGenres', 'imdb.png' if self.iconLogos else 'genres.png', 'DefaultGenre.png')
		if control.getMenuEnabled('navi.tv.tvmaze.networks'):
			self.addDirectoryItem(32468 if self.indexLabels else 32469, 'tvNetworks', 'tmdb.png' if self.iconLogos else 'networks.png', 'DefaultNetwork.png')
		if control.getMenuEnabled('navi.tv.imdb.languages'):
			self.addDirectoryItem(32462 if self.indexLabels else 32461, 'tvLanguages', 'imdb.png' if self.iconLogos else 'languages.png', 'DefaultAddonLanguage.png')
		if control.getMenuEnabled('navi.tv.imdb.certificates'):
			self.addDirectoryItem(32464 if self.indexLabels else 32463, 'tvCertificates', 'imdb.png' if self.iconLogos else 'certificates.png', 'DefaultTVShows.png')
		if control.getMenuEnabled('navi.tv.tmdb.airingtoday'):
			self.addDirectoryItem(32467 if self.indexLabels else 32465, 'tmdbTvshows&url=tmdb_airingtoday', 'tmdb.png' if self.iconLogos else 'airing-today.png', 'DefaultRecentlyAddedEpisodes.png')
		if control.getMenuEnabled('navi.tv.imdb.airingtoday'):
			self.addDirectoryItem(32466 if self.indexLabels else 32465, 'tvshows&url=airing', 'imdb.png' if self.iconLogos else 'airing-today.png', 'DefaultRecentlyAddedEpisodes.png')
		if control.getMenuEnabled('navi.tv.tmdb.ontv'):
			self.addDirectoryItem(32472 if self.indexLabels else 32471, 'tmdbTvshows&url=tmdb_ontheair', 'tmdb.png' if self.iconLogos else 'new-tvshows.png', 'DefaultRecentlyAddedEpisodes.png')
		if control.getMenuEnabled('navi.tv.imdb.returningtvshows'):
			self.addDirectoryItem(32474 if self.indexLabels else 32473, 'tvshows&url=active', 'imdb.png' if self.iconLogos else 'returning-tvshows.png', 'DefaultRecentlyAddedEpisodes.png')
		if control.getMenuEnabled('navi.tv.imdb.newtvshows'):
			self.addDirectoryItem(32476 if self.indexLabels else 32475, 'tvshows&url=premiere', 'imdb.png' if self.iconLogos else 'new-tvshows.png', 'DefaultRecentlyAddedEpisodes.png')
		if control.getMenuEnabled('navi.tv.tvmaze.calendar'):
			self.addDirectoryItem(32450 if self.indexLabels else 32027, 'calendars', 'tvmaze.png' if self.iconLogos else 'calendar.png', 'DefaultYear.png')
		if not lite:
			if control.getMenuEnabled('mylists.widget'):
				self.addDirectoryItem(32004, 'mytvliteNavigator', 'mytvshows.png', 'DefaultTVShows.png')
			self.addDirectoryItem(33045, 'tvPerson', 'imdb.png' if self.iconLogos else 'people-search.png', 'DefaultAddonsSearch.png')
			self.addDirectoryItem(33043, 'tvSearch', 'trakt.png' if self.iconLogos else 'search.png', 'DefaultAddonsSearch.png')
		self.endDirectory()

	def mytvshows(self, lite=False):
		self.accountCheck()
		self.addDirectoryItem(32040, 'tvUserlists', 'userlists.png', 'DefaultVideoPlaylists.png')
		if self.traktCredentials:
			if self.traktIndicators:
				self.addDirectoryItem(35308, 'episodesUnfinished&url=traktunfinished', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
				self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
				self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
				self.addDirectoryItem(32019, 'upcomingProgress&url=progress', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
				self.addDirectoryItem(32027, 'calendar&url=mycalendar', 'trakt.png', 'DefaultYear.png', queue=True)
			self.addDirectoryItem(32683, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultVideoPlaylists.png', context=(32551, 'library_tvshowsToLibrary&url=traktwatchlist&name=traktwatchlist'))
			self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultVideoPlaylists.png', context=(32551, 'library_tvshowsToLibrary&url=traktcollection&name=traktcollection'))
			self.addDirectoryItem(32041, 'episodesUserlists', 'userlists.png', 'DefaultVideoPlaylists.png')
		if self.imdbCredentials: self.addDirectoryItem(32682, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultVideoPlaylists.png')
		if not lite:
			self.addDirectoryItem(32031, 'tvliteNavigator', 'tvshows.png', 'DefaultTVShows.png')
			self.addDirectoryItem(33045, 'tvPerson', 'imdb.png' if self.iconLogos else 'people-search.png', 'DefaultAddonsSearch.png')
			self.addDirectoryItem(33043, 'tvSearch', 'trakt.png' if self.iconLogos else 'search.png', 'DefaultAddonsSearch.png')
		self.endDirectory()

	def anime(self, lite=False):
		self.addDirectoryItem(32001, 'anime_Movies&url=anime', 'movies.png', 'DefaultMovies.png')
		self.addDirectoryItem(32002, 'anime_TVshows&url=anime', 'tvshows.png', 'DefaultTVShows.png')
		self.endDirectory()

	def tools(self):
		self.addDirectoryItem(32510, 'cache_Navigator', 'tools.png', 'DefaultAddonService.png', isFolder=True)
		self.addDirectoryItem(32609, 'tools_openMyAccount', 'MyAccounts.png', 'DefaultAddonService.png', isFolder=False)
		if control.condVisibility('System.HasAddon(service.upnext)'):
			self.addDirectoryItem(32505, 'tools_UpNextSettings', 'UpNext.png', 'DefaultAddonProgram.png', isFolder=False)
		self.addDirectoryItem(32506, 'tools_contextThorSettings', 'icon.png', 'DefaultAddonProgram.png', isFolder=False)
		#-- Providers - 4
		self.addDirectoryItem(32651, 'tools_fenomscrapersSettings', 'fenomscrapers.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(32083, 'tools_cleanSettings', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
		#-- General - 0
		self.addDirectoryItem(32043, 'tools_openSettings&query=0.0', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		#-- Navigation - 1
		self.addDirectoryItem(32362, 'tools_openSettings&query=1.1', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		#-- Playback - 3
		self.addDirectoryItem(32045, 'tools_openSettings&query=3.1', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		#-- Accounts - 7
		self.addDirectoryItem(32044, 'tools_openSettings&query=7.0', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		#-- Downloads - 9
		self.addDirectoryItem(32048, 'tools_openSettings&query=9.0', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		#-- Subtitles - 10
		self.addDirectoryItem(32046, 'tools_openSettings&query=10.0', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(32556, 'library_Navigator', 'tools.png', 'DefaultAddonService.png', isFolder=True)
		self.addDirectoryItem(32049, 'tools_viewsNavigator', 'tools.png', 'DefaultAddonService.png', isFolder=True)
		self.addDirectoryItem(32361, 'tools_resetViewTypes', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.endDirectory()

	def cf(self):
		self.addDirectoryItem(32610, 'cache_clearAll', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(32611, 'cache_clearSources', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(32612, 'cache_clearMeta', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(32613, 'cache_clearCache', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(32614, 'cache_clearSearch', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(32615, 'cache_clearBookmarks', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.endDirectory()

	def library(self):
	# -- Library - 8
		self.addDirectoryItem(32557, 'tools_openSettings&query=8.0', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
		self.addDirectoryItem(32558, 'library_update', 'library_update.png', 'DefaultAddonLibrary.png', isFolder=False)
		self.addDirectoryItem(32676, 'library_clean', 'library_update.png', 'DefaultAddonLibrary.png', isFolder=False)
		self.addDirectoryItem(32559, control.setting('library.movie'), 'movies.png', 'DefaultMovies.png', isAction=False)
		self.addDirectoryItem(32560, control.setting('library.tv'), 'tvshows.png', 'DefaultTVShows.png', isAction=False)
		if self.traktCredentials:
			self.addDirectoryItem(32561, 'library_moviesToLibrary&url=traktcollection&name=traktcollection', 'trakt.png', 'DefaultMovies.png', isFolder=False)
			self.addDirectoryItem(32562, 'library_moviesToLibrary&url=traktwatchlist&name=traktwatchlist', 'trakt.png', 'DefaultMovies.png', isFolder=False)
			self.addDirectoryItem(32672, 'library_moviesListToLibrary&url=traktlists', 'trakt.png', 'DefaultMovies.png', isFolder=False)
			self.addDirectoryItem(32673, 'library_moviesListToLibrary&url=traktlikedlists', 'trakt.png', 'DefaultMovies.png', isFolder=False)
		if self.tmdbSessionID:
			self.addDirectoryItem('TMDb: Import Movie Watchlist...', 'library_moviesToLibrary&url=tmdb_watchlist&name=tmdb_watchlist', 'tmdb.png', 'DefaultMovies.png', isFolder=False)
			self.addDirectoryItem('TMDb: Import Movie Favorites...', 'library_moviesToLibrary&url=tmdb_favorites&name=tmdb_favorites', 'tmdb.png', 'DefaultMovies.png', isFolder=False)
			self.addDirectoryItem('TMDb: Import Movie User list...', 'library_moviesListToLibrary&url=tmdb_userlists', 'tmdb.png', 'DefaultMovies.png', isFolder=False)
		if self.traktCredentials:
			self.addDirectoryItem(32563, 'library_tvshowsToLibrary&url=traktcollection&name=traktcollection', 'trakt.png', 'DefaultTVShows.png', isFolder=False)
			self.addDirectoryItem(32564, 'library_tvshowsToLibrary&url=traktwatchlist&name=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', isFolder=False)
			self.addDirectoryItem(32674, 'library_tvshowsListToLibrary&url=traktlists', 'trakt.png', 'DefaultMovies.png', isFolder=False)
			self.addDirectoryItem(32675, 'library_tvshowsListToLibrary&url=traktlikedlists', 'trakt.png', 'DefaultMovies.png', isFolder=False)
		if self.tmdbSessionID:
			self.addDirectoryItem('TMDb: Import TV Watchlist...', 'library_tvshowsToLibrary&url=tmdb_watchlist&name=tmdb_watchlist', 'tmdb.png', 'DefaultMovies.png', isFolder=False)
			self.addDirectoryItem('TMDb: Import TV Favorites...', 'library_tvshowsToLibrary&url=tmdb_favorites&name=tmdb_favorites', 'tmdb.png', 'DefaultMovies.png', isFolder=False)
			self.addDirectoryItem('TMDb: Import TV User list...', 'library_tvshowsListToLibrary&url=tmdb_userlists', 'tmdb.png', 'DefaultMovies.png', isFolder=False)
		self.endDirectory()

	def downloads(self):
		movie_downloads = control.setting('movie.download.path')
		tv_downloads = control.setting('tv.download.path')
		if len(control.listDir(movie_downloads)[0]) > 0: self.addDirectoryItem(32001, movie_downloads, 'movies.png', 'DefaultMovies.png', isAction=False)
		if len(control.listDir(tv_downloads)[0]) > 0: self.addDirectoryItem(32002, tv_downloads, 'tvshows.png', 'DefaultTVShows.png', isAction=False)
		self.endDirectory()

	def premium_services(self):
		self.addDirectoryItem(40059, 'ad_ServiceNavigator', 'alldebrid.png', 'DefaultAddonService.png')
		self.addDirectoryItem(40057, 'pm_ServiceNavigator', 'premiumize.png', 'DefaultAddonService.png')
		self.addDirectoryItem(40058, 'rd_ServiceNavigator', 'realdebrid.png', 'DefaultAddonService.png')
		self.endDirectory()

	def alldebrid_service(self):
		if control.setting('alldebrid.token'):
			self.addDirectoryItem('All-Debrid: Cloud Storage', 'ad_CloudStorage', 'alldebrid.png', 'DefaultAddonService.png')
			self.addDirectoryItem('All-Debrid: Transfers', 'ad_Transfers', 'alldebrid.png', 'DefaultAddonService.png')
			self.addDirectoryItem('All-Debrid: Account Info', 'ad_AccountInfo', 'alldebrid.png', 'DefaultAddonService.png', isFolder=False)
		else:
			self.addDirectoryItem('[I]Please visit My Accounts for setup[/I]', 'tools_openMyAccount&amp;query=1.4', 'alldebrid.png', 'DefaultAddonService.png', isFolder=False)
		self.endDirectory()

	def premiumize_service(self):
		if control.setting('premiumize.token'):
			self.addDirectoryItem('Premiumize: My Files', 'pm_MyFiles', 'premiumize.png', 'DefaultAddonService.png')
			self.addDirectoryItem('Premiumize: Transfers', 'pm_Transfers', 'premiumize.png', 'DefaultAddonService.png')
			self.addDirectoryItem('Premiumize: Account Info', 'pm_AccountInfo', 'premiumize.png', 'DefaultAddonService.png', isFolder=False)
		else:
			self.addDirectoryItem('[I]Please visit My Accounts for setup[/I]', 'tools_openMyAccount&amp;query=1.11', 'premiumize.png', 'DefaultAddonService.png', isFolder=False)
		self.endDirectory()

	def realdebrid_service(self):
		if control.setting('realdebrid.token'):
			self.addDirectoryItem('Real-Debrid: Torrent Transfers', 'rd_UserTorrentsToListItem', 'realdebrid.png', 'DefaultAddonService.png')
			self.addDirectoryItem('Real-Debrid: My Downloads', 'rd_MyDownloads&query=1', 'realdebrid.png', 'DefaultAddonService.png')
			self.addDirectoryItem('Real-Debrid: Account Info', 'rd_AccountInfo', 'realdebrid.png', 'DefaultAddonService.png',isFolder=False )
		else:
			self.addDirectoryItem('[I]Please visit My Accounts for setup[/I]', 'tools_openMyAccount&amp;query=1.18', 'realdebrid.png', 'DefaultAddonService.png', isFolder=False)
		self.endDirectory()

	def search(self):
		self.addDirectoryItem(33042, 'movieSearch', 'trakt.png' if iconLogos else 'search.png', 'DefaultAddonsSearch.png')
		self.addDirectoryItem(33043, 'tvSearch', 'trakt.png' if iconLogos else 'search.png', 'DefaultAddonsSearch.png')
		self.addDirectoryItem(33044, 'moviePerson', 'imdb.png' if iconLogos else 'people-search.png', 'DefaultAddonsSearch.png')
		self.addDirectoryItem(33045, 'tvPerson', 'imdb.png' if iconLogos else 'people-search.png', 'DefaultAddonsSearch.png')
		self.endDirectory()

	def views(self):
		try:
			syshandle = int(argv[1])
			control.hide()
			items = [(control.lang(32001), 'movies'), (control.lang(32002), 'tvshows'), (control.lang(32054), 'seasons'), (control.lang(32038), 'episodes') ]
			select = control.selectDialog([i[0] for i in items], control.lang(32049))
			if select == -1: return
			content = items[select][1]
			title = control.lang(32059)
			url = '%s?action=tools_addView&content=%s' % (argv[0], content)
			poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()
			try: item = control.item(label=title, offscreen=True)
			except: item = control.item(label=title)
			item.setInfo(type='video', infoLabels = {'title': title})
			item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'fanart': fanart, 'banner': banner})
			item.setProperty('IsPlayable', 'false')
			control.addItem(handle=syshandle, url=url, listitem=item, isFolder=False)
			control.content(syshandle, content)
			control.directory(syshandle, cacheToDisc=True)
			from resources.lib.modules import views
			views.setView(content, {})
		except:
			from resources.lib.modules import log_utils
			log_utils.error()
			return

	def accountCheck(self):
		if not self.traktCredentials and not self.imdbCredentials:
			control.hide()
			control.notification(message=32042, icon='WARNING')
			sysexit()

	def clearCacheAll(self):
		control.hide()
		if not control.yesnoDialog(control.lang(32077), '', ''): return
		try:
			def cache_clear_all():
				try:
					from resources.lib.database import cache, providerscache, metacache
					providerscache.cache_clear_providers()
					metacache.cache_clear_meta()
					cache.cache_clear()
					cache.cache_clear_search()
					# cache.cache_clear_bookmarks()
					return True
				except:
					from resources.lib.modules import log_utils
					log_utils.error()
			if cache_clear_all():
				control.notification(message=32089)
			else: control.notification(message=33586)
		except:
			from resources.lib.modules import log_utils
			log_utils.error()

	def clearCacheProviders(self):
		control.hide()
		if not control.yesnoDialog(control.lang(32056), '', ''): return
		try:
			from resources.lib.database import providerscache
			if providerscache.cache_clear_providers(): control.notification(message=32090)
			else: control.notification(message=33586)
		except:
			from resources.lib.modules import log_utils
			log_utils.error()

	def clearCacheMeta(self):
		control.hide()
		if not control.yesnoDialog(control.lang(32076), '', ''): return
		try:
			from resources.lib.database import metacache
			if metacache.cache_clear_meta(): control.notification(message=32091)
			else: control.notification(message=33586)
		except:
			from resources.lib.modules import log_utils
			log_utils.error()

	def clearCache(self):
		control.hide()
		if not control.yesnoDialog(control.lang(32056), '', ''): return
		try:
			from resources.lib.database import cache
			if cache.cache_clear(): control.notification(message=32092)
			else: control.notification(message=33586)
		except:
			from resources.lib.modules import log_utils
			log_utils.error()

	def clearCacheSearch(self):
		control.hide()
		if not control.yesnoDialog(control.lang(32056), '', ''): return
		try:
			from resources.lib.database import cache
			if cache.cache_clear_search(): control.notification(message=32093)
			else: control.notification(message=33586)
		except:
			from resources.lib.modules import log_utils
			log_utils.error()

	def clearCacheSearchPhrase(self, table, name):
		control.hide()
		if not control.yesnoDialog(control.lang(32056), '', ''): return
		try:
			from resources.lib.database import cache
			if cache.cache_clear_SearchPhrase(table, name): control.notification(message=32094)
			else: control.notification(message=33586)
		except:
			from resources.lib.modules import log_utils
			log_utils.error()

	def clearBookmarks(self):
		control.hide()
		if not control.yesnoDialog(control.lang(32056), '', ''): return
		try:
			from resources.lib.database import cache
			if cache.cache_clear_bookmarks(): control.notification(message=32100)
			else: control.notification(message=33586)
		except:
			from resources.lib.modules import log_utils
			log_utils.error()

	def clearBookmark(self, name, year):
		control.hide()
		if not control.yesnoDialog(control.lang(32056), '', ''): return
		try:
			from resources.lib.database import cache
			if cache.cache_clear_bookmark(name, year): control.notification(title=name, message=32102)
			else: control.notification(message=33586)
		except:
			from resources.lib.modules import log_utils
			log_utils.error()

	def addDirectoryItem(self, name, query, thumb, icon, context=None, queue=False, isAction=True, isFolder=True, isPlayable=False, isSearch=False, table=''):
		sysaddon = argv[0] ; syshandle = int(argv[1])
		if isinstance(name, int): name = control.lang(name)
		url = '%s?action=%s' % (sysaddon, query) if isAction else query
		thumb = control.joinPath(self.artPath, thumb) if self.artPath else icon
		if not icon.startswith('Default'): icon = control.joinPath(self.artPath, icon)
		cm = []
		queueMenu = control.lang(32065)
		if queue: cm.append((queueMenu, 'RunPlugin(%s?action=playlist_QueueItem)' % sysaddon))
		if context: cm.append((control.lang(context[0]), 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))
		if isSearch: cm.append(('Clear Search Phrase', 'RunPlugin(%s?action=cache_clearSearchPhrase&source=%s&name=%s)' % (sysaddon, table, quote_plus(name))))
		cm.append(('[COLOR red]Thor Settings[/COLOR]', 'RunPlugin(%s?action=tools_openSettings)' % sysaddon))
		try: item = control.item(label=name, offscreen=True)
		except: item = control.item(label=name)
		item.addContextMenuItems(cm)
		if isPlayable: item.setProperty('IsPlayable', 'true')
		else: item.setProperty('IsPlayable', 'false')
		item.setArt({'icon': icon, 'poster': thumb, 'thumb': thumb, 'fanart': control.addonFanart(), 'banner': thumb})
		control.addItem(handle=syshandle, url=url, listitem=item, isFolder= isFolder)

	def endDirectory(self):
		syshandle = int(argv[1])
		control.content(syshandle, 'addons')
		control.directory(syshandle, cacheToDisc=True)
        
        
	def add_addons(self):
		if control.getMenuEnabled('navi.eyecandy') == True:         
			self.addDirectoryItem(90164, 'eyecandy', 'eyecandy.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.retribution') == True:         
			self.addDirectoryItem(90165, 'retribution', 'retribution.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.titan') == True:         
			self.addDirectoryItem(90155, 'titan', 'titan.png', 'DefaultMovies.png')

		self.endDirectory()


	def sports(self):
		self.addDirectoryItem(90025, 'nfl', 'nfl.png', 'nfl.png')
		self.addDirectoryItem(90026, 'nhl', 'nhl.png', 'nhl.png')
		self.addDirectoryItem(90027, 'nba', 'nba.png', 'nba.png')
		self.addDirectoryItem(90024, 'mlb', 'mlb.png', 'mlb.png')
		self.addDirectoryItem(90023, 'ncaa', 'ncaa.png', 'ncaa.png')
		self.addDirectoryItem(90156, 'ncaab', 'ncaab.png', 'ncaab.png')
		self.addDirectoryItem(90193, 'xfl', 'xfl.png', 'xfl.png')
		self.addDirectoryItem(90028, 'ufc', 'ufc.png', 'ufc.png')
		self.addDirectoryItem(90049, 'wwe', 'wwe.png', 'wwe.png')
		self.addDirectoryItem(90115, 'boxing', 'boxing.png', 'boxing.png')
		self.addDirectoryItem(90046, 'fifa', 'fifa.png', 'fifa.png')
		self.addDirectoryItem(90136, 'tennis', 'tennis.png', 'tennis.png')
		self.addDirectoryItem(90047, 'motogp', 'motogp.png', 'motogp.png')
		self.addDirectoryItem(90151, 'f1', 'f1.png', 'f1.png')
		self.addDirectoryItem(90153, 'pga', 'pga.png', 'pga.png')
		self.addDirectoryItem(90142, 'lfl', 'lfl.png', 'lfl.png')
		self.addDirectoryItem(90114, 'misc_sports', 'misc_sports.png', 'misc_sports.png')
		#self.addDirectoryItem(90030, 'sports_channels', 'sports_schannels.png', 'sports_schannels.png')
		self.addDirectoryItem(90031, 'sreplays', 'sports_replays.png', 'sports_replays.png')
		#self.addDirectoryItem(90154, 'cricket', 'cricket.png', 'cricket.png')
		#self.addDirectoryItem(90152, 'nascar', 'nascar.png', 'nascar.png')
		self.endDirectory()

	def iptv(self):
		self.addDirectoryItem(90013, 'swiftNavigator', 'swift.png', 'swift.png')
		self.addDirectoryItem(90187, 'gitNavigator', 'iptv.png', 'iptv.png')
		self.addDirectoryItem(90184, 'fluxNavigator', 'iptv.png', 'iptv.png')
		self.addDirectoryItem(90185, 'stratusNavigator', 'iptv.png', 'iptv.png')
		self.addDirectoryItem(90186, 'lodgeNavigator', 'iptv.png', 'iptv.png')
		
		self.endDirectory()

	def iptv_fluxus(self):
		self.addDirectoryItem(90035, 'iptv', 'iptv.png', 'iptv.png')
		self.addDirectoryItem(90038, 'spanish', 'iptv.png', 'iptv.png')  
		self.addDirectoryItem(90039, 'faith', 'iptv.png', 'iptv.png')
		self.addDirectoryItem(90040, 'cctv', 'iptv.png', 'iptv.png')
		adult = True if control.setting('adult_pw') == 'lol' else False
		if adult == True:
			self.addDirectoryItem(90171, 'lust', 'main_pinkhat.png', 'DefaultMovies.png')
	   
		self.endDirectory()

	def iptv_stratus(self):
		self.addDirectoryItem(90037, 'stratus', 'iptv.png', 'iptv.png')
		self.addDirectoryItem(90179, 'arabic2', 'iptv.png', 'iptv.png')
		self.addDirectoryItem(90177, 'argentina', 'iptv.png', 'iptv.png')
		self.addDirectoryItem(90180, 'bp', 'iptv.png', 'iptv.png')
		self.addDirectoryItem(90174, 'chile', 'iptv.png', 'iptv.png')
		self.addDirectoryItem(90176, 'colombia', 'iptv.png', 'iptv.png')
		self.addDirectoryItem(90175, 'india', 'iptv.png', 'iptv.png')
		self.addDirectoryItem(90178, 'spain', 'iptv.png', 'iptv.png')
		self.endDirectory()

	def iptv_tvlodge(self):
		self.addDirectoryItem(90036, 'iptv_lodge', 'iptv.png', 'iptv.png')
		self.addDirectoryItem(90172, 'spanish2', 'iptv.png', 'iptv.png')
		self.addDirectoryItem(90173, 'arabic', 'iptv.png', 'iptv.png')
		self.endDirectory()


	def imdblist(self):

		self.addDirectoryItem(90085, 'movies&url=top100', 'imdb.png', 'DefaultMovies.png')
		self.addDirectoryItem(90409, 'movies&url=top100_classic', 'imdb.png', 'DefaultMovies.png')	
		self.addDirectoryItem(90406, 'movies&url=top100_classic_comedies', 'imdb.png', 'DefaultMovies.png')	
		self.addDirectoryItem(90407, 'movies&url=top300_comedies', 'imdb.png', 'DefaultMovies.png')			
		self.addDirectoryItem(90086, 'movies&url=top250', 'imdb.png', 'DefaultMovies.png')
		self.addDirectoryItem(90087, 'movies&url=top1000', 'imdb.png', 'DefaultMovies.png')
		self.addDirectoryItem(90089, 'movies&url=rated_g', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90090, 'movies&url=rated_pg', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90091, 'movies&url=rated_pg13', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90092, 'movies&url=rated_r', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90093, 'movies&url=rated_nc17', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90088, 'movies&url=bestdirector', 'imdb.png', 'DefaultMovies.png')
		self.addDirectoryItem(90094, 'movies&url=national_film_board', 'imdb.png', 'DefaultMovies.png')
		self.addDirectoryItem(90100, 'movies&url=dreamworks_pictures', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90095, 'movies&url=fox_pictures', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90096, 'movies&url=paramount_pictures', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90097, 'movies&url=mgm_pictures', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90099, 'movies&url=universal_pictures', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90100, 'movies&url=sony_pictures', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90101, 'movies&url=warnerbrothers_pictures', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90102, 'movies&url=amazon_prime', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90098, 'movies&url=disney_pictures', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90138, 'movies&url=family_movies', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90103, 'movies&url=classic_movies', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90408, 'movies&url=classic_comedy', 'imdb.png', 'DefaultMovies.png')	
		self.addDirectoryItem(90410, 'movies&url=classic_romance', 'imdb.png', 'DefaultMovies.png')		
		self.addDirectoryItem(90104, 'movies&url=classic_horror', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90105, 'movies&url=classic_fantasy', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90106, 'movies&url=classic_western', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90107, 'movies&url=classic_annimation', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90108, 'movies&url=classic_war', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90109, 'movies&url=classic_scifi', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90420, 'movies&url=thirties', 'imdb.png', 'DefaultTVShows.png')		
		self.addDirectoryItem(90421, 'movies&url=forties', 'imdb.png', 'DefaultTVShows.png')		
		self.addDirectoryItem(90422, 'movies&url=fifties', 'imdb.png', 'DefaultTVShows.png')		
		self.addDirectoryItem(90423, 'movies&url=sixties', 'imdb.png', 'DefaultTVShows.png')		
		self.addDirectoryItem(90424, 'movies&url=seventies', 'imdb.png', 'DefaultTVShows.png')		
		self.addDirectoryItem(90110, 'movies&url=eighties', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90111, 'movies&url=nineties', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90112, 'movies&url=thousands', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90139, 'movies&url=twenty10', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90425, 'movies&url=twenty20', 'imdb.png', 'DefaultTVShows.png')		

		self.endDirectory()

	def holidays(self):
		self.addDirectoryItem(90161, 'movies&url=top50_holiday', 'holidays.png', 'holidays.png')
		self.addDirectoryItem(90162, 'movies&url=best_holiday', 'holidays.png', 'holidays.png')
		self.addDirectoryItem(90158, 'movies&url=https://api.trakt.tv/users/movistapp/lists/christmas-movies/items', 'holidays.png', 'holidays.png')
		self.addDirectoryItem(90159, 'movies&url=https://api.trakt.tv/users/cjcope/lists/hallmark-christmas/items', 'holidays.png', 'holidays.png')
		self.addDirectoryItem(90160, 'movies&url=https://api.trakt.tv/users/mkadam68/lists/christmas-list/items', 'holidays.png', 'holidays.png')
		self.addDirectoryItem(90309, 'movies&url=http://aussiehulk.com/MyAddon/thor/Menus/christmas_collection.xml', 'holidays.png', 'holidays.png')

		self.endDirectory()

	def halloween(self):
		self.addDirectoryItem(90146, 'movies&url=halloween_imdb', 'halloween.png', 'halloween.png')
		self.addDirectoryItem(90147, 'movies&url=halloween_top_100', 'halloween.png', 'halloween.png')
		self.addDirectoryItem(90148, 'movies&url=halloween_best', 'halloween.png', 'halloween.png')
		self.addDirectoryItem(90149, 'movies&url=halloween_great', 'halloween.png', 'halloween.png')
		self.addDirectoryItem(90145, 'movies&url=https://api.trakt.tv/users/petermesh/lists/halloween-movies/items', 'halloween.png', 'halloween.png')

		self.endDirectory()


		
		
	def traktlist(self):

		self.addDirectoryItem(90041, 'movies&url=https://api.trakt.tv/users/giladg/lists/latest-releases/items', 'fhd_releases.png', 'DefaultMovies.png')
		self.addDirectoryItem(90042, 'movies&url=https://api.trakt.tv/users/giladg/lists/latest-4k-releases/items', '4k_releases.png', 'DefaultMovies.png')
		self.addDirectoryItem(90043, 'movies&url=https://api.trakt.tv/users/giladg/lists/top-10-movies-of-the-week/items', 'top_10.png', 'DefaultMovies.png')
		self.addDirectoryItem(90044, 'movies&url=https://api.trakt.tv/users/giladg/lists/academy-award-for-best-cinematography/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90045, 'movies&url=https://api.trakt.tv/users/giladg/lists/stand-up-comedy/items', 'standup.png', 'DefaultMovies.png')
		self.addDirectoryItem(90052, 'movies&url=https://api.trakt.tv/users/daz280982/lists/movie-boxsets/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90053, 'movies&url=https://api.trakt.tv/users/movistapp/lists/action/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90054, 'movies&url=https://api.trakt.tv/users/movistapp/lists/adventure/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90055, 'movies&url=https://api.trakt.tv/users/movistapp/lists/animation/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90056, 'movies&url=https://api.trakt.tv/users/ljransom/lists/comedy-movies/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90057, 'movies&url=https://api.trakt.tv/users/movistapp/lists/crime/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90058, 'movies&url=https://api.trakt.tv/users/movistapp/lists/drama/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90059, 'movies&url=https://api.trakt.tv/users/movistapp/lists/family/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90060, 'movies&url=https://api.trakt.tv/users/movistapp/lists/history/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90061, 'movies&url=https://api.trakt.tv/users/movistapp/lists/horror/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90062, 'movies&url=https://api.trakt.tv/users/movistapp/lists/music/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90063, 'movies&url=https://api.trakt.tv/users/movistapp/lists/mystery/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90064, 'movies&url=https://api.trakt.tv/users/movistapp/lists/romance/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90065, 'movies&url=https://api.trakt.tv/users/movistapp/lists/science-fiction/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90066, 'movies&url=https://api.trakt.tv/users/movistapp/lists/thriller/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90067, 'movies&url=https://api.trakt.tv/users/movistapp/lists/war/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90068, 'movies&url=https://api.trakt.tv/users/movistapp/lists/western/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90069, 'movies&url=https://api.trakt.tv/users/movistapp/lists/marvel/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90070, 'movies&url=https://api.trakt.tv/users/movistapp/lists/walt-disney-animated-feature-films/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90071, 'movies&url=https://api.trakt.tv/users/movistapp/lists/batman/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90072, 'movies&url=https://api.trakt.tv/users/movistapp/lists/superman/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90073, 'movies&url=https://api.trakt.tv/users/movistapp/lists/star-wars/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90074, 'movies&url=https://api.trakt.tv/users/movistapp/lists/007/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90075, 'movies&url=https://api.trakt.tv/users/movistapp/lists/pixar-animation-studios/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90076, 'movies&url=https://api.trakt.tv/users/movistapp/lists/quentin-tarantino-collection/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90077, 'movies&url=https://api.trakt.tv/users/movistapp/lists/rocky/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90078, 'movies&url=https://api.trakt.tv/users/movistapp/lists/dreamworks-animation/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90079, 'movies&url=https://api.trakt.tv/users/movistapp/lists/dc-comics/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90080, 'movies&url=https://api.trakt.tv/users/movistapp/lists/the-30-best-romantic-comedies-of-all-time/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90081, 'movies&url=https://api.trakt.tv/users/movistapp/lists/88th-academy-awards-winners/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90082, 'movies&url=https://api.trakt.tv/users/movistapp/lists/most-sexy-movies/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90083, 'movies&url=https://api.trakt.tv/users/movistapp/lists/dance-movies/items', 'trakt.png', 'DefaultMovies.png')
		self.addDirectoryItem(90084, 'movies&url=https://api.trakt.tv/users/movistapp/lists/halloween-movies/items', 'trakt.png', 'DefaultMovies.png')

		self.endDirectory()


	def collections(self, lite=False):
		self.addDirectoryItem('[COLOR dodgerblue]¤[/COLOR] [B][COLOR white]Actor Collection[/COLOR][/B]', 'collectionActors', 'boxsets.png', 'DefaultMovies.png')
		self.addDirectoryItem('[COLOR dodgerblue]¤[/COLOR] [B][COLOR white]Movie Collection[/COLOR][/B]', 'collectionBoxset', 'boxsets.png', 'DefaultMovies.png')
		self.addDirectoryItem('[COLOR dodgerblue]¤[/COLOR] [B][COLOR white]Car Movie Collections[/COLOR][/B]', 'collections&url=carmovies', 'boxsets.png', 'DefaultMovies.png')
		self.addDirectoryItem('[COLOR dodgerblue]¤[/COLOR] [B][COLOR white]Christmas Collection[/COLOR][/B]', 'collections&url=xmasmovies', 'boxsets.png', 'DefaultMovies.png')
		self.addDirectoryItem('[COLOR dodgerblue]¤[/COLOR] [B][COLOR white]DC Comics Collection[/COLOR][/B]', 'collections&url=dcmovies', 'boxsets.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('[COLOR dodgerblue]¤[/COLOR] [B][COLOR white]Kids Collections[/COLOR][/B]', 'collectionKids', 'boxsets.png', 'DefaultMovies.png')
		self.addDirectoryItem('[COLOR dodgerblue]¤[/COLOR] [B][COLOR white]Marvel Collection[/COLOR][/B]', 'collections&url=marvelmovies', 'boxsets.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('[COLOR dodgerblue]¤[/COLOR] [B][COLOR white]Superhero Collections[/COLOR][/B]', 'collectionSuperhero', 'boxsets.png', 'DefaultMovies.png')
		
		self.endDirectory()

	def collectionActors(self):
		self.addDirectoryItem('Adam Sandler', 'collections&url=adamsandler', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Al Pacino', 'collections&url=alpacino', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Alan Rickman', 'collections&url=alanrickman', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Anthony Hopkins', 'collections&url=anthonyhopkins', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Angelina Jolie', 'collections&url=angelinajolie', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Arnold Schwarzenegger', 'collections&url=arnoldschwarzenegger', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Charlize Theron', 'collections&url=charlizetheron', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Clint Eastwood', 'collections&url=clinteastwood', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Demi Moore', 'collections&url=demimoore', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Denzel Washington', 'collections&url=denzelwashington', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Eddie Murphy', 'collections&url=eddiemurphy', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Elvis Presley', 'collections&url=elvispresley', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Gene Wilder', 'collections&url=genewilder', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Gerard Butler', 'collections&url=gerardbutler', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Goldie Hawn', 'collections&url=goldiehawn', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Jason Statham', 'collections&url=jasonstatham', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Jean-Claude Van Damme', 'collections&url=jeanclaudevandamme', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Jeffrey Dean Morgan', 'collections&url=jeffreydeanmorgan', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('John Travolta', 'collections&url=johntravolta', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Johnny Depp', 'collections&url=johnnydepp', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Julia Roberts', 'collections&url=juliaroberts', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Kevin Costner', 'collections&url=kevincostner', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Liam Neeson', 'collections&url=liamneeson', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Mel Gibson', 'collections&url=melgibson', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Melissa McCarthy', 'collections&url=melissamccarthy', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Meryl Streep', 'collections&url=merylstreep', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Michelle Pfeiffer', 'collections&url=michellepfeiffer', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Nicolas Cage', 'collections&url=nicolascage', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Nicole Kidman', 'collections&url=nicolekidman', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Paul Newman', 'collections&url=paulnewman', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Reese Witherspoon', 'collections&url=reesewitherspoon', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Robert De Niro', 'collections&url=robertdeniro', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Samuel L Jackson', 'collections&url=samueljackson', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Sean Connery', 'collections&url=seanconnery', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Scarlett Johansson', 'collections&url=scarlettjohansson', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Sharon Stone', 'collections&url=sharonstone', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Sigourney Weaver', 'collections&url=sigourneyweaver', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Steven Seagal', 'collections&url=stevenseagal', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Tom Hanks', 'collections&url=tomhanks', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Vin Diesel', 'collections&url=vindiesel', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Wesley Snipes', 'collections&url=wesleysnipes', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Will Smith', 'collections&url=willsmith', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Winona Ryder', 'collections&url=winonaryder', 'collectionactors.png', 'DefaultRecentlyAddedMovies.png')

		self.endDirectory()


	def collectionBoxset(self):
		self.addDirectoryItem('48 Hrs. (1982-1990)', 'collections&url=fortyeighthours', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Ace Ventura (1994-1995)', 'collections&url=aceventura', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Airplane (1980-1982)', 'collections&url=airplane', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Airport (1970-1979)', 'collections&url=airport', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('American Graffiti (1973-1979)', 'collections&url=americangraffiti', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Anaconda (1997-2004)', 'collections&url=anaconda', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Analyze This (1999-2002)', 'collections&url=analyzethis', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Anchorman (2004-2013)', 'collections&url=anchorman', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Austin Powers (1997-2002)', 'collections&url=austinpowers', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Back to the Future (1985-1990)', 'collections&url=backtothefuture', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Bad Boys (1995-2003)', 'collections&url=badboys', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Bad Santa (2003-2016)', 'collections&url=badsanta', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Basic Instinct (1992-2006)', 'collections&url=basicinstinct', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Beverly Hills Cop (1984-1994)', 'collections&url=beverlyhillscop', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Big Mommas House (2000-2011)', 'collections&url=bigmommashouse', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Blues Brothers (1980-1998)', 'collections&url=bluesbrothers', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Bourne (2002-2016)', 'collections&url=bourne', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Bruce Almighty (2003-2007)', 'collections&url=brucealmighty', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Caddyshack (1980-1988)', 'collections&url=caddyshack', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Cheaper by the Dozen (2003-2005)', 'collections&url=cheaperbythedozen', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Cheech and Chong (1978-1984)', 'collections&url=cheechandchong', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Childs Play (1988-2004)', 'collections&url=childsplay', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('City Slickers (1991-1994)', 'collections&url=cityslickers', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Conan (1982-2011)', 'collections&url=conan', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Crank (2006-2009)', 'collections&url=crank', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Crocodile Dundee (1986-2001)', 'collections&url=crodiledunde', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Da Vinci Code (2006-2017)', 'collections&url=davincicode', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Daddy Day Care (2003-2007)', 'collections&url=daddydaycare', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Death Wish (1974-1994)', 'collections&url=deathwish', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Delta Force (1986-1990)', 'collections&url=deltaforce', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Die Hard (1988-2013)', 'collections&url=diehard', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Dirty Dancing (1987-2004)', 'collections&url=dirtydancing', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Dirty Harry (1971-1988)', 'collections&url=dirtyharry', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Dumb and Dumber (1994-2014)', 'collections&url=dumbanddumber', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Escape from New York (1981-1996)', 'collections&url=escapefromnewyork', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Every Which Way But Loose (1978-1980)', 'collections&url=everywhichwaybutloose', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Exorcist (1973-2005)', 'collections&url=exorcist', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('The Expendables (2010-2014)', 'collections&url=theexpendables', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Fast and the Furious (2001-2017)', 'collections&url=fastandthefurious', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Father of the Bride (1991-1995)', 'collections&url=fatherofthebride', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Fletch (1985-1989)', 'collections&url=fletch', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Friday (1995-2002)', 'collections&url=friday', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Friday the 13th (1980-2009)', 'collections&url=fridaythe13th', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Fugitive (1993-1998)', 'collections&url=fugitive', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('G.I. Joe (2009-2013)', 'collections&url=gijoe', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Get Shorty (1995-2005)', 'collections&url=getshorty', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Gettysburg (1993-2003)', 'collections&url=gettysburg', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Ghost Rider (2007-2011)', 'collections&url=ghostrider', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Ghostbusters (1984-2016)', 'collections&url=ghostbusters', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Gods Not Dead (2014-2016)', 'collections&url=godsnotdead', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Godfather (1972-1990)', 'collections&url=godfather', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Godzilla (1956-2016)', 'collections&url=godzilla', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Grown Ups (2010-2013)', 'collections&url=grownups', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Grumpy Old Men (2010-2013)', 'collections&url=grumpyoldmen', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Guns of Navarone (1961-1978)', 'collections&url=gunsofnavarone', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Halloween (1978-2009)', 'collections&url=halloween', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Hangover (2009-2013)', 'collections&url=hangover', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Hannibal Lector (1986-2007)', 'collections&url=hanniballector', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Hellraiser (1987-1996)', 'collections&url=hellraiser', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Honey I Shrunk the Kids (1989-1995)', 'collections&url=honeyishrunkthekids', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Horrible Bosses (2011-2014)', 'collections&url=horriblebosses', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Hostel (2005-2011)', 'collections&url=hostel', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Hot Shots (1991-1996)', 'collections&url=hotshots', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Independence Day (1996-2016)', 'collections&url=independenceday', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Indiana Jones (1981-2008)', 'collections&url=indianajones', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Insidious (2010-2015)', 'collections&url=insidious', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Iron Eagle (1986-1992)', 'collections&url=ironeagle', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Jack Reacher (2012-2016)', 'collections&url=jackreacher', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Jack Ryan (1990-2014)', 'collections&url=jackryan', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Jackass (2002-2013)', 'collections&url=jackass', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('James Bond (1963-2015)', 'collections&url=jamesbond', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Jaws (1975-1987)', 'collections&url=jaws', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Jeepers Creepers (2001-2017)', 'collections&url=jeeperscreepers', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('John Wick (2014-2017)', 'collections&url=johnwick', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Jumanji (1995-2005)', 'collections&url=jumanji', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Jurassic Park (1993-2015)', 'collections&url=jurassicpark', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Kick-Ass (2010-2013)', 'collections&url=kickass', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Kill Bill (2003-2004)', 'collections&url=killbill', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('King Kong (1933-2016)', 'collections&url=kingkong', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Lara Croft (2001-2003)', 'collections&url=laracroft', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Legally Blonde (2001-2003)', 'collections&url=legallyblonde', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Lethal Weapon (1987-1998)', 'collections&url=leathalweapon', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Look Whos Talking (1989-1993)', 'collections&url=lookwhostalking', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Machete (2010-2013)', 'collections&url=machete', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Magic Mike (2012-2015)', 'collections&url=magicmike', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Major League (1989-1998)', 'collections&url=majorleague', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Man from Snowy River (1982-1988)', 'collections&url=manfromsnowyriver', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Mask (1994-2005)', 'collections&url=mask', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Matrix (1999-2003)', 'collections&url=matrix', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('The Mechanic (2011-2016)', 'collections&url=themechanic', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Meet the Parents (2000-2010)', 'collections&url=meettheparents', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Men in Black (1997-2012)', 'collections&url=meninblack', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Mighty Ducks (1995-1996)', 'collections&url=mightyducks', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Miss Congeniality (2000-2005)', 'collections&url=misscongeniality', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Missing in Action (1984-1988)', 'collections&url=missinginaction', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Mission Impossible (1996-2015)', 'collections&url=missionimpossible', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Naked Gun (1988-1994)', 'collections&url=nakedgun', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('National Lampoon (1978-2006)', 'collections&url=nationallampoon', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('National Lampoons Vacation (1983-2015)', 'collections&url=nationallampoonsvacation', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('National Treasure (2004-2007)', 'collections&url=nationaltreasure', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Neighbors (2014-2016)', 'collections&url=neighbors', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Night at the Museum (2006-2014)', 'collections&url=nightatthemuseum', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Nightmare on Elm Street (1984-2010)', 'collections&url=nightmareonelmstreet', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Now You See Me (2013-2016)', 'collections&url=nowyouseeme', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Nutty Professor (1996-2000)', 'collections&url=nuttyprofessor', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Oceans Eleven (2001-2007)', 'collections&url=oceanseleven', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Odd Couple (1968-1998)', 'collections&url=oddcouple', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Oh, God (1977-1984)', 'collections&url=ohgod', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Olympus Has Fallen (2013-2016)', 'collections&url=olympushasfallen', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Omen (1976-1981)', 'collections&url=omen', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Paul Blart Mall Cop (2009-2015)', 'collections&url=paulblart', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Pirates of the Caribbean (2003-2017)', 'collections&url=piratesofthecaribbean', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Planet of the Apes (1968-2014)', 'collections&url=planetoftheapes', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Police Academy (1984-1994)', 'collections&url=policeacademy', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Poltergeist (1982-1988)', 'collections&url=postergeist', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Porkys (1981-1985)', 'collections&url=porkys', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Predator (1987-2010)', 'collections&url=predator', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('The Purge (2013-2016)', 'collections&url=thepurge', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Rambo (1982-2008)', 'collections&url=rambo', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('RED (2010-2013)', 'collections&url=red', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Revenge of the Nerds (1984-1987)', 'collections&url=revengeofthenerds', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Riddick (2000-2013)', 'collections&url=riddick', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Ride Along (2014-2016)', 'collections&url=ridealong', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('The Ring (2002-2017)', 'collections&url=thering', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('RoboCop (1987-1993)', 'collections&url=robocop', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Rocky (1976-2015)', 'collections&url=rocky', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Romancing the Stone (1984-1985)', 'collections&url=romancingthestone', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Rush Hour (1998-2007)', 'collections&url=rushhour', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Santa Clause (1994-2006)', 'collections&url=santaclause', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Saw (2004-2010)', 'collections&url=saw', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Sex and the City (2008-2010)', 'collections&url=sexandthecity', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Shaft (1971-2000)', 'collections&url=shaft', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Shanghai Noon (2000-2003)', 'collections&url=shanghainoon', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Sin City (2005-2014)', 'collections&url=sincity', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Sinister (2012-2015)', 'collections&url=sinister', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Sister Act (1995-1993)', 'collections&url=sisteract', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Smokey and the Bandit (1977-1986)', 'collections&url=smokeyandthebandit', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Speed (1994-1997)', 'collections&url=speed', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Stakeout (1987-1993)', 'collections&url=stakeout', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Star Trek (1979-2016)', 'collections&url=startrek', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Star Wars (1977-2015)', 'collections&url=starwars', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('The Sting (1973-1983)', 'collections&url=thesting', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Taken (2008-2014)', 'collections&url=taken', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Taxi (1998-2007)', 'collections&url=taxi', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Ted (2012-2015)', 'collections&url=ted', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Teen Wolf (1985-1987)', 'collections&url=teenwolf', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Terminator (1984-2015)', 'collections&url=terminator', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Terms of Endearment (1983-1996)', 'collections&url=termsofendearment', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Texas Chainsaw Massacre (1974-2013)', 'collections&url=texaschainsawmassacre', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('The Thing (1982-2011)', 'collections&url=thething', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Thomas Crown Affair (1968-1999)', 'collections&url=thomascrownaffair', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Transporter (2002-2015)', 'collections&url=transporter', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Under Siege (1992-1995)', 'collections&url=undersiege', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Universal Soldier (1992-2012)', 'collections&url=universalsoldier', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Wall Street (1987-2010)', 'collections&url=wallstreet', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Waynes World (1992-1993)', 'collections&url=waynesworld', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Weekend at Bernies (1989-1993)', 'collections&url=weekendatbernies', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Whole Nine Yards (2000-2004)', 'collections&url=wholenineyards', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('X-Files (1998-2008)', 'collections&url=xfiles', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('xXx (2002-2005)', 'collections&url=xxx', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Young Guns (1988-1990)', 'collections&url=youngguns', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Zoolander (2001-2016)', 'collections&url=zoolander', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Zorro (1998-2005)', 'collections&url=zorro', 'collectionboxset.png', 'DefaultRecentlyAddedMovies.png')

		self.endDirectory()


	def collectionKids(self):
		self.addDirectoryItem('Disney Collection', 'collections&url=disneymovies', 'collectiondisney.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Kids Boxset Collection', 'collectionBoxsetKids', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Kids Movie Collection', 'collections&url=kidsmovies', 'collectionkids.png', 'DefaultRecentlyAddedMovies.png')

		self.endDirectory()
		

	def collectionBoxsetKids(self):
		self.addDirectoryItem('101 Dalmations (1961-2003)', 'collections&url=onehundredonedalmations', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Addams Family (1991-1998)', 'collections&url=addamsfamily', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Aladdin (1992-1996)', 'collections&url=aladdin', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Alvin and the Chipmunks (2007-2015)', 'collections&url=alvinandthechipmunks', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Atlantis (2001-2003)', 'collections&url=atlantis', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Babe (1995-1998)', 'collections&url=babe', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Balto (1995-1998)', 'collections&url=balto', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Bambi (1942-2006)', 'collections&url=bambi', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Beauty and the Beast (1991-2017)', 'collections&url=beautyandthebeast', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Beethoven (1992-2014)', 'collections&url=beethoven', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Brother Bear (2003-2006)', 'collections&url=brotherbear', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Cars (2006-2017)', 'collections&url=cars', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Cinderella (1950-2007)', 'collections&url=cinderella', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Cloudy With a Chance of Meatballs (2009-2013)', 'collections&url=cloudywithachanceofmeatballs', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Despicable Me (2010-2015)', 'collections&url=despicableme', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Finding Nemo (2003-2016)', 'collections&url=findingnemo', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Fox and the Hound (1981-2006)', 'collections&url=foxandthehound', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Free Willy (1993-2010)', 'collections&url=freewilly', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Ghostbusters (1984-2016)', 'collections&url=ghostbusters', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Gremlins (1984-2016)', 'collections&url=gremlins', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Happy Feet (2006-2011)', 'collections&url=happyfeet', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Harry Potter (2001-2011)', 'collections&url=harrypotter', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Home Alone (1990-2012)', 'collections&url=homealone', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Homeward Bound (1993-1996)', 'collections&url=homewardbound', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Honey, I Shrunk the Kids (1989-1997)', 'collections&url=honeyishrunkthekids', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Hotel Transylvania (2012-2015)', 'collections&url=hoteltransylvania', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('How to Train Your Dragon (2010-2014)', 'collections&url=howtotrainyourdragon', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Hunchback of Notre Dame (1996-2002)', 'collections&url=hunchbackofnotredame', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Ice Age (2002-2016)', 'collections&url=iceage', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Jurassic Park (1993-2015)', 'collections&url=jurassicpark', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Kung Fu Panda (2008-2016)', 'collections&url=kungfupanda', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Lady and the Tramp (1955-2001)', 'collections&url=ladyandthetramp', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Lilo and Stitch (2002-2006)', 'collections&url=liloandstitch', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Madagascar (2005-2014)', 'collections&url=madagascar', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Monsters Inc (2001-2013)', 'collections&url=monstersinc', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Mulan (1998-2004)', 'collections&url=mulan', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Narnia (2005-2010)', 'collections&url=narnia', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('New Groove (2000-2005)', 'collections&url=newgroove', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Open Season (2006-2015)', 'collections&url=openseason', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Planes (2013-2014)', 'collections&url=planes', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Pocahontas (1995-1998)', 'collections&url=pocahontas', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Problem Child (1990-1995)', 'collections&url=problemchild', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Rio (2011-2014)', 'collections&url=rio', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Sammys Adventures (2010-2012)', 'collections&url=sammysadventures', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Scooby-Doo (2002-2014)', 'collections&url=scoobydoo', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Short Circuit (1986-1988)', 'collections&url=shortcircuit', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Shrek (2001-2011)', 'collections&url=shrek', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('SpongeBob SquarePants (2004-2017)', 'collections&url=spongebobsquarepants', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Spy Kids (2001-2011)', 'collections&url=spykids', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Star Wars (1977-2015)', 'collections&url=starwars', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Stuart Little (1999-2002)', 'collections&url=stuartlittle', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Tarzan (1999-2016)', 'collections&url=tarzan', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Teenage Mutant Ninja Turtles (1978-2009)', 'collections&url=teenagemutantninjaturtles', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('The Jungle Book (1967-2003)', 'collections&url=thejunglebook', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('The Karate Kid (1984-2010)', 'collections&url=thekaratekid', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('The Lion King (1994-2016)', 'collections&url=thelionking', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('The Little Mermaid (1989-1995)', 'collections&url=thelittlemermaid', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('The Neverending Story (1984-1994)', 'collections&url=theneverendingstory', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('The Smurfs (2011-2013)', 'collections&url=thesmurfs', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Tooth Fairy (2010-2012)', 'collections&url=toothfairy', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Tinker Bell (2008-2014)', 'collections&url=tinkerbell', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Tom and Jerry (1992-2013)', 'collections&url=tomandjerry', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Toy Story (1995-2014)', 'collections&url=toystory', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('VeggieTales (2002-2008)', 'collections&url=veggietales', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Winnie the Pooh (2000-2005)', 'collections&url=winniethepooh', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Wizard of Oz (1939-2013)', 'collections&url=wizardofoz', 'collectionkidsboxset.png', 'DefaultRecentlyAddedMovies.png')

		self.endDirectory()


	def collectionSuperhero(self):
		self.addDirectoryItem('Avengers (2008-2017)', 'collections&url=avengers', 'collectionsuperhero.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Batman (1989-2016)', 'collections&url=batman', 'collectionsuperhero.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Captain America (2011-2016)', 'collections&url=captainamerica', 'collectionsuperhero.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Dark Knight Trilogy (2005-2013)', 'collections&url=darkknight', 'collectionsuperhero.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Fantastic Four (2005-2015)', 'collections&url=fantasticfour', 'collectionsuperhero.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Hulk (2003-2008)', 'collections&url=hulk', 'collectionsuperhero.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Iron Man (2008-2013)', 'collections&url=ironman', 'collectionsuperhero.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Spider-Man (2002-2017)', 'collections&url=spiderman', 'collectionsuperhero.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('Superman (1978-2016)', 'collections&url=superman', 'collectionsuperhero.png', 'DefaultRecentlyAddedMovies.png')
		self.addDirectoryItem('X-Men (2000-2016)', 'collections&url=xmen', 'collectionsuperhero.png', 'DefaultRecentlyAddedMovies.png')

		self.endDirectory()

	def hodgepodge(self):
		self.addDirectoryItem('Films that are mostly taking place in one room', 'movies&url=imdb1', 'chest.png', 'chest.png')
		self.addDirectoryItem('Movies Based On True Story', 'movies&url=imdb2', 'chest.png', 'chest.png')
		self.addDirectoryItem('Best Movies Set in the 60s', 'movies&url=imdb3', 'chest.png', 'chest.png')
		self.addDirectoryItem('80s Movies', 'movies&url=imdb4', 'chest.png', 'chest.png')
		self.addDirectoryItem('Movies from the 80s you DIDNT know you should watch before you die.', 'movies&url=imdb5', 'chest.png', 'chest.png')
		self.addDirectoryItem('100 Best Action Movies of All Time', 'movies&url=imdb6', 'chest.png', 'chest.png')
		self.addDirectoryItem('Best of 80s, 90s, 00s Action', 'movies&url=imdb7', 'chest.png', 'chest.png')
		self.addDirectoryItem('Top 250 Action Movies', 'movies&url=imdb8', 'chest.png', 'chest.png')
		self.addDirectoryItem('Adventure-Fantasy Films 1970 to 1996', 'movies&url=imdb9', 'chest.png', 'chest.png')
		self.addDirectoryItem('Great Kids Adventures Movies', 'movies&url=imdb10', 'chest.png', 'chest.png')  # start
		self.addDirectoryItem('Movies dealing in some way with the afterlife', 'movies&url=imdb11', 'chest.png', 'chest.png')
		self.addDirectoryItem('Against All Odds - Survival of the fittest', 'movies&url=imdb12', 'chest.png', 'chest.png')
		self.addDirectoryItem('Agoraphobia ( Fear of going Outside )', 'movies&url=imdb13', 'chest.png', 'chest.png')
		self.addDirectoryItem('Airplane Movies', 'movies&url=imdb14', 'chest.png', 'chest.png')
		self.addDirectoryItem('Alien Life: Friendly aliens movies', 'movies&url=imdb15', 'chest.png', 'chest.png')
		self.addDirectoryItem('Aliens: Movies with Aliens', 'movies&url=imdb16', 'chest.png', 'chest.png')
		self.addDirectoryItem('Angels In Movies', 'movies&url=imdb17', 'chest.png', 'chest.png')
		self.addDirectoryItem('Animation: Best Achievements in Animation', 'movies&url=imdb18', 'chest.png', 'chest.png')
		self.addDirectoryItem('Anime/Animated', 'movies&url=imdb19', 'chest.png', 'chest.png')
		self.addDirectoryItem('Archery: Movies involving archery', 'movies&url=imdb20', 'chest.png', 'chest.png')
		self.addDirectoryItem('Atmospheric Movies', 'movies&url=imdb21', 'chest.png', 'chest.png')
		self.addDirectoryItem('Australian Summer', 'movies&url=imdb22', 'chest.png', 'chest.png')
		self.addDirectoryItem('Aviation: Pilots, Flight Attendants, Airports or Planes', 'movies&url=imdb23', 'chest.png', 'chest.png')
		self.addDirectoryItem('Awesome movies with a child/teenager in the leading role', 'movies&url=imdb24', 'chest.png', 'chest.png')
		self.addDirectoryItem('B-Movies: 80s 90s Sci-Fi & B-movies', 'movies&url=imdb25', 'chest.png', 'chest.png')
		self.addDirectoryItem('Bad Guy Wins', 'movies&url=imdb26', 'chest.png', 'chest.png')
		self.addDirectoryItem('Bad Luck - Characters Down on Their Luck', 'movies&url=imdb27', 'chest.png', 'chest.png')
		self.addDirectoryItem('BANNED: Video Nasties, The Complete 72 Banned UK Titles List', 'movies&url=imdb28', 'chest.png', 'chest.png')
		self.addDirectoryItem('Baseball Movies', 'movies&url=imdb29', 'chest.png', 'chest.png')
		self.addDirectoryItem('Before They were famous', 'movies&url=imdb30', 'chest.png', 'chest.png')
		self.addDirectoryItem('Best Buddies Movies', 'movies&url=imdb31', 'chest.png', 'chest.png')
		self.addDirectoryItem('Best Conspiracy Thrillers', 'movies&url=imdb32', 'chest.png', 'chest.png')
		self.addDirectoryItem('Best films about Civil Rights / Racism', 'movies&url=imdb33', 'chest.png', 'chest.png')
		self.addDirectoryItem('Best Movie Remakes of All Time', 'movies&url=imdb34', 'chest.png', 'chest.png')
		self.addDirectoryItem('Best of Jackie Chan', 'movies&url=imdb35', 'chest.png', 'chest.png')
		self.addDirectoryItem('Best Opening Scenes In Movies', 'movies&url=imdb36', 'chest.png', 'chest.png')
		self.addDirectoryItem('Best Special Effects in Movies', 'movies&url=imdb37', 'chest.png', 'chest.png')
		self.addDirectoryItem('Best Teen Movies of All Time', 'movies&url=imdb38', 'chest.png', 'chest.png')
		self.addDirectoryItem('Biggest names among movies: the huge, the classic and the beautiful', 'movies&url=imdb39', 'chest.png', 'chest.png')
		self.addDirectoryItem('Biography: The Best Biographical Films', 'movies&url=imdb40', 'chest.png', 'chest.png')
		self.addDirectoryItem('Biopic: Top 50 Greatest Biopics of All Time', 'movies&url=imdb41', 'chest.png', 'chest.png')
		self.addDirectoryItem('Blaxploitation Movies - Greatest Ones', 'movies&url=imdb42', 'chest.png', 'chest.png')
		self.addDirectoryItem('Body Switch Movies', 'movies&url=imdb43', 'chest.png', 'chest.png')
		self.addDirectoryItem('Boogeyman in Movies', 'movies&url=imdb44', 'chest.png', 'chest.png')
		self.addDirectoryItem('Book: A list of Movies Based on Books', 'movies&url=imdb45', 'chest.png', 'chest.png')
		self.addDirectoryItem('Bullying in Movies', 'movies&url=imdb46', 'chest.png', 'chest.png')
		self.addDirectoryItem('Campy Movies!', 'movies&url=imdb47', 'chest.png', 'chest.png')
		self.addDirectoryItem('Cartoons', 'movies&url=imdb48', 'chest.png', 'chest.png')
		self.addDirectoryItem('Chased/Sought after', 'movies&url=imdb49', 'chest.png', 'chest.png')
		self.addDirectoryItem('Cheesy love / drama / sad movies', 'movies&url=imdb50', 'chest.png', 'chest.png')
		self.addDirectoryItem('Christmas Movies', 'movies&url=imdb51', 'chest.png', 'chest.png')
		self.addDirectoryItem('Cities: Movies where the city is practically a character', 'movies&url=imdb52', 'chest.png', 'chest.png')
		self.addDirectoryItem('Clever Movies', 'movies&url=imdb53', 'chest.png', 'chest.png')
		self.addDirectoryItem('Clones Movies And Shows', 'movies&url=imdb54', 'chest.png', 'chest.png')
		self.addDirectoryItem('Coen Brothers Filmography', 'movies&url=imdb55', 'chest.png', 'chest.png')
		self.addDirectoryItem('The 100 Best Comedies of the 80s', 'movies&url=imdb56', 'chest.png', 'chest.png')
		self.addDirectoryItem('Top 200 Comedy Movies', 'movies&url=imdb57', 'chest.png', 'chest.png')
		self.addDirectoryItem('Comfy, cozy, chamber movies', 'movies&url=imdb58', 'chest.png', 'chest.png')
		self.addDirectoryItem('Coming of age: The Ultimate list', 'movies&url=imdb59', 'chest.png', 'chest.png')
		self.addDirectoryItem('Confessions, Diaries, Or Both', 'movies&url=imdb60', 'chest.png', 'chest.png')
		self.addDirectoryItem('Cops', 'movies&url=imdb61', 'chest.png', 'chest.png')
		self.addDirectoryItem('Cops: Dirty Cop Movies', 'movies&url=imdb62', 'chest.png', 'chest.png')
		self.addDirectoryItem('Cozy Winter Movies', 'movies&url=imdb63', 'chest.png', 'chest.png')
		self.addDirectoryItem('Crime Shows/Documentaries', 'movies&url=imdb64', 'chest.png', 'chest.png')
		self.addDirectoryItem('Crime: Best Crime Movies:The Ultimate List', 'movies&url=imdb65', 'chest.png', 'chest.png')
		self.addDirectoryItem('Cruise Ships Movies', 'movies&url=imdb66', 'chest.png', 'chest.png')
		self.addDirectoryItem('Cult: The Ultimate Cult Movie List', 'movies&url=imdb67', 'chest.png', 'chest.png')
		self.addDirectoryItem('Cyberpunk', 'movies&url=imdb68', 'chest.png', 'chest.png')
		self.addDirectoryItem('Dance movies / great list of dance movies', 'movies&url=imdb69', 'chest.png', 'chest.png')
		self.addDirectoryItem('Dark and Gritty Movies', 'movies&url=imdb70', 'chest.png', 'chest.png')
		self.addDirectoryItem('Dark Comedies', 'movies&url=imdb71', 'chest.png', 'chest.png')
		self.addDirectoryItem('Desert themed movies', 'movies&url=imdb72', 'chest.png', 'chest.png')
		self.addDirectoryItem('Detectives: Best Detective Films and TV series:The Ultimate List', 'movies&url=imdb73', 'chest.png', 'chest.png')
		self.addDirectoryItem('Direct to Video Movies That Are Actually Great', 'movies&url=imdb74', 'chest.png', 'chest.png')
		self.addDirectoryItem('Disaster Movies. Huge list of disaster movies', 'movies&url=imdb75', 'chest.png', 'chest.png')
		self.addDirectoryItem('Disney Movies - Animated', 'movies&url=imdb76', 'chest.png', 'chest.png')
		self.addDirectoryItem('Disney: Every Disney Movies', 'movies&url=imdb77', 'chest.png', 'chest.png')
		self.addDirectoryItem('Disorder: Movies about physical disability', 'movies&url=imdb78', 'chest.png', 'chest.png')
		self.addDirectoryItem('Disorder: Movies Depicting Mental Disorders', 'movies&url=imdb79', 'chest.png', 'chest.png')
		self.addDirectoryItem('Disorder: Movies with main characters that are blind', 'movies&url=imdb80', 'chest.png', 'chest.png')
		self.addDirectoryItem('Disorder:Brain Powers', 'movies&url=imdb81', 'chest.png', 'chest.png')
		self.addDirectoryItem('Disorder: The best movies about INSANITY', 'movies&url=imdb82', 'chest.png', 'chest.png')
		self.addDirectoryItem('Dolls, Puppets, Dummies, Mannequins, Toys, and Marionettes', 'movies&url=imdb83', 'chest.png', 'chest.png')
		self.addDirectoryItem('Drugs: Modern Films & TV Shows About Drugs/Pharmaceuticals', 'movies&url=imdb84', 'chest.png', 'chest.png')
		self.addDirectoryItem('Ethnic: Must See Movies For Black Folks', 'movies&url=imdb85', 'chest.png', 'chest.png')
		self.addDirectoryItem('Ethnic: The Best hood movies', 'movies&url=imdb86', 'chest.png', 'chest.png')
		self.addDirectoryItem('Evil Kid Horror Movies', 'movies&url=imdb87', 'chest.png', 'chest.png')
		self.addDirectoryItem('Expedition Gone Wrong Movies', 'movies&url=imdb88', 'chest.png', 'chest.png')
		self.addDirectoryItem('Fairy Tale Movies', 'movies&url=imdb89', 'chest.png', 'chest.png')
		self.addDirectoryItem('Family: 100 best family movies ever for your children', 'movies&url=imdb90', 'chest.png', 'chest.png')
		self.addDirectoryItem('Fantasy: Some of the best fantasy kid movies ever', 'movies&url=imdb90', 'chest.png', 'chest.png')
		self.addDirectoryItem('Farms', 'movies&url=imdb91', 'chest.png', 'chest.png')
		self.addDirectoryItem('Feel Good Movies', 'movies&url=imdb92', 'chest.png', 'chest.png')
		self.addDirectoryItem('Fighting Movies', 'movies&url=imdb93', 'chest.png', 'chest.png')
		self.addDirectoryItem('Films with disfigured characters', 'movies&url=imdb94', 'chest.png', 'chest.png')
		self.addDirectoryItem('Food & Restaurant Movies', 'movies&url=imdb95', 'chest.png', 'chest.png')
		self.addDirectoryItem('Foreign: Some of the Best Foreign Films', 'movies&url=imdb96', 'chest.png', 'chest.png')
		self.addDirectoryItem('Found Footage Movies', 'movies&url=imdb97', 'chest.png', 'chest.png')
		self.addDirectoryItem('Frat Pack Movies', 'movies&url=imdb98', 'chest.png', 'chest.png')
		self.addDirectoryItem('Full list of comic based movies', 'movies&url=imdb99', 'chest.png', 'chest.png')
		self.addDirectoryItem('Funny Movies of all sorts', 'movies&url=imdb100', 'chest.png', 'chest.png')
		self.addDirectoryItem('Futuristic Apocalypse Movies', 'movies&url=imdb101', 'chest.png', 'chest.png')
		self.addDirectoryItem('Futuristic: 200 futuristic apocalypse films', 'movies&url=imdb102', 'chest.png', 'chest.png')
		self.addDirectoryItem('Ghost Ship movies collection', 'movies&url=imdb103', 'chest.png', 'chest.png')
		self.addDirectoryItem('Ghosts: The best of Ghost Movies', 'movies&url=imdb104', 'chest.png', 'chest.png')
		self.addDirectoryItem('Great Soundtracks in Movies', 'movies&url=imdb105', 'chest.png', 'chest.png')
		self.addDirectoryItem('GREATEST MOVIES: 2000-2017', 'movies&url=imdb106', 'chest.png', 'chest.png')
		self.addDirectoryItem('Hacking / Computer Geeks', 'movies&url=imdb107', 'chest.png', 'chest.png')
		self.addDirectoryItem('Halloween Themed Movies and Movies with Halloween Scenes', 'movies&url=imdb108', 'chest.png', 'chest.png')
		self.addDirectoryItem('High School: Best High School Themed Movies', 'movies&url=imdb109', 'chest.png', 'chest.png')
		self.addDirectoryItem('Hillbillys, Rednecks & Hicks', 'movies&url=imdb110', 'chest.png', 'chest.png')
		self.addDirectoryItem('Hip-hop culture / racial discrimination and etc.', 'movies&url=imdb111', 'chest.png', 'chest.png')
		self.addDirectoryItem('Hipster Movies', 'movies&url=imdb112', 'chest.png', 'chest.png')
		self.addDirectoryItem('Hitmen: Great list of movies with Hitmen/Assassins', 'movies&url=imdb113', 'chest.png', 'chest.png')
		self.addDirectoryItem('Home Invasion movies', 'movies&url=imdb114', 'chest.png', 'chest.png')
		self.addDirectoryItem('Hood/Gangsters/Ghetto movies', 'movies&url=imdb115', 'chest.png', 'chest.png')
		self.addDirectoryItem('horror flicks based on true story', 'movies&url=imdb116', 'chest.png', 'chest.png')
		self.addDirectoryItem('Horror Movies 2017', 'movies&url=imdb117', 'chest.png', 'chest.png')
		self.addDirectoryItem('Horror movies with awesome houses', 'movies&url=imdb118', 'chest.png', 'chest.png')
		self.addDirectoryItem('Horror: Best Horror Movies of the 2000s', 'movies&url=imdb119', 'chest.png', 'chest.png')
		self.addDirectoryItem('Horror: Cabins/Cottages', 'movies&url=imdb120', 'chest.png', 'chest.png')
		self.addDirectoryItem('Horror: Christmas Horror', 'movies&url=imdb121', 'chest.png', 'chest.png')
		self.addDirectoryItem('Horror: Creeps / Stalkers', 'movies&url=imdb122', 'chest.png', 'chest.png')
		self.addDirectoryItem('Horror: Haunted Houses - The Ultimate List', 'movies&url=imdb123', 'chest.png', 'chest.png')
		self.addDirectoryItem('Horror: Horror movies set in asylums/ mental hospitals', 'movies&url=imdb124', 'chest.png', 'chest.png')
		self.addDirectoryItem('Horror: Korean Horror Movies', 'movies&url=imdb125', 'chest.png', 'chest.png')
		self.addDirectoryItem('Horror: Redneck Horror Movies', 'movies&url=imdb126', 'chest.png', 'chest.png')
		self.addDirectoryItem('Horror: Slashers Horror', 'movies&url=imdb127', 'chest.png', 'chest.png')
		self.addDirectoryItem('Horror: Slow Burn Horror', 'movies&url=imdb128', 'chest.png', 'chest.png')
		self.addDirectoryItem('Horror: Underlooked Gems', 'movies&url=imdb129', 'chest.png', 'chest.png')
		self.addDirectoryItem('Horror: Winter-setting horror movies', 'movies&url=imdb130', 'chest.png', 'chest.png')
		self.addDirectoryItem('Imaginary friends', 'movies&url=imdb131', 'chest.png', 'chest.png')
		self.addDirectoryItem('Inspirational movies "BASED ON TRUE STORY"', 'movies&url=imdb132', 'chest.png', 'chest.png')
		self.addDirectoryItem('Island: Stranded on an Island', 'movies&url=imdb133', 'chest.png', 'chest.png')
		self.addDirectoryItem('Jack Nicholson - The Filmography', 'movies&url=imdb134', 'chest.png', 'chest.png')
		self.addDirectoryItem('James Bond: The Complete Collection', 'movies&url=imdb135', 'chest.png', 'chest.png')
		self.addDirectoryItem('James Wan', 'movies&url=imdb136', 'chest.png', 'chest.png')
		self.addDirectoryItem('JcVd', 'movies&url=imdb137', 'chest.png', 'chest.png')
		self.addDirectoryItem('John Hughes Movies', 'movies&url=imdb138', 'chest.png', 'chest.png')
		self.addDirectoryItem('Jump Scares', 'movies&url=imdb139', 'chest.png', 'chest.png')
		self.addDirectoryItem('Jungle: Movies taking place in jungles', 'movies&url=imdb140', 'chest.png', 'chest.png')
		self.addDirectoryItem('Kid-friendly "Halloween" movies & TV shows', 'movies&url=imdb141', 'chest.png', 'chest.png')
		self.addDirectoryItem('Kid/Teens Adventures', 'movies&url=imdb142', 'chest.png', 'chest.png')
		self.addDirectoryItem('Kidnapped or Hostage movies', 'movies&url=imdb143', 'chest.png', 'chest.png')
		self.addDirectoryItem('Killer bug movies', 'movies&url=imdb144', 'chest.png', 'chest.png')
		self.addDirectoryItem('Las Vegas: List of films set in Las Vegas', 'movies&url=imdb145', 'chest.png', 'chest.png')
		self.addDirectoryItem('Law: Great movies with lawyers', 'movies&url=imdb146', 'chest.png', 'chest.png')
		self.addDirectoryItem('Lesbian: Huge lesbian movies list', 'movies&url=imdb147', 'chest.png', 'chest.png')
		self.addDirectoryItem('Life Lessons: Movies with life lessons', 'movies&url=imdb148', 'chest.png', 'chest.png')
		self.addDirectoryItem('Lifetime Movies That Are Great', 'movies&url=imdb149', 'chest.png', 'chest.png')
		self.addDirectoryItem('Lighthouses: Movies set in a Lighthouse', 'movies&url=imdb150', 'chest.png', 'chest.png')
		self.addDirectoryItem('Live-Action Fairy Tale Movies', 'movies&url=imdb151', 'chest.png', 'chest.png')
		self.addDirectoryItem('Losers in Movies', 'movies&url=imdb152', 'chest.png', 'chest.png')
		self.addDirectoryItem('Mafia, Gangsters, Mob Movies', 'movies&url=imdb153', 'chest.png', 'chest.png')
		self.addDirectoryItem('Magic: Movies and Shows About Magic', 'movies&url=imdb154', 'chest.png', 'chest.png')
		self.addDirectoryItem('Martial Arts: Awesome Martial Arts Movies!', 'movies&url=imdb155', 'chest.png', 'chest.png')
		self.addDirectoryItem('Martial Arts: The Top 250 Greatest Martial Arts Movies of All-Time', 'movies&url=imdb156', 'chest.png', 'chest.png')
		self.addDirectoryItem('Medieval Movies', 'movies&url=imdb157', 'chest.png', 'chest.png')
		self.addDirectoryItem('Medieval: Films set in the Middle Ages', 'movies&url=imdb158', 'chest.png', 'chest.png')
		self.addDirectoryItem('Mel Brooks Movies', 'movies&url=imdb159', 'chest.png', 'chest.png')
		self.addDirectoryItem('Military: 54 MOVIES INVOLVING MILITARY TRAINING', 'movies&url=imdb160', 'chest.png', 'chest.png')
		self.addDirectoryItem('Missing Person/People movie', 'movies&url=imdb161', 'chest.png', 'chest.png')
		self.addDirectoryItem('Modern (1990s-Now) Films That are Set in the 1970s', 'movies&url=imdb162', 'chest.png', 'chest.png')
		self.addDirectoryItem('Modern People in Historical Setting or Historical/Ancient', 'movies&url=imdb163', 'chest.png', 'chest.png')
		self.addDirectoryItem('Modern Westerns', 'movies&url=imdb163', 'chest.png', 'chest.png')
		self.addDirectoryItem('Monsters: Movies featuring monsters', 'movies&url=imdb165', 'chest.png', 'chest.png')
		self.addDirectoryItem('Moon: Top 10 Moon Movies', 'movies&url=imdb166', 'chest.png', 'chest.png')
		self.addDirectoryItem('Movies for High School Girls', 'movies&url=imdb167', 'chest.png', 'chest.png')
		self.addDirectoryItem('Movies inside a Video-Game', 'movies&url=imdb168', 'chest.png', 'chest.png')
		self.addDirectoryItem('Movies involving Portrayals of Real Life Teachers', 'movies&url=imdb169', 'chest.png', 'chest.png')
		self.addDirectoryItem('Movies set in San Francisco/ Bay Area', 'movies&url=imdb170', 'chest.png', 'chest.png')
		self.addDirectoryItem('Movies similar to the burbs', 'movies&url=imdb171', 'chest.png', 'chest.png')
		self.addDirectoryItem('Movies that keep you guessing until the end', 'movies&url=imdb172', 'chest.png', 'chest.png')
		self.addDirectoryItem('Movies that switch Genres halfway through', 'movies&url=imdb173', 'chest.png', 'chest.png')
		self.addDirectoryItem('Movies That Take Place In A Single Day', 'movies&url=imdb174', 'chest.png', 'chest.png')
		self.addDirectoryItem('Movies To Watch On a Rainy Day', 'movies&url=imdb175', 'chest.png', 'chest.png')
		self.addDirectoryItem('Movies with great aesthetics', 'movies&url=imdb176', 'chest.png', 'chest.png')
		self.addDirectoryItem('Movies written, directed and starring the same person', 'movies&url=imdb177', 'chest.png', 'chest.png')
		self.addDirectoryItem('Music: LIST OF 356 FILMS ABOUT OR INVOLVING MUSICIANS', 'movies&url=imdb178', 'chest.png', 'chest.png')
		self.addDirectoryItem('Must See World War II Documentaries', 'movies&url=imdb179', 'chest.png', 'chest.png')
		self.addDirectoryItem('Mystery Movies set in Castles and Mansions', 'movies&url=imdb180', 'chest.png', 'chest.png')
		self.addDirectoryItem('Narrated Movies', 'movies&url=imdb181', 'chest.png', 'chest.png')
		self.addDirectoryItem('National Lampoon Marathon!', 'movies&url=imdb182', 'chest.png', 'chest.png')
		self.addDirectoryItem('Nature Documentaries!', 'movies&url=imdb183', 'chest.png', 'chest.png')
		self.addDirectoryItem('Nature: Man vs. Nature/Animal movies', 'movies&url=imdb184', 'chest.png', 'chest.png')
		self.addDirectoryItem('Nature: Scuba / Underwater / Diving', 'movies&url=imdb185', 'chest.png', 'chest.png')
		self.addDirectoryItem('Noir: 100 Best Film-Noir movies', 'movies&url=imdb186', 'chest.png', 'chest.png')
		self.addDirectoryItem('Nostalgia Inducing Movies For People In Their Mid 20s 30s', 'movies&url=imdb187', 'chest.png', 'chest.png')
		self.addDirectoryItem('Ocean Adventure', 'movies&url=imdb188', 'chest.png', 'chest.png')
		self.addDirectoryItem('One Man Army', 'movies&url=imdb189', 'chest.png', 'chest.png')
		self.addDirectoryItem('Outer Space movies/Great Space Exploration', 'movies&url=imdb190', 'chest.png', 'chest.png')
		self.addDirectoryItem('Parallel stories ', 'movies&url=imdb191', 'chest.png', 'chest.png')
		self.addDirectoryItem('Paul Verhoeven Movies', 'movies&url=imdb192', 'chest.png', 'chest.png')
		self.addDirectoryItem('Plot Twists In Movies', 'movies&url=imdb193', 'chest.png', 'chest.png')
		self.addDirectoryItem('Politics: 150 FILMS', 'movies&url=imdb194', 'chest.png', 'chest.png')
		self.addDirectoryItem('Post-Apocalyptic Movies', 'movies&url=imdb195', 'chest.png', 'chest.png')
		self.addDirectoryItem('Prison-Jail Movies', 'movies&url=imdb196', 'chest.png', 'chest.png')
		self.addDirectoryItem('Psychological Thrillers', 'movies&url=imdb197', 'chest.png', 'chest.png')
		self.addDirectoryItem('Psychologists/Psychiatrists/Therapists', 'movies&url=imdb198', 'chest.png', 'chest.png')
		self.addDirectoryItem('Psychosexual thrillers', 'movies&url=imdb199', 'chest.png', 'chest.png')
		self.addDirectoryItem('Quotable: Top 50 Most Quotable Movies Ever', 'movies&url=imdb200', 'chest.png', 'chest.png')
		self.addDirectoryItem('R rated superhero movies', 'movies&url=imdb201', 'chest.png', 'chest.png')
		self.addDirectoryItem('Rape & Revenge', 'movies&url=imdb202', 'chest.png', 'chest.png')
		self.addDirectoryItem('Really Long Movies', 'movies&url=imdb203', 'chest.png', 'chest.png')
		self.addDirectoryItem('Reddit - Films Before You Die', 'movies&url=imdb204', 'chest.png', 'chest.png')
		self.addDirectoryItem('Revenge & Vigilante Movies', 'movies&url=imdb205', 'chest.png', 'chest.png')
		self.addDirectoryItem('Road Trips - Travels', 'movies&url=imdb206', 'chest.png', 'chest.png')
		self.addDirectoryItem('Robbery / Heist Movies', 'movies&url=imdb207', 'chest.png', 'chest.png')
		self.addDirectoryItem('Robot Movies', 'movies&url=imdb208', 'chest.png', 'chest.png')
		self.addDirectoryItem('Romance: Best romance in movies', 'movies&url=imdb209', 'chest.png', 'chest.png')
		self.addDirectoryItem('Romance: Bromance in Movies', 'movies&url=imdb210', 'chest.png', 'chest.png')
		self.addDirectoryItem('Romance: Forbidden Love in Movies', 'movies&url=imdb211', 'chest.png', 'chest.png')
		self.addDirectoryItem('Romance: Unconventional Romance Films', 'movies&url=imdb212', 'chest.png', 'chest.png')
		self.addDirectoryItem('Saddest Movies - Movies That Will Make You Cry', 'movies&url=imdb213', 'chest.png', 'chest.png')
		self.addDirectoryItem('Sailing & Seamanship Movies', 'movies&url=imdb214', 'chest.png', 'chest.png')
		self.addDirectoryItem('Sam Rockwell Movies', 'movies&url=imdb215', 'chest.png', 'chest.png')
		self.addDirectoryItem('Sci-Fi Based on Books, Short Stories, or Graphic Novels', 'movies&url=imdb216', 'chest.png', 'chest.png')
		self.addDirectoryItem('Sci-Fi: The Truly Ultimate Sci-Fi List: 1902-2015', 'movies&url=imdb217', 'chest.png', 'chest.png')
		self.addDirectoryItem('Sequels: 30 Great Sequels', 'movies&url=imdb218', 'chest.png', 'chest.png')
		self.addDirectoryItem('Serial Killer Movies', 'movies&url=imdb219', 'chest.png', 'chest.png')
		self.addDirectoryItem('Sharks, Sharks and Sharks!', 'movies&url=imdb220', 'chest.png', 'chest.png')
		self.addDirectoryItem('Sniper Movies', 'movies&url=imdb221', 'chest.png', 'chest.png')
		self.addDirectoryItem('Social Network: Movies ', 'movies&url=imdb222', 'chest.png', 'chest.png')
		self.addDirectoryItem('Some of The Best Military movies of all time', 'movies&url=imdb223', 'chest.png', 'chest.png')
		self.addDirectoryItem('Some Of The Most Inventive and Creative', 'movies&url=imdb224', 'chest.png', 'chest.png')
		self.addDirectoryItem('Spies: Best Spy Movies:The Ultimate List', 'movies&url=imdb225', 'chest.png', 'chest.png')
		self.addDirectoryItem('Steampunk', 'movies&url=imdb226', 'chest.png', 'chest.png')
		self.addDirectoryItem('Stephen King: Real Stephen King Movies / Adaptions', 'movies&url=imdb227', 'chest.png', 'chest.png')
		self.addDirectoryItem('Steven Spielberg Feature Filmography', 'movies&url=imdb228', 'chest.png', 'chest.png')
		self.addDirectoryItem('Strippers: Movies Featuring Strippers', 'movies&url=imdb229', 'chest.png', 'chest.png')
		self.addDirectoryItem('Submarines', 'movies&url=imdb230', 'chest.png', 'chest.png')
		self.addDirectoryItem('Suburban Nostalgia, Spider-Man, Superman, Avengers', 'movies&url=imdb231', 'chest.png', 'chest.png')
		self.addDirectoryItem('Super Hero Films, Superman, Avengers', 'movies&url=imdb232', 'chest.png', 'chest.png')
		self.addDirectoryItem('Surfing: Movies about surfing', 'movies&url=imdb233', 'chest.png', 'chest.png')
		self.addDirectoryItem('Tarantino-Esque Movies: THE ULTIMATE LIST', 'movies&url=imdb234', 'chest.png', 'chest.png')
		self.addDirectoryItem('The Best Non Animated Children, Teen and Family Movies of all Time', 'movies&url=imdb235', 'chest.png', 'chest.png')
		self.addDirectoryItem('The best Vampire Movies!', 'movies&url=imdb236', 'chest.png', 'chest.png')
		self.addDirectoryItem('The Criterion Collection', 'movies&url=imdb237', 'chest.png', 'chest.png')
		self.addDirectoryItem('The Finest Fantasy: 25 Must-See Sword & Sorcery Films', 'movies&url=imdb237', 'chest.png', 'chest.png')
		self.addDirectoryItem('The Girlfriends Corner', 'movies&url=imdb238', 'chest.png', 'chest.png')
		self.addDirectoryItem('The Greatest Acting Performances of All Time', 'movies&url=imdb239', 'chest.png', 'chest.png')
		self.addDirectoryItem('The One True God', 'movies&url=imdb240', 'chest.png', 'chest.png')
		self.addDirectoryItem('Time Travel Movies', 'movies&url=imdb241', 'chest.png', 'chest.png')
		self.addDirectoryItem('Top 100 Gore Films', 'movies&url=imdb242', 'chest.png', 'chest.png')
		self.addDirectoryItem('Top 240 Horror Movies 2000-2016', 'movies&url=imdb243', 'chest.png', 'chest.png')
		self.addDirectoryItem('Top50 World War II Movies', 'movies&url=imdb244', 'chest.png', 'chest.png')
		self.addDirectoryItem('Trapped Movies', 'movies&url=imdb245', 'chest.png', 'chest.png')
		self.addDirectoryItem('TV: Live-Action TV Series Based on Comics', 'movies&url=imdb246', 'chest.png', 'chest.png')
		self.addDirectoryItem('TV: Live-action TV series based on Marvel Comics', 'movies&url=imdb247', 'chest.png', 'chest.png')
		self.addDirectoryItem('Underdogs in Movies', 'movies&url=imdb248', 'chest.png', 'chest.png')
		self.addDirectoryItem('Vacations: 100+ Summer, Vacation, and Beach Movies', 'movies&url=imdb249', 'chest.png', 'chest.png')
		self.addDirectoryItem('Vampire and Werewolf Movies', 'movies&url=imdb250', 'chest.png', 'chest.png')
		self.addDirectoryItem('Victorian Era', 'movies&url=imdb251', 'chest.png', 'chest.png')
		self.addDirectoryItem('Video Games: Movies/Series involving video games', 'movies&url=imdb252', 'chest.png', 'chest.png')
		self.addDirectoryItem('Visually Striking - Good Cinematography', 'movies&url=imdb253', 'chest.png', 'chest.png')
		self.addDirectoryItem('War: 1600+ War movies list', 'movies&url=imdb254', 'chest.png', 'chest.png')
		self.addDirectoryItem('War: Top 25 Greatest War Movies of All Time', 'movies&url=imdb255', 'chest.png', 'chest.png')
		self.addDirectoryItem('Weather: Films Set in a Heat Wave', 'movies&url=imdb256', 'chest.png', 'chest.png')
		self.addDirectoryItem('Weed Movies', 'movies&url=imdb257', 'chest.png', 'chest.png')
		self.addDirectoryItem('Weird claustrophobic movies like Cube and Saw', 'movies&url=imdb258', 'chest.png', 'chest.png')
		self.addDirectoryItem('Westerns with HD releases', 'movies&url=imdb259', 'chest.png', 'chest.png')
		self.addDirectoryItem('Wilderness Survival Movies', 'movies&url=imdb260', 'chest.png', 'chest.png')
		self.addDirectoryItem('Winter and Snow Movies: The Ultimate List', 'movies&url=imdb261', 'chest.png', 'chest.png')
		self.addDirectoryItem('Witches: Best Witch Movies', 'movies&url=imdb262', 'chest.png', 'chest.png')
		self.addDirectoryItem('Worst Movies of All Time', 'movies&url=imdb263', 'chest.png', 'chest.png')
		self.addDirectoryItem('WTF - Weird, fcked up , Bizzare etc', 'movies&url=imdb264', 'chest.png', 'chest.png')
		self.addDirectoryItem('Zombies: Definitive zombie list', 'movies&url=imdb265', 'chest.png', 'chest.png')

		self.endDirectory()



	def movieCollections(self, lite=False):  # Collections ####################
		self.addDirectoryItem('Alien Invasion', 'movies&url=alien', 'alien.png', 'playlist.jpg')
		self.addDirectoryItem('Anime', 'movies&url=anime', 'anime.png', 'playlist.jpg')
		self.addDirectoryItem('Avant Garde', 'movies&url=avant', 'avant.png', 'playlist.jpg')
		self.addDirectoryItem('Based On A True Story', 'movies&url=true', 'true.png', 'playlist.jpg')
		self.addDirectoryItem('Biographical', 'movies&url=bio', 'bio.png', 'playlist.jpg')
		self.addDirectoryItem('Biker', 'movies&url=biker', 'biker.png', 'playlist.jpg')
		self.addDirectoryItem('B Movies', 'movies&url=bmovie', 'bmovie.png', 'playlist.jpg')
		self.addDirectoryItem('Breaking The Fourth Wall', 'movies&url=breaking', 'breaking.png', 'playlist.jpg')
		self.addDirectoryItem('Business', 'movies&url=business', 'business.png', 'playlist.jpg')
		self.addDirectoryItem('Capers', 'movies&url=caper', 'caper.png', 'playlist.jpg')
		self.addDirectoryItem('Chick Flix', 'movies&url=chick', 'chick.png', 'playlist.jpg')
		self.addDirectoryItem('Coen Brothers Movies', 'movies&url=coen', 'coen.png', 'playlist.jpg')
		self.addDirectoryItem('Competition', 'movies&url=competition', 'comps.png', 'playlist.jpg')
		self.addDirectoryItem('Crime', 'movies&url=crime', 'crime.png', 'playlist.jpg')
		self.addDirectoryItem('Cult', 'movies&url=cult', 'cult.png', 'playlist.jpg')
		# self.addDirectoryItem('Cult Horror Movies', 'movies&url=imdb9', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Cyberpunk', 'movies&url=cyber', 'cyber.png', 'playlist.jpg')
		self.addDirectoryItem('DC Universe', 'movies&url=dc', 'dc.png', 'playlist.jpg')
		self.addDirectoryItem('Disney and Pixar', 'movies&url=disney', 'disney.png', 'playlist.jpg')
		self.addDirectoryItem('Drug Addiction', 'movies&url=drugs', 'drugs.png', 'playlist.jpg')
		self.addDirectoryItem('Dystopia', 'movies&url=dystopia', 'dystopia.png', 'playlist.jpg')
		self.addDirectoryItem('Epic!', 'movies&url=epic', 'epic.png', 'playlist.jpg')
		self.addDirectoryItem('Espionage', 'movies&url=espionage', 'espionage.png', 'playlist.jpg')
		self.addDirectoryItem('Fairy Tale', 'movies&url=fairytale', 'fairytale.png', 'playlist.jpg')
		# self.addDirectoryItem('Fairy Tale', 'movies&url=fairytale', 'fairytale.png', 'playlist.jpg')
		self.addDirectoryItem('Farce', 'movies&url=farce', 'farce.png', 'playlist.jpg')
		self.addDirectoryItem('Femme Fatale', 'movies&url=femme', 'femme.png', 'playlist.jpg')
		self.addDirectoryItem('Futuristic', 'movies&url=futuristic', 'futuristic.png', 'playlist.jpg')
		self.addDirectoryItem('Gangster', 'movies&url=gangster', 'gangsters.png', 'playlist.jpg')
		# self.addDirectoryItem('Halloween', 'movies&url=halloween', 'halloween.png', 'season.jpg')
		self.addDirectoryItem('James Bond', 'movies&url=bond', 'bond.png', 'playlist.jpg')
		self.addDirectoryItem('Man Vs. Nature', 'movies&url=nature', 'man.png', 'playlist.jpg')
		self.addDirectoryItem('Marvel Universe', 'movies&url=marvel', 'marvel.png', 'playlist.jpg')
		self.addDirectoryItem('Motivational Movies', 'movies&url=mot', 'mot.png', 'playlist.jpg')
		self.addDirectoryItem('Monsters', 'movies&url=monsters', 'monster.png', 'playlist.jpg')
		self.addDirectoryItem('Movies To Make You Rethink Your Survival Plan', 'movies&url=survival', 'survival.png', 'playlist.jpg')
		self.addDirectoryItem('Movies To Make You Cancel That Vacation', 'movies&url=vacation', 'vaca.png', 'playlist.jpg')
		self.addDirectoryItem('Movies To Make You Pick Up And Move', 'movies&url=move', 'house.png', 'playlist.jpg')
		self.addDirectoryItem('Movies To Make You Reconsider Parenthood', 'movies&url=parenthood', 'kids.png', 'playlist.jpg')
		self.addDirectoryItem('Musical Movies', 'movies&url=music', 'musical.png', 'playlist.jpg')
		self.addDirectoryItem('Neo Noir', 'movies&url=neo', 'neo.png', 'playlist.jpg')
		self.addDirectoryItem('Parody', 'movies&url=parody', 'parody.png', 'playlist.jpg')
		self.addDirectoryItem('Post Apocalypse', 'movies&url=apocalypse', 'apocalypse.png', 'playlist.jpg')
		self.addDirectoryItem('Private Eye', 'movies&url=private', 'eye.png', 'playlist.jpg')
		self.addDirectoryItem('Psychological Thrillers', 'movies&url=psychological', 'thrill.png', 'playlist.jpg')
		self.addDirectoryItem('Revenge', 'movies&url=revenge', 'revenge.png', 'playlist.jpg')
		self.addDirectoryItem('Satire', 'movies&url=satire', 'satire.png', 'playlist.jpg')
		self.addDirectoryItem('Science Fiction', 'movies&url=sci', 'sci.png', 'playlist.jpg')
		self.addDirectoryItem('Serial Killers', 'movies&url=killer', 'killers.png', 'playlist.jpg')
		self.addDirectoryItem('Slasher', 'movies&url=slasher', 'slasher.png', 'playlist.jpg')
		self.addDirectoryItem('Sleeper Hits', 'movies&url=sleeper', 'sleeper.png', 'playlist.jpg')
		self.addDirectoryItem('Spoofs', 'movies&url=spoof', 'spoof.png', 'playlist.jpg')
		self.addDirectoryItem('Sports', 'movies&url=sports', 'sports.png', 'playlist.jpg')
		self.addDirectoryItem('SPY - CIA - KGB', 'movies&url=spy', 'spy.png', 'playlist.jpg')
		self.addDirectoryItem('Star Wars', 'movies&url=star', 'starwars.png', 'playlist.jpg')
		self.addDirectoryItem('Steampunk', 'movies&url=steampunk', 'steampunk.png', 'playlist.jpg')
		self.addDirectoryItem('Superheros', 'movies&url=superhero', 'superhero.png', 'playlist.jpg')
		self.addDirectoryItem('Supernatural', 'movies&url=supernatural', 'super.png', 'playlist.jpg')
		self.addDirectoryItem('Tarantino Films', 'movies&url=tarantino', 'tino.png', 'playlist.jpg')
		self.addDirectoryItem('Tech Noir', 'movies&url=tech', 'tech.png', 'playlist.jpg')
		self.addDirectoryItem('Teenage', 'movies&url=teen', 'teen.png', 'playlist.jpg')
		self.addDirectoryItem('Time Travel', 'movies&url=time', 'time.png', 'playlist.jpg')
		self.addDirectoryItem('Twist Ending Movies', 'movies&url=twist', 'twist.png', 'playlist.jpg')
		self.addDirectoryItem('Virtual Reality', 'movies&url=vr', 'vr.png', 'playlist.jpg')

		self.endDirectory()

	def movieMosts(self):
		self.addDirectoryItem('Most Played This Week', 'movies&url=played1', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Played This Month', 'movies&url=played2', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Played This Year', 'movies&url=played3', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Played All Time', 'movies&url=played4', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Collected This Week', 'movies&url=collected1', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Collected This Month', 'movies&url=collected2', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Collected This Year', 'movies&url=collected3', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Collected All Time', 'movies&url=collected4', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Watched This Week', 'movies&url=watched1', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Watched This Month', 'movies&url=watched2', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Watched This Year', 'movies&url=watched3', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Watched All Time', 'movies&url=watched4', 'trakt.png', 'playlist.jpg')

		self.endDirectory()

	def showMosts(self):
		self.addDirectoryItem('Most Played This Week', 'tvshows&url=played1', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Played This Month', 'tvshows&url=played2', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Played This Year', 'tvshows&url=played3', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Played All Time', 'tvshows&url=played4', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Collected This Week', 'tvshows&url=collected1', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Collected This Month', 'tvshows&url=collected2', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Collected This Year', 'tvshows&url=collected3', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Collected All Time', 'tvshows&url=collected4', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Watched This Week', 'tvshows&url=watched1', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Watched This Month', 'tvshows&url=watched2', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Watched This Year', 'tvshows&url=watched3', 'trakt.png', 'playlist.jpg')
		self.addDirectoryItem('Most Watched All Time', 'tvshows&url=watched4', 'trakt.png', 'playlist.jpg')

		self.endDirectory()

	def imdbtop250(self):
		self.addDirectoryItem('Top 250 All Time', 'movies&url=topgreatest', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Action', 'movies&url=topaction', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Adventure', 'movies&url=topadventure', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Animation', 'movies&url=topanimation', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Comedy', 'movies&url=topcomedy', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Crime', 'movies&url=topcrime', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Documentaries', 'movies&url=topdocumentary', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Drama', 'movies&url=topdrama', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Family', 'movies&url=topfamily', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Fantasy', 'movies&url=topfantasy', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 History', 'movies&url=tophistory', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Horror', 'movies&url=tophorror', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Music', 'movies&url=topmusic', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Mystery', 'movies&url=topmystery', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Romance', 'movies&url=topromance', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Sci-Fi', 'movies&url=topsci_fi', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Sports', 'movies&url=topsport', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Thriller', 'movies&url=topthriller', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 War', 'movies&url=topwar', 'imdb.png', 'playlist.jpg')
		self.addDirectoryItem('Top 250 Western', 'movies&url=topwestern', 'imdb.png', 'playlist.jpg')
		self.endDirectory()		        