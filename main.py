import pyqrcode

url = input("url girin : ")

url = pyqrcode.create(url)
url.svg('uca-url.svg', scale=5)
url.eps('uca-url.eps', scale=2)
print(url.terminal(quiet_zone=1))
