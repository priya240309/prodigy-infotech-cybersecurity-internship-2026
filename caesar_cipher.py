def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# User input
print("=== Caesar Cipher Encryption/Decryption ===")
choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

if choice == 'e':
    encrypted = encrypt(message, shift)
    print(f"Encrypted message: {encrypted}")
elif choice == 'd':
    decrypted = decrypt(message, shift)
    print(f"Decrypted message: {decrypted}")
else:
    print("Invalid choice. Enter 'e' or 'd'.")
