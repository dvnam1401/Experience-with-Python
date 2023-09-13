import base64
import io
from tkinter import Image

import requests

# Tạo dữ liệu cho mã QR
data = {
    "amount": 10000,
    "name": "John Doe",
    "store_id": 123456,
}

# Gọi API để tạo mã QR
response = requests.post("https://example.com/qrcode", data=data)

# Lấy mã QR từ response
qr_code = response.json()["qr_code"]

# Hiển thị mã QR
img = Image.open(io.BytesIO(base64.b64decode(qr_code)))
img.show()