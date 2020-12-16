#Program returns details of all followers of a user.
import base64
from github import Github
from pprint import pprint
# Any Github username 
username ="Pavithra2411"
g=Github()
user=g.get_user(username)
for follow in user.get_followers():
    print (follow)