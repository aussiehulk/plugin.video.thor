# -*- coding: utf-8 -*-
"""
	Thor Add-on
"""

from sys import argv, exit as sysexit
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
		self.highlight_color = control.getHighlightColor()

	def root(self):
		self.addDirectoryItem(33046, 'movieNavigator', 'movies.png', 'DefaultMovies.png')
		self.addDirectoryItem(33047, 'tvNavigator', 'tvshows.png', 'DefaultTVShows.png')
		if control.getMenuEnabled('navi.anime'): self.addDirectoryItem('Anime', 'anime_Navigator', 'boxsets.png', 'DefaultFolder.png')
		if control.getMenuEnabled('mylists.widget'):
			self.addDirectoryItem(32003, 'mymovieNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')
			self.addDirectoryItem(32004, 'mytvNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')
		if control.setting('furk.api') != '' and control.getMenuEnabled('navi.furk') : self.addDirectoryItem('Furk.net', 'furkNavigator', 'movies.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.trakt.popularList'):
			self.addDirectoryItem(32417, 'movies_PublicLists&url=trakt_popularLists', 'trakt.png' if self.iconLogos else 'trakt.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.imdblist') == True:
			self.addDirectoryItem(90451, 'imdblist', 'imdb.png', 'Defaultmovies.png')			
		if control.getMenuEnabled('navi.imdbtop250') == True:
			self.addDirectoryItem(90313, 'imdbtop250', 'imdb.png', 'Defaultmovies.png')
		if control.getMenuEnabled('navi.hodgepodge') == True:
			self.addDirectoryItem(90314, 'hodgepodge', 'hodgepodge.png', 'Defaultmovies.png')			
		if control.getMenuEnabled('navi.youtube'):
			self.addDirectoryItem(41002, 'youtube', 'youtube.png', 'youtube.png')
		self.addDirectoryItem(32010, 'tools_searchNavigator', 'search.png', 'DefaultAddonsSearch.png')
		self.addDirectoryItem(32008, 'tools_toolNavigator', 'tools.png', 'tools.png')
		downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
		if downloads: self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')
		if control.getMenuEnabled('navi.prem.services'): self.addDirectoryItem(90450, 'premiumNavigator', 'premium.png', 'DefaultFolder.png')
		if control.getMenuEnabled('navi.news'): self.addDirectoryItem(32013, 'tools_ShowNews', 'icon.png', 'DefaultAddonHelper.png', isFolder=False)
		if control.getMenuEnabled('navi.changelog'): self.addDirectoryItem(32014, 'tools_ShowChangelog&name=Thor', 'icon.png', 'DefaultAddonHelper.png', isFolder=False)
		self.endDirectory()

	def furk(self):
		self.addDirectoryItem('User Files', 'furkUserFiles', 'userlists.png', 'DefaultVideoPlaylists.png')
		self.addDirectoryItem('Search', 'furkSearch', 'search.png', 'search.png')
		self.endDirectory()

	def movies(self, lite=False):
		if control.getMenuEnabled('navi.movie.imdb.intheater'):
			self.addDirectoryItem(32421 if self.indexLabels else 32420, 'movies&url=theaters', 'imdb.png' if self.iconLogos else 'in-theaters.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.tmdb.nowplaying'):
			self.addDirectoryItem(32423 if self.indexLabels else 32422, 'tmdbmovies&url=tmdb_nowplaying', 'tmdb.png' if self.iconLogos else 'in-theaters.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.imdb.comingsoon'):
			self.addDirectoryItem(32215 if self.indexLabels else 32214, 'movies&url=imdb_comingsoon', 'imdb.png' if self.iconLogos else 'in-theaters.png', 'DefaultMovies.png')
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
			self.addDirectoryItem(32443 if self.indexLabels else 32442, 'movies&url=trakttrending', 'trakt.png' if self.iconLogos else 'trending.png', 'trending.png')
		if control.getMenuEnabled('navi.movie.trakt.recommended'):
			self.addDirectoryItem(32445 if self.indexLabels else 32444, 'movies&url=traktrecommendations', 'trakt.png' if self.iconLogos else 'highly-rated.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.imdb.featured'):
			self.addDirectoryItem(32447 if self.indexLabels else 32446, 'movies&url=featured', 'imdb.png' if self.iconLogos else 'movies.png', 'movies.png')
		if control.getMenuEnabled('navi.movie.imdb.oscarwinners'):
			self.addDirectoryItem(32452 if self.indexLabels else 32451, 'movies&url=oscars', 'imdb.png' if self.iconLogos else 'oscar-winners.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.imdb.oscarnominees'):
			self.addDirectoryItem(32454 if self.indexLabels else 32453, 'movies&url=oscarsnominees', 'imdb.png' if self.iconLogos else 'oscar-winners.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.imdb.genres'):
			self.addDirectoryItem(32456 if self.indexLabels else 32455, 'movieGenres&url=genre', 'imdb.png' if self.iconLogos else 'genres.png', 'DefaultGenre.png')
		if control.getMenuEnabled('navi.movie.tmdb.genres'):
			self.addDirectoryItem(32486 if self.indexLabels else 32455, 'movieGenres&url=tmdb_genre', 'tmdb.png' if self.iconLogos else 'genres.png', 'DefaultGenre.png')
		if control.getMenuEnabled('navi.movie.imdb.years'):
			self.addDirectoryItem(32458 if self.indexLabels else 32457, 'movieYears&url=year', 'imdb.png' if self.iconLogos else 'years.png', 'DefaultYear.png')
		if control.getMenuEnabled('navi.movie.tmdb.years'):
			self.addDirectoryItem(32485 if self.indexLabels else 32457, 'movieYears&url=tmdb_year', 'tmdb.png' if self.iconLogos else 'years.png', 'DefaultYear.png')
		if control.getMenuEnabled('navi.movie.imdb.people'):
			self.addDirectoryItem(32460 if self.indexLabels else 32459, 'moviePersons', 'imdb.png' if self.iconLogos else 'people.png', 'DefaultActor.png')
		if control.getMenuEnabled('navi.movie.imdb.languages'):
			self.addDirectoryItem(32462 if self.indexLabels else 32461, 'movieLanguages', 'imdb.png' if self.iconLogos else 'languages.png', 'DefaultAddonLanguage.png')
		if control.getMenuEnabled('navi.movie.imdb.certificates'):
			self.addDirectoryItem(32464 if self.indexLabels else 32463, 'movieCertificates&url=certification', 'imdb.png' if self.iconLogos else 'certificates.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.tmdb.certificates'):
			self.addDirectoryItem(32487 if self.indexLabels else 32463, 'movieCertificates&url=tmdb_certification', 'tmdb.png' if self.iconLogos else 'certificates.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.collections'):
			self.addDirectoryItem(32000, 'collections_Navigator', 'boxsets.png', 'DefaultSets.png')
		if control.getMenuEnabled('navi.movie.trakt.popularList'):
			self.addDirectoryItem(32417, 'movies_PublicLists&url=trakt_popularLists', 'trakt.png' if self.iconLogos else 'movies.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.trakt.trendingList'):
			self.addDirectoryItem(32418, 'movies_PublicLists&url=trakt_trendingLists', 'trakt.png' if self.iconLogos else 'movies.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.movie.trakt.searchList'):
			self.addDirectoryItem(32419, 'movies_SearchLists&media_type=movies', 'trakt.png' if self.iconLogos else 'movies.png', 'DefaultMovies.png', isFolder=False)
		if not lite:
			if control.getMenuEnabled('mylists.widget'): self.addDirectoryItem(32003, 'mymovieliteNavigator', 'mymovies.png', 'DefaultMovies.png')
			self.addDirectoryItem(33044, 'moviePerson', 'imdb.png' if self.iconLogos else 'people-search.png', 'DefaultAddonsSearch.png', isFolder=False)
			self.addDirectoryItem(33042, 'movieSearch', 'trakt.png' if self.iconLogos else 'search.png', 'DefaultAddonsSearch.png')
		self.endDirectory()

	def mymovies(self, lite=False):
		self.accountCheck()
		self.addDirectoryItem(32039, 'movieUserlists', 'userlists.png', 'DefaultVideoPlaylists.png')
		if self.traktCredentials:
			if self.traktIndicators:
				self.addDirectoryItem(35308, 'movies&url=traktunfinished', 'trakt.png', 'trakt.png', queue=True)
				self.addDirectoryItem(32036, 'movies&url=trakthistory', 'trakt.png', 'trakt.png', queue=True)
			self.addDirectoryItem(32683, 'movies&url=traktwatchlist', 'trakt.png', 'trakt.png', queue=True, context=(32551, 'library_moviesToLibrary&url=traktwatchlist&name=traktwatchlist'))
			self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'trakt.png', queue=True, context=(32551, 'library_moviesToLibrary&url=traktcollection&name=traktcollection'))
			self.addDirectoryItem(90453, 'movies_LikedLists', 'trakt.png', 'trakt.png', queue=True)
		if self.imdbCredentials: self.addDirectoryItem(32682, 'movies&url=imdbwatchlist', 'imdb.png', 'imdb.png', queue=True)
		if not lite:
			self.addDirectoryItem(32031, 'movieliteNavigator', 'movies.png', 'DefaultMovies.png')
			self.addDirectoryItem(33044, 'moviePerson', 'imdb.png' if self.iconLogos else 'people-search.png', 'DefaultAddonsSearch.png', isFolder=False)
			self.addDirectoryItem(33042, 'movieSearch', 'search.png' if self.iconLogos else 'search.png', 'DefaultAddonsSearch.png')
		self.endDirectory()

	def tvshows(self, lite=False):
		if control.getMenuEnabled('navi.originals'):
			self.addDirectoryItem(40077 if self.indexLabels else 40070, 'tvOriginals', 'tvmaze.png' if self.iconLogos else 'networks.png', 'DefaultNetwork.png')
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
			self.addDirectoryItem(32456 if self.indexLabels else 32455, 'tvGenres&url=genre', 'imdb.png' if self.iconLogos else 'genres.png', 'DefaultGenre.png')
		if control.getMenuEnabled('navi.tv.tmdb.genres'):
			self.addDirectoryItem(32486 if self.indexLabels else 32455, 'tvGenres&url=tmdb_genre', 'tmdb.png' if self.iconLogos else 'genres.png', 'DefaultGenre.png')
		if control.getMenuEnabled('navi.tv.tvmaze.networks'):
			self.addDirectoryItem(32468 if self.indexLabels else 32469, 'tvNetworks', 'tmdb.png' if self.iconLogos else 'networks.png', 'DefaultNetwork.png')
		if control.getMenuEnabled('navi.tv.imdb.languages'):
			self.addDirectoryItem(32462 if self.indexLabels else 32461, 'tvLanguages', 'imdb.png' if self.iconLogos else 'languages.png', 'DefaultAddonLanguage.png')
		if control.getMenuEnabled('navi.tv.imdb.certificates'):
			self.addDirectoryItem(32464 if self.indexLabels else 32463, 'tvCertificates', 'imdb.png' if self.iconLogos else 'certificates.png', 'DefaultTVShows.png')
		# if control.getMenuEnabled('navi.tv.tmdb.certificates'):
		if control.getMenuEnabled('navi.tv.imdb.years'):
			self.addDirectoryItem(32458 if self.indexLabels else 32457, 'tvYears&url=year', 'imdb.png' if self.iconLogos else 'years.png', 'DefaultYear.png')
		if control.getMenuEnabled('navi.tv.tmdb.years'):
			self.addDirectoryItem(32485 if self.indexLabels else 32457, 'tvYears&url=tmdb_year', 'tmdb.png' if self.iconLogos else 'years.png', 'DefaultYear.png')
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
		if control.getMenuEnabled('navi.tv.trakt.popularList'):
			self.addDirectoryItem(32417, 'tv_PublicLists&url=trakt_popularLists', 'trakt.png' if self.iconLogos else 'tvshows.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.tv.trakt.trendingList'):
			self.addDirectoryItem(32418, 'tv_PublicLists&url=trakt_trendingLists', 'trakt.png' if self.iconLogos else 'tvshows.png', 'DefaultMovies.png')
		if control.getMenuEnabled('navi.tv.trakt.searchList'):
			self.addDirectoryItem(32419, 'tv_SearchLists&media_type=shows', 'trakt.png' if self.iconLogos else 'tvshows.png', 'DefaultMovies.png', isFolder=False)
		if not lite:
			if control.getMenuEnabled('mylists.widget'): self.addDirectoryItem(32004, 'mytvliteNavigator', 'mytvshows.png', 'DefaultTVShows.png')
			self.addDirectoryItem(33045, 'tvPerson', 'imdb.png' if self.iconLogos else 'people-search.png', 'DefaultAddonsSearch.png', isFolder=False)
			self.addDirectoryItem(33043, 'tvSearch', 'trakt.png' if self.iconLogos else 'search.png', 'DefaultAddonsSearch.png')
		self.endDirectory()

	def mytvshows(self, lite=False):
		self.accountCheck()
		self.addDirectoryItem(32040, 'tvUserlists', 'userlists.png', 'DefaultVideoPlaylists.png')
		if self.traktCredentials:
			if self.traktIndicators:
				self.addDirectoryItem(35308, 'episodesUnfinished&url=traktunfinished', 'trakt.png', 'trakt.png', queue=True)
				self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.png', 'trakt.png', queue=True)
				self.addDirectoryItem(32019, 'upcomingProgress&url=progress', 'trakt.png', 'trakt.png', queue=True)
				self.addDirectoryItem(32202, 'calendar&url=mycalendarRecent', 'trakt.png', 'trakt.png', queue=True)
				self.addDirectoryItem(32203, 'calendar&url=mycalendarUpcoming', 'trakt.png', 'trakt.png', queue=True)
				self.addDirectoryItem(32204, 'calendar&url=mycalendarPremiers', 'trakt.png', 'trakt.png', queue=True)
				self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.png', 'trakt.png', queue=True)
			self.addDirectoryItem(32683, 'tvshows&url=traktwatchlist', 'trakt.png', 'trakt.png', context=(32551, 'library_tvshowsToLibrary&url=traktwatchlist&name=traktwatchlist'))
			self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'trakt.png', context=(32551, 'library_tvshowsToLibrary&url=traktcollection&name=traktcollection'))
			self.addDirectoryItem(90453, 'shows_LikedLists', 'trakt.png', 'trakt.png', queue=True)
		if self.imdbCredentials: self.addDirectoryItem(32682, 'tvshows&url=imdbwatchlist', 'imdb.png', 'imdb.png')
		if not lite:
			self.addDirectoryItem(32031, 'tvliteNavigator', 'tvshows.png', 'DefaultTVShows.png')
			self.addDirectoryItem(33045, 'tvPerson', 'imdb.png' if self.iconLogos else 'people-search.png', 'DefaultAddonsSearch.png', isFolder=False)
			self.addDirectoryItem(33043, 'tvSearch', 'trakt.png' if self.iconLogos else 'search.png', 'DefaultAddonsSearch.png')
		self.endDirectory()

	def anime(self, lite=False):
		self.addDirectoryItem(32001, 'anime_Movies&url=anime', 'movies.png', 'DefaultMovies.png')
		self.addDirectoryItem(32002, 'anime_TVshows&url=anime', 'tvshows.png', 'DefaultTVShows.png')
		self.endDirectory()

	def traktSearchLists(self, media_type):
		k = control.keyboard('', control.lang(32010))
		k.doModal()
		q = k.getText() if k.isConfirmed() else None
		if not q: return control.closeAll()
		page_limit = control.setting('page.item.limit')
		url = 'https://api.trakt.tv/search/list?limit=%s&page=1&query=' % page_limit + quote_plus(q)
		control.closeAll()
		if media_type == 'movies':
			control.execute('ActivateWindow(Videos,plugin://plugin.video.thor/?action=movies_PublicLists&url=%s,return)' % (quote_plus(url)))
		else:
			control.execute('ActivateWindow(Videos,plugin://plugin.video.thor/?action=tv_PublicLists&url=%s,return)' % (quote_plus(url)))

	def tools(self):
		if self.traktCredentials: self.addDirectoryItem(35057, 'tools_traktToolsNavigator', 'tools.png', 'DefaultAddonService.png', isFolder=True)
		self.addDirectoryItem(32510, 'cache_Navigator', 'tools.png', 'DefaultAddonService.png', isFolder=True)
		self.addDirectoryItem(32609, 'tools_openMyAccount', 'MyAccounts.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(32506, 'tools_contextThorSettings', 'icon.png', 'DefaultAddonProgram.png', isFolder=False)
		#-- Providers - 4
		self.addDirectoryItem(32651, 'tools_fenomscrapersSettings', 'fenomscrapers.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(32523, 'tools_loggingNavigator', 'tools.png', 'DefaultAddonService.png')
		self.addDirectoryItem(32083, 'tools_cleanSettings', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
		#-- General - 0
		self.addDirectoryItem(32043, 'tools_openSettings&query=0.0', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		#-- Navigation - 1
		self.addDirectoryItem(32362, 'tools_openSettings&query=1.1', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		#-- Playback - 3
		self.addDirectoryItem(32045, 'tools_openSettings&query=3.1', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		#-- Accounts - 7
		self.addDirectoryItem(32044, 'tools_openSettings&query=7.0', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		#-- Downloads - 10
		self.addDirectoryItem(32048, 'tools_openSettings&query=10.0', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		#-- Subtitles - 11
		self.addDirectoryItem(32046, 'tools_openSettings&query=11.0', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(32556, 'library_Navigator', 'tools.png', 'DefaultAddonService.png', isFolder=True)
		self.addDirectoryItem(32049, 'tools_viewsNavigator', 'tools.png', 'DefaultAddonService.png', isFolder=True)
		self.addDirectoryItem(32361, 'tools_resetViewTypes', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.endDirectory()

	def traktTools(self):
		self.addDirectoryItem(35058, 'shows_traktHiddenManager', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(35059, 'movies_traktUnfinishedManager', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(35060, 'episodes_traktUnfinishedManager', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(35061, 'movies_traktWatchListManager', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(35062, 'shows_traktWatchListManager', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(35063, 'movies_traktCollectionManager', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(35064, 'shows_traktCollectionManager', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(35065, 'tools_traktLikedListManager', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.addDirectoryItem(35066, 'tools_forceTraktSync', 'tools.png', 'DefaultAddonService.png', isFolder=False)
		self.endDirectory()

	def loggingNavigator(self):
		self.addDirectoryItem(32524, 'tools_viewLogFile&name=Thor', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
		self.addDirectoryItem(32525, 'tools_clearLogFile', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
		self.addDirectoryItem(32526, 'tools_ShowChangelog&name=Thor', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
		self.addDirectoryItem(32527, 'tools_uploadLogFile&name=Thor', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
		self.addDirectoryItem(32528, 'tools_viewLogFile&name=MyAccounts', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
		self.addDirectoryItem(32529, 'tools_ShowChangelog&name=MyAccounts', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
		self.addDirectoryItem(32530, 'tools_viewLogFile&name=FenomScrapers', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
		self.addDirectoryItem(32531, 'tools_ShowChangelog&name=FenomScrapers', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
		self.addDirectoryItem(32532, 'tools_viewLogFile&name=Kodi', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
		self.addDirectoryItem(32198, 'tools_uploadLogFile&name=Kodi', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
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
	# -- Library - 9
		self.addDirectoryItem(32557, 'tools_openSettings&query=9.0', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
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
		self.addDirectoryItem(40059, 'ad_ServiceNavigator', 'alldebrid.png', 'alldebrid.png')
		self.addDirectoryItem(40057, 'pm_ServiceNavigator', 'premiumize.png', 'premiumize.png')
		self.addDirectoryItem(40058, 'rd_ServiceNavigator', 'realdebrid.png', 'realdebrid.png')
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
		self.addDirectoryItem(33042, 'movieSearch', 'trakt.png' if self.iconLogos else 'search.png', 'DefaultAddonsSearch.png')
		self.addDirectoryItem(33043, 'tvSearch', 'trakt.png' if self.iconLogos else 'search.png', 'DefaultAddonsSearch.png')
		self.addDirectoryItem(33044, 'moviePerson', 'imdb.png' if self.iconLogos else 'people-search.png', 'DefaultAddonsSearch.png', isFolder=False)
		self.addDirectoryItem(33045, 'tvPerson', 'imdb.png' if self.iconLogos else 'people-search.png', 'DefaultAddonsSearch.png', isFolder=False)
		self.endDirectory()

	def views(self):
		try:
			syshandle = int(argv[1])
			control.hide()
			items = [(control.lang(32001), 'movies'), (control.lang(32002), 'tvshows'), (control.lang(32054), 'seasons'), (control.lang(32326), 'episodes') ]
			select = control.selectDialog([i[0] for i in items], control.lang(32049))
			if select == -1: return
			content = items[select][1]
			title = control.lang(32059)
			url = '%s?action=tools_addView&content=%s' % (argv[0], content)
			poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()
			item = control.item(label=title, offscreen=True)
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
			if cache_clear_all(): control.notification(message=32089)
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

	def clearMetaAndCache(self):
		control.hide()
		if not control.yesnoDialog(control.lang(35531), '', ''): return
		try:
			def cache_clear_both():
				try:
					from resources.lib.database import cache, metacache
					metacache.cache_clear_meta()
					cache.cache_clear()
					return True
				except:
					from resources.lib.modules import log_utils
					log_utils.error()
			if cache_clear_both():
				control.notification(message=35532)
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

	def addDirectoryItem(self, name, query, poster, icon, context=None, queue=False, isAction=True, isFolder=True, isPlayable=False, isSearch=False, table=''):
		try:
			sysaddon = argv[0] ; syshandle = int(argv[1])
			if isinstance(name, int): name = control.lang(name)
			url = '%s?action=%s' % (sysaddon, query) if isAction else query
			poster = control.joinPath(self.artPath, poster) if self.artPath else icon
			if not icon.startswith('Default'): icon = control.joinPath(self.artPath, icon)
			cm = []
			queueMenu = control.lang(32065)
			if queue: cm.append((queueMenu, 'RunPlugin(%s?action=playlist_QueueItem)' % sysaddon))
			if context: cm.append((control.lang(context[0]), 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))
			if isSearch: cm.append(('Clear Search Phrase', 'RunPlugin(%s?action=cache_clearSearchPhrase&source=%s&name=%s)' % (sysaddon, table, quote_plus(name))))
			cm.append(('[COLOR red]Thor Settings[/COLOR]', 'RunPlugin(%s?action=tools_openSettings)' % sysaddon))
			item = control.item(label=name, offscreen=True)
			item.addContextMenuItems(cm)
			if isPlayable: item.setProperty('IsPlayable', 'true')
			else: item.setProperty('IsPlayable', 'false')
			item.setArt({'icon': icon, 'poster': poster, 'thumb': poster, 'fanart': control.addonFanart(), 'banner': poster})
			item.setInfo(type='video', infoLabels={'plot': name})
			control.addItem(handle=syshandle, url=url, listitem=item, isFolder= isFolder)
		except:
			from resources.lib.modules import log_utils
			log_utils.error()

	def imdblist(self):

		self.addDirectoryItem(90085, 'movies&url=top100','imdb.png', 'DefaultMovies.png')
		self.addDirectoryItem(90086, 'movies&url=top250','imdb.png', 'DefaultMovies.png')
		self.addDirectoryItem(90087, 'movies&url=top1000','imdb.png', 'DefaultMovies.png')
		self.addDirectoryItem(90089, 'movies&url=rated_g','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90090, 'movies&url=rated_pg','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90091, 'movies&url=rated_pg13','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90092, 'movies&url=rated_r','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90093, 'movies&url=rated_nc17','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90088, 'movies&url=bestdirector','imdb.png', 'DefaultMovies.png')
		self.addDirectoryItem(90094, 'movies&url=national_film_board', 'imdb.png', 'DefaultMovies.png')
		self.addDirectoryItem(90100, 'movies&url=dreamworks_pictures', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90095, 'movies&url=fox_pictures','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90096, 'movies&url=paramount_pictures', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90097, 'movies&url=mgm_pictures','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90099, 'movies&url=universal_pictures', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90100, 'movies&url=sony_pictures','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90101, 'movies&url=warnerbrothers_pictures', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90102, 'movies&url=amazon_prime','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90098, 'movies&url=disney_pictures', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90138, 'movies&url=family_movies','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90103, 'movies&url=classic_movies','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90104, 'movies&url=classic_horror','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90105, 'movies&url=classic_fantasy', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90106, 'movies&url=classic_western', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90107, 'movies&url=classic_annimation', 'imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90108, 'movies&url=classic_war','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90109, 'movies&url=classic_scifi','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90110, 'movies&url=eighties','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90111, 'movies&url=nineties','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90112, 'movies&url=thousands','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90139, 'movies&url=twenty10','imdb.png', 'DefaultTVShows.png')
		self.addDirectoryItem(90452, 'movies&url=twenty20','imdb.png', 'DefaultTVShows.png')		

		self.endDirectory()

	def holidays(self):
		self.addDirectoryItem(90161, 'movies&url=top50_holiday', 'holidays.png', 'holidays.png')
		self.addDirectoryItem(90162, 'movies&url=best_holiday','holidays.png', 'holidays.png')
		self.addDirectoryItem(90158, 'movieUserlists&url=https://api.trakt.tv/users/movistapp/lists/christmas-movies/items?', 'holidays.png', 'holidays.png')
		self.addDirectoryItem(90159, 'movieUserlists&url=https://api.trakt.tv/users/cjcope/lists/hallmark-christmas/items?', 'holidays.png', 'holidays.png')
		self.addDirectoryItem(90160, 'movieUserlists&url=https://api.trakt.tv/users/mkadam68/lists/christmas-list/items?', 'holidays.png', 'holidays.png')

		self.endDirectory()

	def halloween(self):
		self.addDirectoryItem(90146, 'movies&url=halloween_imdb', 'halloween.png', 'halloween.png')
		self.addDirectoryItem(90147, 'movies&url=halloween_top_100', 'halloween.png', 'halloween.png')
		self.addDirectoryItem(90148, 'movies&url=halloween_best', 'halloween.png', 'halloween.png')
		self.addDirectoryItem(90149, 'movies&url=halloween_great', 'halloween.png', 'halloween.png')
		self.addDirectoryItem(90145, 'movieUserlists&url=https://api.trakt.tv/users/petermesh/lists/halloween-movies/items?', 'halloween.png', 'halloween.png')

		self.endDirectory()

	def hodgepodge(self):
		self.addDirectoryItem('Films that are mostly taking place in one room', 'movies&url=imdb1', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Movies Based On True Story', 'movies&url=imdb2', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Best Movies Set in the 60s', 'movies&url=imdb3', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('80s Movies', 'movies&url=imdb4', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Movies from the 80s you DIDNT know you should watch before you die.', 'movies&url=imdb5', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('100 Best Action Movies of All Time', 'movies&url=imdb6', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Best of 80s, 90s, 00s Action', 'movies&url=imdb7', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Top 250 Action Movies', 'movies&url=imdb8', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Adventure-Fantasy Films 1970 to 1996', 'movies&url=imdb9', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Great Kids Adventures Movies', 'movies&url=imdb10', 'hodgepodge.png', 'hodgepodge.png')  # start
		self.addDirectoryItem('Movies dealing in some way with the afterlife', 'movies&url=imdb11', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Against All Odds - Survival of the fittest', 'movies&url=imdb12', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Agoraphobia ( Fear of going Outside )', 'movies&url=imdb13', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Airplane Movies', 'movies&url=imdb14', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Alien Life: Friendly aliens movies', 'movies&url=imdb15', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Aliens: Movies with Aliens', 'movies&url=imdb16', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Angels In Movies', 'movies&url=imdb17', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Animation: Best Achievements in Animation', 'movies&url=imdb18', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Anime/Animated', 'movies&url=imdb19', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Archery: Movies involving archery', 'movies&url=imdb20', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Atmospheric Movies', 'movies&url=imdb21', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Australian Summer', 'movies&url=imdb22', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Aviation: Pilots, Flight Attendants, Airports or Planes', 'movies&url=imdb23', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Awesome movies with a child/teenager in the leading role', 'movies&url=imdb24', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('B-Movies: 80s 90s Sci-Fi & B-movies', 'movies&url=imdb25', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Bad Guy Wins', 'movies&url=imdb26', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Bad Luck - Characters Down on Their Luck', 'movies&url=imdb27', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('BANNED: Video Nasties, The Complete 72 Banned UK Titles List', 'movies&url=imdb28', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Baseball Movies', 'movies&url=imdb29', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Before They were famous', 'movies&url=imdb30', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Best Buddies Movies', 'movies&url=imdb31', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Best Conspiracy Thrillers', 'movies&url=imdb32', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Best films about Civil Rights / Racism', 'movies&url=imdb33', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Best Movie Remakes of All Time', 'movies&url=imdb34', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Best of Jackie Chan', 'movies&url=imdb35', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Best Opening Scenes In Movies', 'movies&url=imdb36', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Best Special Effects in Movies', 'movies&url=imdb37', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Best Teen Movies of All Time', 'movies&url=imdb38', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Biggest names among movies: the huge, the classic and the beautiful', 'movies&url=imdb39', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Biography: The Best Biographical Films', 'movies&url=imdb40', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Biopic: Top 50 Greatest Biopics of All Time', 'movies&url=imdb41', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Blaxploitation Movies - Greatest Ones', 'movies&url=imdb42', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Body Switch Movies', 'movies&url=imdb43', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Boogeyman in Movies', 'movies&url=imdb44', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Book: A list of Movies Based on Books', 'movies&url=imdb45', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Bullying in Movies', 'movies&url=imdb46', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Campy Movies!', 'movies&url=imdb47', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Cartoons', 'movies&url=imdb48', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Chased/Sought after', 'movies&url=imdb49', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Cheesy love / drama / sad movies', 'movies&url=imdb50', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Christmas Movies', 'movies&url=imdb51', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Cities: Movies where the city is practically a character', 'movies&url=imdb52', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Clever Movies', 'movies&url=imdb53', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Clones Movies And Shows', 'movies&url=imdb54', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Coen Brothers Filmography', 'movies&url=imdb55', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('The 100 Best Comedies of the 80s', 'movies&url=imdb56', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Top 200 Comedy Movies', 'movies&url=imdb57', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Comfy, cozy, chamber movies', 'movies&url=imdb58', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Coming of age: The Ultimate list', 'movies&url=imdb59', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Confessions, Diaries, Or Both', 'movies&url=imdb60', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Cops', 'movies&url=imdb61', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Cops: Dirty Cop Movies', 'movies&url=imdb62', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Cozy Winter Movies', 'movies&url=imdb63', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Crime Shows/Documentaries', 'movies&url=imdb64', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Crime: Best Crime Movies:The Ultimate List', 'movies&url=imdb65', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Cruise Ships Movies', 'movies&url=imdb66', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Cult: The Ultimate Cult Movie List', 'movies&url=imdb67', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Cyberpunk', 'movies&url=imdb68', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Dance movies / great list of dance movies', 'movies&url=imdb69', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Dark and Gritty Movies', 'movies&url=imdb70', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Dark Comedies', 'movies&url=imdb71', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Desert themed movies', 'movies&url=imdb72', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Detectives: Best Detective Films and TV series:The Ultimate List', 'movies&url=imdb73', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Direct to Video Movies That Are Actually Great', 'movies&url=imdb74', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Disaster Movies. Huge list of disaster movies', 'movies&url=imdb75', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Disney Movies - Animated', 'movies&url=imdb76', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Disney: Every Disney Movies', 'movies&url=imdb77', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Disorder: Movies about physical disability', 'movies&url=imdb78', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Disorder: Movies Depicting Mental Disorders', 'movies&url=imdb79', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Disorder: Movies with main characters that are blind', 'movies&url=imdb80', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Disorder:Brain Powers', 'movies&url=imdb81', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Disorder: The best movies about INSANITY', 'movies&url=imdb82', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Dolls, Puppets, Dummies, Mannequins, Toys, and Marionettes', 'movies&url=imdb83', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Drugs: Modern Films & TV Shows About Drugs/Pharmaceuticals', 'movies&url=imdb84', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Ethnic: Must See Movies For Black Folks', 'movies&url=imdb85', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Ethnic: The Best hood movies', 'movies&url=imdb86', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Evil Kid Horror Movies', 'movies&url=imdb87', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Expedition Gone Wrong Movies', 'movies&url=imdb88', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Fairy Tale Movies', 'movies&url=imdb89', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Family: 100 best family movies ever for your children', 'movies&url=imdb90', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Fantasy: Some of the best fantasy kid movies ever', 'movies&url=imdb90', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Farms', 'movies&url=imdb91', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Feel Good Movies', 'movies&url=imdb92', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Fighting Movies', 'movies&url=imdb93', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Films with disfigured characters', 'movies&url=imdb94', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Food & Restaurant Movies', 'movies&url=imdb95', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Foreign: Some of the Best Foreign Films', 'movies&url=imdb96', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Found Footage Movies', 'movies&url=imdb97', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Frat Pack Movies', 'movies&url=imdb98', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Full list of comic based movies', 'movies&url=imdb99', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Funny Movies of all sorts', 'movies&url=imdb100', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Futuristic Apocalypse Movies', 'movies&url=imdb101', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Futuristic: 200 futuristic apocalypse films', 'movies&url=imdb102', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Ghost Ship movies collection', 'movies&url=imdb103', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Ghosts: The best of Ghost Movies', 'movies&url=imdb104', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Great Soundtracks in Movies', 'movies&url=imdb105', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('GREATEST MOVIES: 2000-2017', 'movies&url=imdb106', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Hacking / Computer Geeks', 'movies&url=imdb107', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Halloween Themed Movies and Movies with Halloween Scenes', 'movies&url=imdb108', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('High School: Best High School Themed Movies', 'movies&url=imdb109', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Hillbillys, Rednecks & Hicks', 'movies&url=imdb110', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Hip-hop culture / racial discrimination and etc.', 'movies&url=imdb111', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Hipster Movies', 'movies&url=imdb112', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Hitmen: Great list of movies with Hitmen/Assassins', 'movies&url=imdb113', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Home Invasion movies', 'movies&url=imdb114', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Hood/Gangsters/Ghetto movies', 'movies&url=imdb115', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('horror flicks based on true story', 'movies&url=imdb116', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Horror Movies 2017', 'movies&url=imdb117', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Horror movies with awesome houses', 'movies&url=imdb118', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Horror: Best Horror Movies of the 2000s', 'movies&url=imdb119', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Horror: Cabins/Cottages', 'movies&url=imdb120', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Horror: Christmas Horror', 'movies&url=imdb121', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Horror: Creeps / Stalkers', 'movies&url=imdb122', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Horror: Haunted Houses - The Ultimate List', 'movies&url=imdb123', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Horror: Horror movies set in asylums/ mental hospitals', 'movies&url=imdb124', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Horror: Korean Horror Movies', 'movies&url=imdb125', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Horror: Redneck Horror Movies', 'movies&url=imdb126', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Horror: Slashers Horror', 'movies&url=imdb127', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Horror: Slow Burn Horror', 'movies&url=imdb128', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Horror: Underlooked Gems', 'movies&url=imdb129', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Horror: Winter-setting horror movies', 'movies&url=imdb130', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Imaginary friends', 'movies&url=imdb131', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Inspirational movies "BASED ON TRUE STORY"', 'movies&url=imdb132', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Island: Stranded on an Island', 'movies&url=imdb133', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Jack Nicholson - The Filmography', 'movies&url=imdb134', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('James Bond: The Complete Collection', 'movies&url=imdb135', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('James Wan', 'movies&url=imdb136', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('JcVd', 'movies&url=imdb137', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('John Hughes Movies', 'movies&url=imdb138', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Jump Scares', 'movies&url=imdb139', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Jungle: Movies taking place in jungles', 'movies&url=imdb140', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Kid-friendly "Halloween" movies & TV shows', 'movies&url=imdb141', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Kid/Teens Adventures', 'movies&url=imdb142', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Kidnapped or Hostage movies', 'movies&url=imdb143', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Killer bug movies', 'movies&url=imdb144', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Las Vegas: List of films set in Las Vegas', 'movies&url=imdb145', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Law: Great movies with lawyers', 'movies&url=imdb146', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Lesbian: Huge lesbian movies list', 'movies&url=imdb147', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Life Lessons: Movies with life lessons', 'movies&url=imdb148', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Lifetime Movies That Are Great', 'movies&url=imdb149', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Lighthouses: Movies set in a Lighthouse', 'movies&url=imdb150', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Live-Action Fairy Tale Movies', 'movies&url=imdb151', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Losers in Movies', 'movies&url=imdb152', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Mafia, Gangsters, Mob Movies', 'movies&url=imdb153', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Magic: Movies and Shows About Magic', 'movies&url=imdb154', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Martial Arts: Awesome Martial Arts Movies!', 'movies&url=imdb155', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Martial Arts: The Top 250 Greatest Martial Arts Movies of All-Time', 'movies&url=imdb156', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Medieval Movies', 'movies&url=imdb157', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Medieval: Films set in the Middle Ages', 'movies&url=imdb158', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Mel Brooks Movies', 'movies&url=imdb159', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Military: 54 MOVIES INVOLVING MILITARY TRAINING', 'movies&url=imdb160', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Missing Person/People movie', 'movies&url=imdb161', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Modern (1990s-Now) Films That are Set in the 1970s', 'movies&url=imdb162', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Modern People in Historical Setting or Historical/Ancient', 'movies&url=imdb163', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Modern Westerns', 'movies&url=imdb163', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Monsters: Movies featuring monsters', 'movies&url=imdb165', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Moon: Top 10 Moon Movies', 'movies&url=imdb166', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Movies for High School Girls', 'movies&url=imdb167', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Movies inside a Video-Game', 'movies&url=imdb168', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Movies involving Portrayals of Real Life Teachers', 'movies&url=imdb169', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Movies set in San Francisco/ Bay Area', 'movies&url=imdb170', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Movies similar to the burbs', 'movies&url=imdb171', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Movies that keep you guessing until the end', 'movies&url=imdb172', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Movies that switch Genres halfway through', 'movies&url=imdb173', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Movies That Take Place In A Single Day', 'movies&url=imdb174', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Movies To Watch On a Rainy Day', 'movies&url=imdb175', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Movies with great aesthetics', 'movies&url=imdb176', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Movies written, directed and starring the same person', 'movies&url=imdb177', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Music: LIST OF 356 FILMS ABOUT OR INVOLVING MUSICIANS', 'movies&url=imdb178', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Must See World War II Documentaries', 'movies&url=imdb179', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Mystery Movies set in Castles and Mansions', 'movies&url=imdb180', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Narrated Movies', 'movies&url=imdb181', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('National Lampoon Marathon!', 'movies&url=imdb182', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Nature Documentaries!', 'movies&url=imdb183', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Nature: Man vs. Nature/Animal movies', 'movies&url=imdb184', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Nature: Scuba / Underwater / Diving', 'movies&url=imdb185', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Noir: 100 Best Film-Noir movies', 'movies&url=imdb186', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Nostalgia Inducing Movies For People In Their Mid 20s 30s', 'movies&url=imdb187', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Ocean Adventure', 'movies&url=imdb188', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('One Man Army', 'movies&url=imdb189', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Outer Space movies/Great Space Exploration', 'movies&url=imdb190', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Parallel stories ', 'movies&url=imdb191', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Paul Verhoeven Movies', 'movies&url=imdb192', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Plot Twists In Movies', 'movies&url=imdb193', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Politics: 150 FILMS', 'movies&url=imdb194', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Post-Apocalyptic Movies', 'movies&url=imdb195', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Prison-Jail Movies', 'movies&url=imdb196', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Psychological Thrillers', 'movies&url=imdb197', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Psychologists/Psychiatrists/Therapists', 'movies&url=imdb198', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Psychosexual thrillers', 'movies&url=imdb199', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Quotable: Top 50 Most Quotable Movies Ever', 'movies&url=imdb200', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('R rated superhero movies', 'movies&url=imdb201', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Rape & Revenge', 'movies&url=imdb202', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Really Long Movies', 'movies&url=imdb203', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Reddit - Films Before You Die', 'movies&url=imdb204', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Revenge & Vigilante Movies', 'movies&url=imdb205', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Road Trips - Travels', 'movies&url=imdb206', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Robbery / Heist Movies', 'movies&url=imdb207', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Robot Movies', 'movies&url=imdb208', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Romance: Best romance in movies', 'movies&url=imdb209', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Romance: Bromance in Movies', 'movies&url=imdb210', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Romance: Forbidden Love in Movies', 'movies&url=imdb211', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Romance: Unconventional Romance Films', 'movies&url=imdb212', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Saddest Movies - Movies That Will Make You Cry', 'movies&url=imdb213', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Sailing & Seamanship Movies', 'movies&url=imdb214', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Sam Rockwell Movies', 'movies&url=imdb215', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Sci-Fi Based on Books, Short Stories, or Graphic Novels', 'movies&url=imdb216', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Sci-Fi: The Truly Ultimate Sci-Fi List: 1902-2015', 'movies&url=imdb217', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Sequels: 30 Great Sequels', 'movies&url=imdb218', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Serial Killer Movies', 'movies&url=imdb219', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Sharks, Sharks and Sharks!', 'movies&url=imdb220', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Sniper Movies', 'movies&url=imdb221', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Social Network: Movies ', 'movies&url=imdb222', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Some of The Best Military movies of all time', 'movies&url=imdb223', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Some Of The Most Inventive and Creative', 'movies&url=imdb224', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Spies: Best Spy Movies:The Ultimate List', 'movies&url=imdb225', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Steampunk', 'movies&url=imdb226', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Stephen King: Real Stephen King Movies / Adaptions', 'movies&url=imdb227', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Steven Spielberg Feature Filmography', 'movies&url=imdb228', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Strippers: Movies Featuring Strippers', 'movies&url=imdb229', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Submarines', 'movies&url=imdb230', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Suburban Nostalgia, Spider-Man, Superman, Avengers', 'movies&url=imdb231', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Super Hero Films, Superman, Avengers', 'movies&url=imdb232', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Surfing: Movies about surfing', 'movies&url=imdb233', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Tarantino-Esque Movies: THE ULTIMATE LIST', 'movies&url=imdb234', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('The Best Non Animated Children, Teen and Family Movies of all Time', 'movies&url=imdb235', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('The best Vampire Movies!', 'movies&url=imdb236', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('The Criterion Collection', 'movies&url=imdb237', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('The Finest Fantasy: 25 Must-See Sword & Sorcery Films', 'movies&url=imdb237', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('The Girlfriends Corner', 'movies&url=imdb238', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('The Greatest Acting Performances of All Time', 'movies&url=imdb239', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('The One True God', 'movies&url=imdb240', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Time Travel Movies', 'movies&url=imdb241', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Top 100 Gore Films', 'movies&url=imdb242', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Top 240 Horror Movies 2000-2016', 'movies&url=imdb243', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Top50 World War II Movies', 'movies&url=imdb244', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Trapped Movies', 'movies&url=imdb245', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('TV: Live-Action TV Series Based on Comics', 'movies&url=imdb246', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('TV: Live-action TV series based on Marvel Comics', 'movies&url=imdb247', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Underdogs in Movies', 'movies&url=imdb248', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Vacations: 100+ Summer, Vacation, and Beach Movies', 'movies&url=imdb249', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Vampire and Werewolf Movies', 'movies&url=imdb250', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Victorian Era', 'movies&url=imdb251', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Video Games: Movies/Series involving video games', 'movies&url=imdb252', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Visually Striking - Good Cinematography', 'movies&url=imdb253', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('War: 1600+ War movies list', 'movies&url=imdb254', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('War: Top 25 Greatest War Movies of All Time', 'movies&url=imdb255', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Weather: Films Set in a Heat Wave', 'movies&url=imdb256', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Weed Movies', 'movies&url=imdb257', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Weird claustrophobic movies like Cube and Saw', 'movies&url=imdb258', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Westerns with HD releases', 'movies&url=imdb259', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Wilderness Survival Movies', 'movies&url=imdb260', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Winter and Snow Movies: The Ultimate List', 'movies&url=imdb261', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Witches: Best Witch Movies', 'movies&url=imdb262', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Worst Movies of All Time', 'movies&url=imdb263', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('WTF - Weird, fcked up , Bizzare etc', 'movies&url=imdb264', 'hodgepodge.png', 'hodgepodge.png')
		self.addDirectoryItem('Zombies: Definitive zombie list', 'movies&url=imdb265', 'hodgepodge.png', 'hodgepodge.png')

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

	def endDirectory(self):
		syshandle = int(argv[1])
		content = 'addons' if control.skin == 'skin.auramod' else ''
		control.content(syshandle, content) # some skins use their own thumb for things like "genres" when content type is set here
		control.directory(syshandle, cacheToDisc=True)