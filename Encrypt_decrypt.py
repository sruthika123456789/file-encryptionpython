from cryptography.fernet import Fernet

# Generate and save key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    with open("encrypted_" + filename, "wb") as file:
        file.write(encrypted_data)

    print("✅ File encrypted successfully")

# Decrypt file
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    decrypted_data = fernet.decrypt(data)

    with open("decrypted_" + filename, "wb") as file:
        file.write(decrypted_data)

    print("✅ File decrypted successfully")

# Main
generate_key()

choice = input("Enter E to encrypt or D to decrypt: ").upper()

if choice == "E":
    encrypt_file("sample.txt")
elif choice == "D":
    decrypt_file("encrypted_sample.txt")
else:
    print("❌ Invalid choice")
