import pyqrcode
from PIL import Image
data="aajgvdksdcshdbckgsdvcdvckdvcvdvsdvsdv"

qr=pyqrcode.create(data)



qr.png("qrcode.png", scale=8)
image1 = Image.open(r'qrcode.png')
im1 = image1.convert('RGB')
im1.save(r'qrcodee.pdf')
