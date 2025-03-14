from Crypto.Cipher import DES
import os

# Function to validate and adjust the key to 8 bytes
def get_valid_key():
    while True:
        key = input("Enter a key (exactly 8 characters): ")
        if len(key) == 8:
            return key.encode()  # Return key as bytes
        else:
            print("Invalid key length. Please enter exactly 8 characters.")

# Padding to ensure data length is a multiple of 8
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Unpadding function
def unpad(text):
    return text.rstrip()


choice = int(input("Press\n 1 to use a random key\n 2 to use a key given by the user\n"))
if choice == 1:
    key = os.urandom(8)  # Generate a random 8-byte key
    print("Generated Key saved to file 'key.txt'")
else:
    key = get_valid_key()
    print("Your key is saved to 'key.txt' file")

# writing key in key.txt file
keyfile = open("key.txt", "w+")
keyfile.write("Key: " + key.hex())
keyfile.close()

cipher = DES.new(key, DES.MODE_ECB)

while True:
    # Input plaintext from user
    plaintext = input("Enter plain text: ")
    padded_text = pad(plaintext)

    # Encryption
    ciphertext = cipher.encrypt(padded_text.encode())
    print("Encrypted (hex):", ciphertext.hex())

    # Decryption
    decrypted_text = unpad(cipher.decrypt(ciphertext).decode())
    print("Decrypted:", decrypted_text)

    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() != 'yes':
        break
