import requests

url = 'https://nadocoding.tistory.com'
headers = {
    'User-Agent': '유저에이전트'}

res = requests.get(url, headers=headers)
res.raise_for_status()
print(res.status_code)
with open('nadocoding.html', 'w', encoding="utf8") as f:
    f.write(res.text)
