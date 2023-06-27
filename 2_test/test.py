import requests

url = "https://bookwalker.jp/de57a21d74-d918-47df-b22f-b3a9454e59df/"
res = requests.get(url=url)
if not res.status_code == 200:
    print("access failed, error code : %d" % res.status_code)
    exit(1)
with open("./save.html", "a",encoding="utf-8") as save_file:
    save_file.write(res.text)
print(res.text)