# Nhap cac dong tu nguoi dung
print("Nhap cac dong van ban (Nhap 'done' de ket thuc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    # Chuyen cac dong thanh chu in hoa va in ra man hinh
    print("\nCac dong da nhap su khi chuyen thanh chu in hoa:")
    for line in lines:
        print(line.upper())