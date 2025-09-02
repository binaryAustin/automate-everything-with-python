import json
import requests


url = "https://api.languagetoolplus.com/v2/check"

data = {"text": "Tis is a nixe day", "language": "en-US"}

res = requests.post(url, timeout=10.0, data=data)

result = json.loads(res.text)
