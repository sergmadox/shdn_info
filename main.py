import shodan
import sys

# Configuration
API_KEY = "mTqhUFdzBOdTWRjEbGE5DzsZeS5vHf2r"

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
                print (service['ip_str'])
                print (service['hostnames'])
                print ('=========================')
        print ('Total result ' + str(result['total']))
except Exception as e:
        print ('Error: %s') % e
        sys.exit(1)% e