# tạo mã qr: chỉ sử dụng vs python 3.10
import qrcode
my_text = 'Ga python'# cần mã hóa
qr = qrcode.QRCode(version=1, box_size=10, border=5) #thông số của mã qr
qr.add_data(my_text) # mã hóa
qr.make(fit=True) 

img = qr.make_image(fill='black',back_color='white')
img.save('myqrcode.png') #lưu mã qr vào hình