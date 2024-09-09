from PIL import Image
import numpy as np

def decode_watermark(watermarked_image_path):
    # Carrega a imagem
    image = Image.open(watermarked_image_path)
    image = image.convert('RGB')
    pixels = np.array(image)

    binary_data = ""
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):  # R, G, B
                binary_data += bin(pixels[i][j][k])[-1]

    # Converte binário para texto
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_text = ""
    for byte in all_bytes:
        if byte == '11111111':
            break
        decoded_text += chr(int(byte, 2))
    return decoded_text

extracted_watermark = decode_watermark('img/watermarked_image.png')
print(f"Marca d'água extraída: {extracted_watermark}")

extracted_watermark_modified = decode_watermark('img/modified_watermarked_image.png')
print(f"Marca d'água extraída da imagem modificada: {extracted_watermark_modified}")
