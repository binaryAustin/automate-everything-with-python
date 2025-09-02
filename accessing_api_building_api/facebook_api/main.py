import os
import requests
from dotenv import load_dotenv


load_dotenv(".env")

facebook_access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")


url = f"https://graph.facebook.com/v23.0/me?fields=id%2Cname&access_token={facebook_access_token}"

res = requests.get(url, timeout=10.0)

print(res.text)
