import pyqrcode

#replace strings by other websites and svgs
s = "www.arpanmahatra.com"
url = pyqrcode.create(s)
url.svg("arpanmahatra.svg", scale=10)