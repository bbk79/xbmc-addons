import xbmc, xbmcgui, os, xbmcaddon, xbmcplugin

__settings__ = xbmcaddon.Addon()
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
iconFHD = xbmc.translatePath(os.path.join(home, 'FHD.png'))
iconHD = xbmc.translatePath(os.path.join(home, 'HD.png'))

li = xbmcgui.ListItem ('Manoto TV (Auto)')
li.setArt({ 'thumb': icon })
li.setInfo('video', {'plot':'Manoto TV Live Stream'})
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url='https://d2rwmwucnr0d10.cloudfront.net/live.m3u8', listitem=li)

li = xbmcgui.ListItem ('Manoto TV (1080p - 2500kbps)')
li.setArt({ 'thumb': iconFHD })
li.setInfo('video', {'plot':'Manoto TV Live Stream'})
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url='https://d2rwmwucnr0d10.cloudfront.net/live_2500.m3u8', listitem=li)

li = xbmcgui.ListItem ('Manoto TV (1080p - 1500kbps)')
li.setArt({ 'thumb': iconFHD })
li.setInfo('video', {'plot':'Manoto TV Live Stream'})
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url='https://d2rwmwucnr0d10.cloudfront.net/live_1500.m3u8', listitem=li)

li = xbmcgui.ListItem ('Manoto TV (1080p - 1000kbps)')
li.setArt({ 'thumb': iconFHD })
li.setInfo('video', {'plot':'Manoto TV Live Stream'})
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url='https://d2rwmwucnr0d10.cloudfront.net/live_1000.m3u8', listitem=li)

li = xbmcgui.ListItem ('Manoto TV (720p - 750kbps)')
li.setArt({ 'thumb': iconHD })
li.setInfo('video', {'plot':'Manoto TV Live Stream'})
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url='https://d2rwmwucnr0d10.cloudfront.net/live_750.m3u8', listitem=li)

li = xbmcgui.ListItem ('Manoto TV (720p - 500kbps)')
li.setArt({ 'thumb': iconHD })
li.setInfo('video', {'plot':'Manoto TV Live Stream'})
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url='https://d2rwmwucnr0d10.cloudfront.net/live_500.m3u8', listitem=li)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
