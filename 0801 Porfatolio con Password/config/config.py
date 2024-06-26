import hashlib
import os

# Funciones
def hash_password(password):
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    return salt + hashed_password

def check_password(password, hashed_password):
    # print("123456"[:3])
    salt = hashed_password[:16]
    stored_hash = hashed_password[16:]
    new_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    return new_hash == stored_hash

def save_hash(hashed_password):
    with open("enviroment.py", "w") as file:
        file.write(f'HASHED_PASSWORD="{hashed_password.hex()}"')

if __name__ == "__main__":
    # Sólo cuando este script se ejecute directamente se creará el script de enviroment.py
    hashed_password = hash_password("caballo3monitor2")
    save_hash(hashed_password)
