import digital_signature

#Gerar chaves criptograficas
private_key_pem, public_key_pem = digital_signature.generate_keys()
with open('private_key.pem', 'wb') as f:
    f.write(private_key_pem)
with open('public_key.pem', 'wb') as f:
    f.write(public_key_pem)
print("Chaves criptográficas geradas e salvas com sucesso.")


# Assinar a Imagem Original
signature = digital_signature.sign_image(private_key_pem, 'img/original_image.png')
with open('signature.sig', 'wb') as f:
    f.write(signature)
print("Imagem original assinada com sucesso.")

#Verificar assinatura da imagem modificada
is_valid = digital_signature.verify_signature(public_key_pem, 'img/original_image.png',
signature)
if is_valid:
    print("Assinatura verificada: A imagem é autêntica e íntegra.")
else:
    print("Assinatura inválida: A imagem foi alterada ou a assinatura é incorreta.")

#verificar assinatura da imagem modificada
is_valid_modified = digital_signature.verify_signature(public_key_pem, 'img/modified_watermarked_image.png', signature)
if is_valid_modified:
    print("Assinatura verificada: A imagem é autêntica e íntegra.")
else:
    print("Assinatura inválida: A imagem foi alterada ou a assinatura é incorreta.")

# Chamando a função para excluir as chaves e assinatura
digital_signature.delete_files()