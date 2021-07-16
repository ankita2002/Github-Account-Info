import requests
from pprint import pprint

print("Enter username:")
username = input()
url = f"https://api.github.com/{username}"
user_data = requests.get(url).json()

print('Name: ',user_data['name'])
print("login id: ",user_data['login'])
print("Unique id: ",user_data['id'])
print("Followers: ",user_data['followers'])
print("Following: ",user_data['following'])
print("Public Repositories: ",user_data['public_repos'])
print("Location: ",user_data['location'])
print("GitHub Bio: ",user_data['bio'])