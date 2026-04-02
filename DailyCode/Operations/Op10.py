message = input("Enter a message: ")
key = 7  # secret key

encrypted = ""
for ch in message:
    encrypted += chr(ord(ch) ^ key)

print("\nEncrypted message:", encrypted)


decrypted = ""
for ch in encrypted:
    decrypted += chr(ord(ch) ^ key)

print("Decrypted message:", decrypted)