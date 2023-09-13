# Chuỗi biểu diễn địa chỉ email
email = "tranhminhdang@dtu.edu.vn 2023 Jan 5 09:14:16"

# Tách chuỗi email bằng ký tự @
parts = email.split("@")
print(parts)
# Phần đầu tiên là tên tài khoản
username = parts[0]
# Phần thứ hai là tên host và ngày giờ
host_and_date = parts[1]
# Tách phần thứ hai bằng khoảng trắng
host_and_date = host_and_date.split(' ')
print(host_and_date)
# Phần đầu tiên là tên host
host = host_and_date[0]

# Hiển thị tên tài khoản và tên host
print("Tên tài khoản:", username)
print("Tên host:", host)
