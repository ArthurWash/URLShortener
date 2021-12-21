import requests as requests
from secrets import secrets

# Account Credentials
username = secrets.get('username')
password = secrets.get('password')

# Access Token
auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
if auth_res.status_code == 200:
    # if response is OK, get access token
    access_token = auth_res.content.decode()
    print("[!] Got access token:", access_token)
else:
    print("[!] ERROR! Cannot access token. Process cancelled. [!]")
    exit()

# GUID Setup

# Construct the request headers with auth
headers = {"Authorization": f"Bearer {access_token}"}

# Get the GUID associated with my account
groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
if groups_res.status_code == 200:
    # If response is OK, get GUID
    groups_data = groups_res.json()['groups'][0]
    guid = groups_data['guid']
else:
    print("[!] ERROR! Cannot get GUID. Process cancelled. [!]")
    exit()
