import hashlib
import os

# Primeros pasos

# Semilla aleatoria - sal 
# Es una variable binaria de 16 bytes
salt = os.urandom(16)

mi_password = "1234"

# Password-Based Key Derivation Function 2, o PBKDF2
# Se utiliza principalmente para derivar una clave segura a partir de una contraseña
mi_password_hashed = hashlib.pbkdf2_hmac("sha256", mi_password.encode("utf-8"), salt, 100000)

print(f'''
Passowrd : {mi_password}
Hash     : {mi_password_hashed.hex()}
''')

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

# Ejemplo
saved_password = hash_password("1234")

# Resultado correcto
print(check_password("1234", saved_password))

# Resultado incorrecto
print(check_password("12345", saved_password))

def save_hash(hashed_password):
    with open("config.py", "w") as file:
        file.write(f'HASHED_PASSWORD="{hashed_password.hex()}"')

save_hash(saved_password)