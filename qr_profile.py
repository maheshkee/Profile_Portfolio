import qrcode
import qrcode.image.svg as svg

data = "https://maheshkee.github.io/Profile_Portfolio/"

factory = svg.SvgImage
img = qrcode.make(data, image_factory=factory)
img.save("portfolio_qr.svg")
