import urllib.request
fp = urllib.request.urlopen(r'http://www.python.org')
print(fp.read(1000))
print(fp.read(1000).decode())
fp.close()