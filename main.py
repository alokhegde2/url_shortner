import pyshorteners

url = input("[+] Enter the url :")
s = pyshorteners.Shortener().tinyurl.short(url)
print("[+] Your shorted url is --> ", s)
