def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# Kiem tra so nguyen to va in ra ket qua
number = int(input("Nhap vao so can kiem tra: "))
if kiem_tra_so_nguyen_to(number):
    print(number, "La so nguyen to.")
else:
    print(number, "Khong phan la so nguyen to.")
      