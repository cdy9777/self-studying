import requests

url = 'https://nadocoding.tistory.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

res = requests.get(url, headers=headers)
res.raise_for_status()
print(res.status_code)
with open('nadocoding.html', 'w', encoding="utf8") as f:
    f.write(res.text)
