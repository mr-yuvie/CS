from urllib.request import urlopen, Request

url = "http://google.com"
# page= urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
page = urlopen(url)
data = page.read()
final_data = data.decode("utf-8")
print(final_data)
with open(r"Y:\CS\test\data.txt", "w") as F:
    F.write(final_data)
