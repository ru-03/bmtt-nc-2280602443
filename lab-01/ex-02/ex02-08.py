# Kiem tra so nhi phan co chia het cho 5 hay khong
def chia_het_cho_5(so_nhi_phan):
    # Chuyen so nhi phan sang so thap phan
    so_thap_phan = int(so_nhi_phan, 2)
    # Kiem tra so thap phan co chia het cho 5 khong
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False

# Nhap chuoi so nhi phan tu nguoi dung
chuoi_so_nhi_phan = input("Nhap chuoi so nhi phan (phan tach boi dau phay): ")

# Tach chuoi thanh so cac so nhi phan va kiem tra so chia het cho 5
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]

# In ra cac so nhi phan chia het cho 5
if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Cac so nhi phan chia het cho 5 la:", ket_qua)
else:
    print("Khong co so nhi phan nao chia het cho 5 trong chuoi da nhap.")
