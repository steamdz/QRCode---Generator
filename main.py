import pyqrcode
import png
from pyqrcode import QRCode
Link = "https://www.youtube.com/aymendev"
url = pyqrcode.create(Link)
url.png("AYMENDEV.png",scale=6)
print("Votre QRcode OK")