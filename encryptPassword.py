import base64
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Character set for random string generation (matching JavaScript)
AES_CHARS = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"

def random_string(length):
    """Generate a random string of specified length using the defined character set"""
    return ''.join(random.choice(AES_CHARS) for _ in range(length))

def get_aes_string(data, key, iv):
    """Encrypt data with AES-CBC with PKCS7 padding"""
    data = data.encode('utf-8')
    key = key.encode('utf-8')[:16]  # Ensure key is 16 bytes
    iv = iv.encode('utf-8')[:16]    # Ensure IV is 16 bytes
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data, AES.block_size)
    encrypted = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted).decode('utf-8')

def encrypt_aes(data, key):
    """Encrypt with a random 64-character prefix and random 16-character IV"""
    if not key:
        return data
    prefix = random_string(64)
    iv = random_string(16)
    return get_aes_string(prefix + data, key, iv)

def encrypt_password(password, salt):
    """Encrypt password using the salt"""
    try:
        return encrypt_aes(password, salt)
    except:
        return password

# Example usage
if __name__ == "__main__":
    password = input("Enter password: ")
    salt = input("Enter salt: ")
    encrypted = encrypt_password(password, salt)
    print(f"Encrypted password: {encrypted}")