import requests
res = requests.get("https://www.gutenberg.org/cache/epub/67633/pg67633.txt")
res.raise_for_status()
playfile = open("History of the 1/4 Battalion.text", "wb")
for chunk in res.iter_content(18458):
    playfile.write(chunk)
playfile.close()