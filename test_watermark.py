from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Função para comparar duas imagens e verificar se foi modificada
def verify_watermark(image1_path, image2_path):
    # Abrir as imagens
    image1 = Image.open(image1_path).convert("RGB")
    image2 = Image.open(image2_path).convert("RGB")
    
    # Converter as imagens em arrays numpy
    image1_array = np.array(image1)
    image2_array = np.array(image2)
    
    # Comparar as imagens
    diff = np.abs(image1_array - image2_array)
    
    # Se houver uma diferença significativa entre as imagens
    if np.any(diff > 0):
        print("A imagem foi modificada!")
    else:
        print("A imagem está intacta e original.")


# Simulação: carregar a imagem supostamente alterada
original_image = 'img/original_image.png'
modified_image_watermark = 'img/watermarked_image.png'
modified_image = 'img/modified_watermarked_image.png'

# Verificar se a imagem foi alterada comparando com a original com marca d'água
verify_watermark(original_image, modified_image_watermark)
