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

# Input the URL you would like to shorten
url = "https://www.thepythoncode.com/article/make-url-shortener-in-python"

# POST Request to obtain shortened URL
shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
if shorten_res.status_code == 200:
    # If response is OK, get shortened URL
    link = shorten_res.json().get("link")
    print("Shortened URL: ", link)
