"""
Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2
chiều. Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.
Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.
Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4,
6, 8]]
"""
def create_2d_array(x, y):
    # Khởi tạo mảng 2 chiều
    array_2d = []
    
    # Lặp qua các hàng
    for i in range(x):
        row = []
        # Lặp qua các cột
        for j in range(y):
            row.append(i * j)
        array_2d.append(row)
    
    return array_2d

# Nhập giá trị X và Y từ người dùng
X = int(input("Nhập giá trị X: "))
Y = int(input("Nhập giá trị Y: "))

# Tạo mảng 2 chiều
result = create_2d_array(X, Y)

# In mảng 2 chiều
for row in result:
    print(row)
