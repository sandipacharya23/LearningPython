import qrcode
img = qrcode.make('Sandip Acharya')
type(img)  # qrcode.image.pil.PilImage
img.save("sandip.png")