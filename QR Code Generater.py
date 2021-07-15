#QR Code Generater

import qrcode
import image

qr = qrcode.QRCode(
  version = 5,
  box_size = 5,
  border = 8
)

data = input('Enter URL (or) text :\n')

qr.add_data(data)
qr.make(fit=True)
print("Generating QR Code...")
img = qr.make_image(fill = 'black', back_color = 'white')
print("Saving it to 'QR_Code.png'...")
img.save('QR_Code.png')
x = input('QR Code Genration Completed.')