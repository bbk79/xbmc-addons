import xbmc, xbmcgui, os, xbmcaddon

__settings__ = xbmcaddon.Addon()
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
addonname = __settings__.getAddonInfo('name')
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
li = xbmcgui.ListItem ('iranintl')
li.setArt({ 'thumb': icon })
li.setInfo('video', {'plot': 'Live Stream'})

liveVideoUrl = "https://live.playstop.live/LS-63503-1/index.m3u8"

xbmc.Player().play(liveVideoUrl, li, False)
