import qrcode  
from PIL import Image, ImageDraw, ImageOps
import urllib.request

# logo
logo_url = input("\n\tWhich logo shall we add in? Provide the link to the image ") 
logo = Image.open(urllib.request.urlopen(logo_url))

basewidth = 200
# resizer
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)

QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H
)

# url for QR generation
url = input("\n\tEnter URL for QR code is nedded ")

qr_code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

qr_code.add_data(url)
qr_code.make()

color = input("\n\tColor choice? ")

img = qr_code.make_image(fill_color=color, back_color='white').convert('RGB')

# masking for circular shape of logo
mask = Image.new('L', (logo.size[0], logo.size[1]), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, logo.size[0], logo.size[1]), fill=255)

# Apply the circular mask to the logo
logo = ImageOps.fit(logo, mask.size)
logo.putalpha(mask)


position = ((img.size[0]-logo.size[0])//2, (img.size[1]-logo.size[1])//2)

# add logo to the qr generated(img)
img.paste(logo,position,logo)

output_file_name = input("\n\tDesired file name eg:(image.png) ")
img.save(output_file_name+".png")

print(f'QR Code Generated. Check your current folder for {output_file_name}.png')