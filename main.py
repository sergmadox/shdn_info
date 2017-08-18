import shodan
import sys

# Configuration
API_KEY = "your token"

# Input validation
if len(sys.argv) == 1:
    print ('Usage: %s <search query>') % sys.argv[0]
    sys.exit(1)

try:
        # Setup the api
        api = shodan.Shodan(API_KEY)

        # Perform the search
        query = ' '.join(sys.argv[1:])
        result = api.search(query)
        # Loop through the matches and print each IP
        
        for service in result['matches']:
                print ('IP = '+ service['ip_str'] + '\n'+'isp  = ' + service['isp'] + '\nTransport protocol = ' + service['transport'] +'\n' + 'port is '+ str(service['port']) +
                        '\n' + 'country: ' + service['location']['country_name'] + '\nHostname' + str(service['hostnames']) + '\nOS = ' +str(service.get('os','n/a')) + '\n==============================')
        print ('Total result ' + str(result['total']))
except Exception as e:
        print ('Error: %s') % e
        sys.exit(1)% e