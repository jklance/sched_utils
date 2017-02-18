import argparse, ConfigParser, urllib2, os

config = ConfigParser.ConfigParser()
config.readfp(open('sched_util.conf'))

parser = argparse.ArgumentParser(description='Interact with Sched scheduling app')

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

def parseArguments(parser):
    parser.add_argument('-a', help='Selected activity', required=True, choices=['session_list', 'session_add'])
    parser.add_argument('-i', help='Input file')
    parser.add_argument('-o', help='Output file (defaults to console)')

    args = parser.parse_args()
    return args

def outputResults(results, args):
    if args.o is not None:
        with open(args.o, 'w') as outFile:
            outFile.write(results)
        outFile.closed
    else:
        print results

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

    return urllib2.urlopen(requestUrl).read()


apiKey, apiUrl = getConfigs(config)
args = parseArguments(parser)


if args.a == 'session_list':
    results = sessionList(apiKey, apiUrl, None, 'json', None, 'Y')
elif args.a == 'session_add':
    print 'coming soon'

outputResults(results, args)
