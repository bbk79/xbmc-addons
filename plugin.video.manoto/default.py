import xbmc, xbmcgui, os, xbmcaddon, xbmcplugin

__settings__ = xbmcaddon.Addon()
home = __settings__.getAddonInfo('path')
addon_handle = int(sys.argv[1])
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
li = xbmcgui.ListItem ('Live Stream')
li.setArt({ 'thumb': icon })
li.setInfo('video', {'plot':'Manoto TV Live Stream'})

liveVideoUrl = "https://d2rwmwucnr0d10.cloudfront.net/live.m3u8"

xbmcplugin.addDirectoryItem(handle=addon_handle, url=liveVideoUrl, listitem=li)
xbmcplugin.endOfDirectory(addon_handle)
