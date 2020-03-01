import urllib2, re

livePageUrl = 'https://iranintl.com/live'
req = urllib2.Request(livePageUrl, headers = {'User-Agent': 'Kodi'})

try:
    response = urllib2.urlopen(req)
    html = response.read()

    liveVideoUrls = re.findall('https://.*?.m3u8', html)

    if len(liveVideoUrls) == 0:
        print 'Failed to find a stream URL.'

    print liveVideoUrls

except urllib2.URLError as e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
