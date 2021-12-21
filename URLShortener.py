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