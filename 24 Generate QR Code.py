# Install qrcode: pip install qrcode
# Project Name: Generate QR code in Python

import qrcode

data = input("Enter Text or URL: ")

qr = qrcode.make(data)
qr.save("qrcode.png")

print("QR Code generated successfully ...!!!")
