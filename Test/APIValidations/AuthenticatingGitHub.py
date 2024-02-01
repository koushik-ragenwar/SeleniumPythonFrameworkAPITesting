import requests
from Utilities.configurations import *
from Utilities.resources import APIResources

# creating url for github login
url = getConfig()['GITHUB']['endpoint'] + APIResources.github_login

# auth=(getConfigGithub()['GitHub']['username']['password'])

# getting login into github account
githubLogin = requests.get(url, verify=False, auth=('koushik-ragenwar', 'exampletest@1234'))

# printing login response
print(githubLogin)

# asserting login response
assert githubLogin.status_code == 200
