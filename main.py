import cv2
import numpy as np
import os


def encrypt_image(image, key):
    encrypted_image = image.copy()
    rows, cols, channels = encrypted_image.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(channels):
                encrypted_image[i, j, k] = (encrypted_image[i, j, k] + key) % 256
    return encrypted_image


def decrypt_image(encrypted_image, key):
    decrypted_image = encrypted_image.copy()
    rows, cols, channels = decrypted_image.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(channels):
                decrypted_image[i, j, k] = (decrypted_image[i, j, k] - key) % 256
    return decrypted_image


def main():
    # Create output directory if it doesn't exist
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("Pixel Manipulation for Image Encryption:")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter your choice (1 - 2): ")

    if choice == '1':
        image_path = input("Enter the path to the image: ")

        # Check if the file exists
        if not os.path.isfile(image_path):
            print("Error: Image file not found.")
            return

        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            print("Error: Unable to read the image file. Ensure the path is correct and the file is a valid image.")
            return

        key = input("Enter the encryption key (integer): ")
        try:
            key = int(key)
        except ValueError:
            print("Error: Key must be an integer.")
            return

        encrypted_image = encrypt_image(image, key)
        cv2.imshow("Encrypted Image", encrypted_image)
        cv2.waitKey(0)

        encrypted_image_path = os.path.join(output_dir, "encrypted_image.png")
        cv2.imwrite(encrypted_image_path, encrypted_image)
        print(f"Encrypted image saved as {encrypted_image_path}")

        cv2.destroyAllWindows()

    elif choice == '2':
        image_path = input("Enter the path to the encrypted image: ")

        # Check if the file exists
        if not os.path.isfile(image_path):
            print("Error: Image file not found.")
            return

        # Read the image
        encrypted_image = cv2.imread(image_path)
        if encrypted_image is None:
            print("Error: Unable to read the image file. Ensure the path is correct and the file is a valid image.")
            return

        key = input("Enter the decryption key (integer): ")
        try:
            key = int(key)
        except ValueError:
            print("Error: Key must be an integer.")
            return

        decrypted_image = decrypt_image(encrypted_image, key)
        cv2.imshow("Decrypted Image", decrypted_image)
        cv2.waitKey(0)

        decrypted_image_path = os.path.join(output_dir, "decrypted_image.png")
        cv2.imwrite(decrypted_image_path, decrypted_image)
        print(f"Decrypted image saved as {decrypted_image_path}")

        cv2.destroyAllWindows()

    else:
        print("Invalid choice, exiting the program.")


if __name__ == '__main__':
    main()
