import digital_signature
import pathlib

original_folder = "img/"
folder_to_check = "img_modificado/"

def teste_hash():
    for file in pathlib.Path("img").iterdir():
        if file.suffix in [".png", ".jpg", ".jpeg"]:
            print("\n----------------------------------------------------------------\n")
            print(f'Analisando a imagem: {file}')
            private_key_pem, public_key_pem = digital_signature.generate_keys()
            
            with open('private_key.pem', 'wb') as f:
                f.write(private_key_pem)
            with open('public_key.pem', 'wb') as f:
                f.write(public_key_pem)
        
            # Assinar a Imagem Original
            signature = digital_signature.sign_image(private_key_pem, original_folder + file.name)
            
            with open('signature.sig', 'wb') as f:
                f.write(signature)

            #verificar assinatura da imagem modificada
            is_valid_modified = digital_signature.verify_signature(public_key_pem, folder_to_check + file.name, signature)
            
            if not is_valid_modified:
                print("A imagem foi modificada!")
            else:
                print("A imagem está intacta e original.")

            # Chamando a função para excluir as chaves e assinatura
            digital_signature.delete_files()


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
                