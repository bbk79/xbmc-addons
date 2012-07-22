import urllib,urllib2,re,os,cookielib
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup

addon = xbmcaddon.Addon('plugin.video.manoto')
profile = xbmc.translatePath(addon.getAddonInfo('profile'))


__settings__ = xbmcaddon.Addon(id='plugin.video.manoto')
__language__ = __settings__.getLocalizedString

home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))

listitem = xbmcgui.ListItem('Manoto 1 - Live')
listitem.setInfo('video', {'Title': 'Manoto 1 - Live', 'Genre': 'TV'})
listitem.setThumbnailImage(icon)
listitem.setProperty('IsLive', 'true')


if (__settings__.getSetting('username') == "") or (__settings__.getSetting('password') == ""):
	xbmc.executebuiltin("XBMC.Notification(" + __settings__.getAddonInfo('name') + "," + __language__(30000) + ",10000,"+icon+")")
	__settings__.openSettings()

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

domain = 'www.manoto1.com'

def loginAndPlay():
	url = 'http://' + domain + '/live'
	
	if not cj:
		resp = opener.open(url)
		html_data = resp.read()
	
		parsedJS = re.findall(r"setCookie\('(.*?)'\s*,\s*'(.*?)'\s*,\s*(.*?)\);", html_data)

		ck = cookielib.Cookie(version=0, name=parsedJS[0][0], value=parsedJS[0][1], port=None, port_specified=False, domain=domain, domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
		cj.set_cookie(ck)

	resp = opener.open(url)
	html_data = resp.read()

	soup = BeautifulSoup(html_data)
	eventVal = soup.find('input',id='__EVENTVALIDATION',type='hidden')
	viewState = soup.find('input',id='__VIEWSTATE',type='hidden')

	params = '__EVENTARGUMENT=&__EVENTTARGET=ctl00%%24ContentPlaceHolderMainContent%%24lbtnEnter&__EVENTVALIDATION=%s&__VIEWSTATE=%s&ctl00%%24ContentPlaceHolderMainContent%%24txtUsername=%s&ctl00%%24ContentPlaceHolderMainContent%%24txtPassword=%s' % (urllib.quote(eventVal['value']), urllib.quote(viewState['value']), urllib.quote(__settings__.getSetting('username')), urllib.quote(__settings__.getSetting('password')))
	
	resp = opener.open('http://www.manoto1.com/LiveStream.aspx', params) 	

	resp = opener.open(url)
	html_data = resp.read()

	soup = BeautifulSoup(html_data)
	stream = soup.find('source', type='video/mp4');	
	
	if stream is None or stream['src'] is None:
		return False
	
	listitem.setPath(stream['src'])
	xbmc.Player().play(stream['src'], listitem, False)

	return True

if sys.argv[0].endswith('play'):
	while not loginAndPlay():
        	xbmc.executebuiltin("XBMC.Notification(" + __settings__.getAddonInfo('name') + "," + __language__(30001) + ",10000,"+icon+")")
        	__settings__.openSettings()
else:
	xbmcplugin.addDirectoryItem(int(sys.argv[1]), sys.argv[0] + 'play', listitem)
	xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)
