#Program to returns list of github users.
import requests
from pprint import pprint
url = f"https://api.github.com/users"
user_data = requests.get(url).json()
pprint(user_data)