import pathlib
import hashing

original_folder = "img/"
folder_to_check = "img_modificado/"

def teste_hash():
    for file in pathlib.Path("img").iterdir():
        if file.suffix in [".png", ".jpg", ".jpeg"]:
            print("\n----------------------------------------------------------------\n")
            print(f'Analisando a imagem: {file}')
            origianl_hash = hashing.generate_image_hash(original_folder + file.name)
            print(f'Hash imagem original: {origianl_hash}')
            print(f'Comparando o outra imagem: {folder_to_check + file.name}')
            integrity_check = hashing.verify_hash(origianl_hash, folder_to_check + file.name)
            
            if integrity_check:
                print("A imagem está íntegra.")
            else:
                print("A imagem foi modificada.")
            
            print("\n----------------------------------------------------------------\n")



print("Teste de Integridade")
print("----------------------------------------------------------------")

print("1 - Comparando as imagens originais com as imagens modificadas")
print("2 - Comparando as imagens modificadas com as imagens originais")
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
                
        

