def check_type(str, types=None):
    """
  Kiểm tra loại giá trị của chuỗi ký tự.

  Args:
    str: Chuỗi ký tự cần kiểm tra.

  Returns:
    Loại giá trị của chuỗi ký tự.
  """

    # Sử dụng biến khác để lưu giá trị của các điều kiện
    is_alpha = all(c.isalpha() for c in str)
    is_digit = all(c.isdigit() for c in str)
    is_space = all(c.isspace() for c in str)

    # Khởi tạo biến types với các giá trị tương ứng
    types = {
        "Chuỗi ký tự chữ": is_alpha,
        "Chuỗi ký tự số": is_digit,
        "Chuỗi ký tự khoảng trắng": is_space,
        "Chuỗi ký tự hỗn hợp": not is_alpha and not is_digit and not is_space,
    }

    return next(iter(types), "Không xác định")


str = input("Nhập vào một chuỗi ký tự: ")
print(check_type(str))
