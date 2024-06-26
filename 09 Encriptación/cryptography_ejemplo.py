import cryptography
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

def hash_password(password):
    # Generar una sal aleatoria de 16 bytes
    salt = os.urandom(16)
    # Crear un objeto KDF (Key Derivation Function)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    # Derivar la clave (hash de la contraseña)
    hashed_password = kdf.derive(password.encode('utf-8'))
    # Devolver la sal y el hash combinados
    return salt + hashed_password

def check_password(password, hashed_password):
    # Extraer la sal del hash almacenado (los primeros 16 bytes)
    salt = hashed_password[:16]
    # Extraer el hash de la contraseña (los bytes restantes)
    stored_hash = hashed_password[16:]
    # Crear un objeto KDF (Key Derivation Function) con la misma sal
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    try:
        # Verificar la contraseña; esto lanzará una excepción si la contraseña no es correcta
        kdf.verify(password.encode('utf-8'), stored_hash)
        return True
    except cryptography.exceptions.InvalidKey:
        return False