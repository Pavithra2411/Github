#Program returns of all respositries of a user.
import base64
from github import Github
from pprint import pprint
# Any Github username
username ="Pavithra2411"
g=Github()
user=g.get_user(username)
for repo in user.get_repos():
    print (repo)
