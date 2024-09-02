#Esse codigo serve para inserir uma marca d'água em uma imagem.

from PIL import Image
import numpy as np

def encode_watermark(input_image_path, output_image_path, watermark_text):
    # Carrega a imagem
    image = Image.open(input_image_path)
    image = image.convert('RGB')
    pixels = np.array(image)

    # Converte o texto em binário
    binary_watermark = ''.join(format(ord(char), '08b') for char in watermark_text)
    binary_watermark += '1111111111111110'  # Marcador de fim de mensagem

    # Verifica se a imagem pode conter a marca d'água
    total_pixels = pixels.size // 3
    if len(binary_watermark) > total_pixels:
        raise ValueError("Texto muito longo para ser inserido na imagem selecionada.")

    # Inserção da marca d'água
    data_index = 0
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):  # R, G, B
                if data_index < len(binary_watermark):
                    pixels[i][j][k] = int(bin(pixels[i][j][k])[2:-1] + binary_watermark[data_index], 2)
                    data_index += 1

    # Salva a imagem com marca d'água
    watermarked_image = Image.fromarray(pixels)
    watermarked_image.save(output_image_path)
    print(f"Marca d'água inserida com sucesso em {output_image_path}")

encode_watermark('original_image.png', 'watermarked_image.png', 'Esta é uma marca d\'água secreta')

#A marca d'água inserida pelo código é do tipo invisível. Ela não altera visivelmente a imagem, mas esconde a informação dentro dos pixels da imagem de uma maneira que não é perceptível ao olho humano. Isso é feito modificando os bits menos significativos dos valores RGB dos pixels para armazenar o texto da marca d'água em formato binário.

#Como funciona:
#Cada caractere do texto da marca d'água é convertido em binário.
#O código então insere cada bit do texto binário nos bits menos significativos dos valores de cor (R, G, B) dos pixels da imagem.
#A imagem resultante (watermarked_image.png) terá a mesma aparência visual da original, mas conterá o texto oculto dentro dos pixels.
#Para testar se a marca d'água foi realmente inserida é com o decode_watermark