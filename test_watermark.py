from PIL import Image, ImageDraw, ImageFont
import numpy as np
import pathlib

original_folder = "img/"
folder_to_check = "img_modificado/"

def teste_hash():
    for file in pathlib.Path("img").iterdir():
        if file.suffix in [".png", ".jpg", ".jpeg"]:
            print("\n----------------------------------------------------------------\n")
            print(f'Analisando a imagem: {file}')
            
            verify_watermark(original_folder + file.name, folder_to_check + file.name)
            
            print("\n----------------------------------------------------------------\n")

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


print("Teste de Integridade")
print("----------------------------------------------------------------")

print("1 - Comparando as imagens originais com as imagens modificadas")
print("2 - Comparando as imagens originais com as imagens originais")
print("3 - digitar pasta de origem e pasta de destino")

opcao = input("Digite a opção: ")

if opcao == "1":
    teste_hash()
elif opcao == "2":
    original_folder = "img/"
    folder_to_check = "img/"
    teste_hash()
elif opcao == "3":
    original_folder = input("Digite a pasta de origem: ") + "/"
    folder_to_check = input("Digite a pasta de destino: ") + "/"
    teste_hash()
                
