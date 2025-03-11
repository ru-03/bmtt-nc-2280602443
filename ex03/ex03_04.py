def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

# Nhập tuple từ người dùng
input_tuple = eval(input("Nhập một tuple, ví dụ (1, 2, 3): "))

# Sử dụng hàm và in kết quả
first, last = truy_cap_phan_tu(input_tuple)
print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)