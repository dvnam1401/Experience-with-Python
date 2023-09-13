# Nhập vào một chuỗi ký tự. Yêu cầu:
# 	a, Chuỗi ký tự nhập vào có những loại giá trị nào?
# Nhập vào một chuỗi ký tự
s = input("Nhập vào một chuỗi: ")
# In ra chuỗi vừa nhập
print("Chuỗi bạn vừa nhập là:", s)
# Kiểm tra loại giá trị của chuỗi
if s.isnumeric():
    # Nếu chuỗi là số nguyên, chuyển đổi sang số nguyên và in ra kết quả
    n = int(s)
    print("Loại giá trị của chuỗi là số nguyên")
elif s.isdecimal():
    # Nếu chuỗi là số thực, chuyển đổi sang số thực và in ra kết quả
    f = float(s)
    print("Loại giá trị của chuỗi là số thực")
else:
    # Nếu không, in ra loại giá trị là chuỗi
    print("Loại giá trị của chuỗi là chuỗi")

# or

# # Nhập vào một chuỗi ký tự
# s = input("Nhập vào một chuỗi: ")
# # In ra chuỗi vừa nhập
# print("Chuỗi bạn vừa nhập là:", s)
# # Kiểm tra loại giá trị của chuỗi
# try:
#     # Chuyển đổi chuỗi sang số nguyên
#     n = int(s)
#     # In ra loại giá trị là số nguyên
#     print("Loại giá trị của chuỗi là số nguyên")
# except ValueError:
#     try:
#         # Chuyển đổi chuỗi sang số thực
#         f = float(s)
#         # In ra loại giá trị là số thực
#         print("Loại giá trị của chuỗi là số thực")
#     except ValueError:
#         # In ra loại giá trị là chuỗi
#         print("Loại giá trị của chuỗi là chuỗi")