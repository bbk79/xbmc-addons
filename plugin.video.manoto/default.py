import xbmc, xbmcgui, os, xbmcaddon

__settings__ = xbmcaddon.Addon(id='plugin.video.manoto')
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
li = xbmcgui.ListItem ('manoto')
li.setThumbnailImage(icon)

url = 'http://manotolive-i.akamaihd.net/hls/live/251779/livexhq/master_Layer1.m3u8'
xbmc.Player().play(url, li, False)
