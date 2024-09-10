from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
import os

def generate_keys():
    # Gera a chave privada
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    # Extrai a chave pública
    public_key = private_key.public_key()

    # Serializa as chaves
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_pem, public_pem

def sign_image(private_pem, image_path):
    # Carrega a chave privada
    private_key = serialization.load_pem_private_key(private_pem, password=None)
    
    # Lê os dados da imagem
    with open(image_path, 'rb') as file:
        image_data = file.read()

    # Gera a assinatura
    signature = private_key.sign(
        image_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_pem, image_path, signature):
    # Carrega a chave pública
    public_key = serialization.load_pem_public_key(public_pem)
    
    # Lê os dados da imagem
    with open(image_path, 'rb') as file:
        image_data = file.read()

    try:
        public_key.verify(
            signature,
            image_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False

# Após os testes, excluir os arquivos de chave e assinatura
def delete_files():
    try:
        os.remove('private_key.pem')
        os.remove('public_key.pem')
        os.remove('signature.sig')
        print("Chaves e assinatura removidas com sucesso.")
    except FileNotFoundError:
        print("Arquivos já removidos ou não encontrados.")