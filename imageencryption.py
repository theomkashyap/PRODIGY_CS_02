from PIL import Image

print("IMAGE ENCRYPTION/DECRYPTION PROGRAM")

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            encrypted_pixel = (b, g, r)
            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            decrypted_pixel = (b, g, r)
            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

input_image = r"C:\Users\theom\Desktop\sample.jpg"
encrypted_image = r"C:\Users\theom\Desktop\encrypted_image.jpg"
decrypted_image = r"C:\Users\theom\Desktop\decrypted_image.jpg"

encrypt_image(input_image, encrypted_image, key=None)
decrypt_image(encrypted_image, decrypted_image, key=None)
