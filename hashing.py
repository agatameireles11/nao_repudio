import hashlib

def generate_image_hash(image_path):
    
    with open(image_path, 'rb') as file:
        image_data = file.read()
        sha256_hash = hashlib.sha256(image_data).hexdigest()
        
    return sha256_hash

# Verificar Integridade:
def verify_hash(original_hash, image_path):
    current_hash = generate_image_hash(image_path)
    return original_hash == current_hash
