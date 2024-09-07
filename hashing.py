import hashlib

def generate_image_hash(image_path):
    
    with open(image_path, 'rb') as file:
        image_data = file.read()
        sha256_hash = hashlib.sha256(image_data).hexdigest()
        
    return sha256_hash

# Gerar Hash da Imagem Original:
original_image_hash = generate_image_hash('img/original_image.png')
print(f"Hash da imagem original: {original_image_hash}")

# Gerar Hash da Imagem com Marca D'água:
watermarked_hash = generate_image_hash('img/watermarked_image.png')
print(f"Hash da imagem com marca d'água: {watermarked_hash}")

# mesmo uma pequena alteração (como a inserção da marca
# d'água) altera completamente o hash.

# Gerar Hash da Imagem Modificada:
modified_hash = generate_image_hash('img/modified_watermarked_image.png')
print(f"Hash da imagem modificada: {modified_hash}")

# Verificar Integridade:
def verify_hash(original_hash, image_path):
    current_hash = generate_image_hash(image_path)
    return original_hash == current_hash


integrity_check = verify_hash(original_image_hash, 'img/modified_watermarked_image.png')

if integrity_check:
    print("A imagem está íntegra.")
else:
    print("A imagem foi modificada.")