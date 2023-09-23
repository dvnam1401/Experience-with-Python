# Đọc dữ liệu từ tập tin dssv.txt
with open("./dssv.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    danh_sach_sv = [(lines[i], lines[i+1], lines[i+2]) for i in range(0, len(lines), 3)]

# a. In ra danh sách sinh viên đã nhập
print("\nDanh sách sinh viên đã nhập:")
for sv in danh_sach_sv:
    print(sv)

# b. In ra danh sách sinh viên đã nhập với số thứ tự
print("\nDanh sách sinh viên đã nhập (có số thứ tự):")
for idx, sv in enumerate(danh_sach_sv, 1):
    print(f"{idx}. {sv[0].strip()}, {sv[1].strip()}, năm thứ {sv[2].strip()}")

# c. Lưu thông tin sinh viên năm thứ 1 vào tập tin "dssv_nam1.txt"
with open("dssv_nam1.txt", "w", encoding="utf-8") as f:
    for sv in danh_sach_sv:
        if sv[2].strip() == '1':
            f.write(sv[0] + sv[1] + sv[2])
