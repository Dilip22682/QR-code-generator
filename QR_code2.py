import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=7,border=4)

qr.add_data("https://www.linkedin.com/in/dilip-kumar-patel-916168210/")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="pink")
img.save("Dilip_linkedin_ids.png")
