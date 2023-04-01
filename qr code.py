import qrcode
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Define the data to be encoded in the QR code
data = "Example QR code"

# Define the size of the QR code
size = 500

# Generate the QR code
qr = qrcode.QRCode(version=None, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')
img_qr = img_qr.resize((size, size))

# Define the image to be placed in the center of the QR code

# img_center = Image.open('/R/qr/QR.png')    OR
img_center = Image.open('myQR1.png')

img_center = img_center.resize((int(size*0.25), int(size*0.25)))

# Create a new image to combine the QR code and the center image
img_final = Image.new('RGB', (size, size), color = 'white')

# Paste the QR code onto the new image
img_final.paste(img_qr, (0, 0))

# Paste the center image onto the QR code
center_x = int((size - img_center.width) / 2)
center_y = int((size - img_center.height) / 2)
img_final.paste(img_center, (center_x, center_y))

# Add styling to the QR code
draw = ImageDraw.Draw(img_final)
border_size = 40
draw.rectangle([(border_size, border_size), (size-border_size-1, size-border_size-1)], outline='black', width=2)
draw.text((0, size-border_size-20), "Scan to access", font=ImageFont.truetype("arial.ttf", 16), fill='black')

# Save the final image as a PNG file
img_final.save("complex_qr.png")
