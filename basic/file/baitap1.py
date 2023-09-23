# Khởi tạo danh sách để lưu các số nguyên
from random import random

so_nguyens = []

# Cho phép người dùng nhập tối đa 100 số nguyên
for _ in range(100):
    so_nguyen = random.randint(1, 1000)  # Tạo số nguyên ngẫu nhiên từ 1 đến 1000 (có thể điều chỉnh khoảng số ngẫu nhiên theo nhu cầu)
    so_nguyens.append(so_nguyen)

# # Lưu các số nguyên đã nhập vào tập tin "songuyen.txt"
# with open("basic/file/songuyen.txt", "w") as f:
#     for so in so_nguyens:
#         f.write(str(so) + '\n')
#
# # In ra các số nguyên đã nhập và số lượng
# print("\nCác số nguyên đã nhập:", so_nguyens)
# print("Số lượng số nguyên đã nhập:", len(so_nguyens))
#
# # Lọc và in ra các số chẵn từ danh sách
# so_chans = [so for so in so_nguyens if so % 2 == 0]
# print("\nCác số chẵn:", so_chans)
#
#
# # Hàm kiểm tra một số có phải là số nguyên tố hay không
# def la_so_nguyen_to(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# # Lọc và in ra các số nguyên tố từ danh sách
# so_nguyen_tos = [so for so in so_nguyens if la_so_nguyen_to(so)]
# print("\nCác số nguyên tố:", so_nguyen_tos)
