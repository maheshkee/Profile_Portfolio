import qrcode

vcard_data = """BEGIN:VCARD
VERSION:3.0
N:Mahesh;Kumar;;;
FN:Mahesh Kumar
ORG:Software Engineer
TITLE:Backend Developer
TEL;TYPE=CELL:+917989775998
EMAIL:maheshkumaree25@gmail.com
URL:https://maheshkee.github.io/Profile_Portfolio/
END:VCARD
"""

qr = qrcode.make(vcard_data)
qr.save("contact_qr.png")

print("Contact QR code generated: contact_qr.png")
