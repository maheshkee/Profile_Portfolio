import qrcode

data = "https://www.linkedin.com/in/nanupatruni-mahesh-kumar-29105b37b/"

qr = qrcode.make(data)
qr.save("linkedin_qr.png")

print("LinkedIn QR code generated: linkedin_qr.png")
