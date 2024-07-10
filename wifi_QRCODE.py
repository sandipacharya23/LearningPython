import qrcode
img = qrcode.make('Sandip Acharya')

wifi_type ='WPA'
wifi_ssid ='sandipwifi01_fctwn'
wifi_password ='S@Ndy_20570125'
wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make('wifi')
type(img)  # qrcode.image.pil.PilImage
img.save("wifi.png")
