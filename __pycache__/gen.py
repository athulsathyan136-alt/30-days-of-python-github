import qrcode

data = "https://www.w3schools.com"

img = qrcode.make(data)
img.save('generated.png')
print('Sucessfull')