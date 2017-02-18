import ConfigParser, urllib2, os

config = ConfigParser.ConfigParser()
config.readfp(open('sched_util.conf'))

CONFIG_API_SECTION = 'Sched'
CONFIG_API_KEY     = 'api_key'
CONFIG_API_URL     = 'api_url'

def hasConfigValue(config, section, item):
    if config.has_section(section):
        if config.has_option(section, item):
            return True
    return False

def getConfigs(config):
    apiKey = None
    apiUrl = None 

    if hasConfigValue(config, CONFIG_API_SECTION, CONFIG_API_KEY):
        apiKey = config.get(CONFIG_API_SECTION, CONFIG_API_KEY)

    if hasConfigValue(config, CONFIG_API_SECTION, CONFIG_API_URL):
        apiUrl = config.get(CONFIG_API_SECTION, CONFIG_API_URL)

    return apiKey, apiUrl

def sessionList(apiKey, apiUrl, since, format, status, customData):
    argSince = argFormat = argStatus = argCustomData = '' 
    apiEndpoint = apiUrl + 'session/list?'
    argApiKey   = 'api_key=' + apiKey

    if since:
        argSince    = '&since=' + since
    if format:
        argFormat   = '&format=' + format
    if status:
        argStatus   = '&status=' + status
    if customData:
        argCustom   = '&custom_data=' + customData

    requestUrl = apiEndpoint + argApiKey + argSince + argFormat + argStatus + argCustom

    print urllib2.urlopen(requestUrl).read()


apiKey, apiUrl = getConfigs(config)
sessionList(apiKey, apiUrl, None, 'json', None, 'Y')


