#QR Code Generater

import qrcode
import image

qr = qrcode.QRCode(
  version = 5, # version of the QR
  box_size = 5, # size of the box QR displayed
  border = 8 # white space in all 4 sides of QR
)

data = input('Enter URL (or) text :\n')

qr.add_data(data)
qr.make(fit=True)

print("Generating QR Code...")
img = qr.make_image(fill = 'black', back_color = 'white') #generating QR image

print("Saving it to 'QR_Code.png'...")
img.save('QR_Code.png') #saving generated QR in an PNG image file

x = input('QR Code Genration Completed.')
