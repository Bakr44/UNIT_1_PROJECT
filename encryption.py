from cryptography.fernet import Fernet,InvalidToken
from hashlib import sha256
import base64

"""
# Define a random key hash syntax
def generate_key(master_password):
    return sha256(master_password.encode()).digest()
"""
### using lambda fuction to generate a random key hash syntax
generate_key = lambda master_password: sha256(master_password.encode()).digest()


# Define a function to encrypt the password
def encrypt_data(data,master_password):
    """Encrypts the password using the master password"""
    key = generate_key(master_password)
    encoded_key = base64.urlsafe_b64encode(key)
    f = Fernet(encoded_key)
    encrypted_password=f.encrypt(data.encode()).decode()
    return encrypted_password

### using lambda fuction to encrypt the password
#encrypt_data = lambda data, master_password: Fernet(base64.urlsafe_b64encode(generate_key(master_password))).encrypt(data.encode()).decode()


# Define a function to decrypt the password
def decrypt_data(data, master_password):
    """Decrypts the password using the master password"""
    key = generate_key(master_password)
    decoded_key = base64.urlsafe_b64encode(key)
    f = Fernet(decoded_key)
    try:
        return f.decrypt(data.encode()).decode()
    except InvalidToken:
        raise ValueError("Incorrect master password")
    
### using lambda fuction to decrypt the password
#decrypt_data = lambda data, master_password: Fernet(base64.urlsafe_b64encode(generate_key(master_password))).decrypt(data.encode()).decode() 


"""
master_password = "mysecretkey"
password = "mypassword"
encrypted_password = encrypt_data(password, master_password)
print("Encrypted password:", encrypted_password)

decrypted_password = decrypt_data(encrypted_password, master_password)
print("Decrypted password:", decrypted_password)
"""