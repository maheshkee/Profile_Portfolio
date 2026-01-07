import qrcode
import qrcode.image.svg as svg

# -------- YOUR CONTACT DETAILS --------
VCARD = """BEGIN:VCARD
VERSION:3.0
N:Kumar;Mahesh;;;
FN:Mahesh Kumar
TEL;TYPE=CELL:+91XXXXXXXXXX
EMAIL:mahesh@email.com
END:VCARD
"""

LABEL = "Mahesh Kumar"
OUTPUT_FILE = "mahesh_contact.svg"

# -------- GENERATE QR --------
img = qrcode.make(VCARD, image_factory=svg.SvgImage)
qr_svg = img.to_string().decode()

# -------- ADD LABEL BELOW QR --------
final_svg = f"""<svg xmlns="http://www.w3.org/2000/svg">
{qr_svg}
<text x="50%" y="100%" dy="1.6em"
      text-anchor="middle"
      font-size="18"
      font-family="Arial, sans-serif">
{LABEL}
</text>
</svg>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(final_svg)

print("Contact QR generated:", OUTPUT_FILE)
