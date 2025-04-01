import sys
from PIL import Image

def encode_image(image_path, message):
    # Mở ảnh và lấy thông tin kích thước
    img = Image.open(image_path)
    width, height = img.size
    
    # Chuyển thông điệp sang dạng nhị phân
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Dấu hiệu kết thúc thông điệp (16-bit)

    # Giấu tin vào ảnh
    data_index = 0
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            
            # Giấu vào 3 kênh màu (R, G, B)
            for color_channel in range(3):
                if data_index < len(binary_message):
                    # Thay bit cuối cùng của mỗi kênh màu
                    pixel[color_channel] = int(
                        format(pixel[color_channel], '08b')[:-1] + 
                        binary_message[data_index], 2
                    )
                    data_index += 1
            
            img.putpixel((col, row), tuple(pixel))
            
            if data_index >= len(binary_message):
                break
        else:
            continue
        break

    # Lưu ảnh đã giấu tin
    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print(f"Steganography complete. Encoded image saved as {encoded_image_path}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return

    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()