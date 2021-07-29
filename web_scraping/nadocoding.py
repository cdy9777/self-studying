import requests

url = 'https://www.google.com/'
res = requests.get(url)
res.raise_for_status
print(res.status_code)
