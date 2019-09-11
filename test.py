import requests
import json

r = requests.get('https://api.github.com/requests/kennethreitz/requests/issues/482')

print(r.url)


r = requests.get(r.url + u'/comments')
print(r.status_code)
# issue = json.loads(r.text)
# print(issue)
# print(issue[u'documentation_url'])1111