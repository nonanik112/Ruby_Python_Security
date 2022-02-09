require 'rqrcode'

url = ARGV[0]
color = ARGV[1] ? "##{ARGV[1]}" : 'red'

qr_code = RQRCode::QRCode.new(url)
png = qr_code.as_png(
  color: color,
  fill: "white",
  size: 300
)

IO.binwrite("telefon.png", png.to_s)
