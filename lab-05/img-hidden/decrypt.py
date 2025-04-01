import sys
from PIL import Image

def decode_image(encoded_image_path):
    # Mở ảnh đã mã hóa
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""

    # Trích xuất bit ẩn từ ảnh
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            
            # Lấy bit cuối cùng từ mỗi kênh màu (LSB)
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Chuyển đổi chuỗi nhị phân thành thông điệp
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) < 8:  # Bỏ qua nếu không đủ 8 bit
            continue
            
        char = chr(int(byte, 2))
        
        # Dừng khi gặp ký tự kết thúc (null character)
        if char == '\0':
            break
            
        message += char

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()