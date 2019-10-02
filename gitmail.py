"""
1. Promts for a github username
2. Looks up the public events using the Github API, parses the JSON
3. Retrieves the list of emails with their respective user names
"""
import urllib
import json

username = raw_input('Enter Github username:\n')
url = 'https://api.github.com/users/' + username+ '/events/public'

input = urllib.urlopen(url).read()

print '\nRetrieving information about', str(username)+'...'

data_hand = json.loads(input)

email_dict = dict()

for line in data_hand:
    #print 'checking:', line
    try:
        commits_list = line['payload']['commits']
        #print 'FOUND'
        for item in commits_list:
            email_address = item['author']['email']
            name = item['author']['name']
            if name not in email_dict:
                email_dict[name] = email_address
    except:
        continue

print '\nRetrieved', len(email_dict), 'email address(es):'
for name, email in email_dict.items():
    print '    ', name+':', email
