# tạo mã qr: chỉ sử dụng vs python 3.10
import qrcode
my_text = 'Ga python'
qr = qrcode.QRCode(version=1, box_size=10, border=5)
