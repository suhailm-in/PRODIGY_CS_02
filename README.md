# Image Encryption and Decryption Tool

This is a simple Python tool for encrypting and decrypting images using a basic pixel manipulation technique. The tool allows users to securely encrypt images and later decrypt them using the same key.

## Features

- **Encrypt Images**: Securely encrypt images by adding a specified key value to each pixel's RGB values.
- **Decrypt Images**: Restore the original image by subtracting the same key value from the encrypted image's pixel values.
- **Output Folder**: Automatically saves encrypted and decrypted images in an "output" folder. The folder is created if it doesn't exist.

# Resources
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

## Installation

### Step 1: Clone the repository
```bash
$ git clone https://github.com/suhailm-in/
$ cd 
```

### Step 2: Run the Installation Script
This will install the required Python packages: OpenCV and NumPy.
```bash
$ chmod +x install.sh
$ ./install_tools.sh
```
### Manual Installation

If you prefer to install manually, you can use the following command after ensuring that pip is installed:

```bash 
pip install opencv-python numpy
```

# Usage
### 1. Run the Tool
After installation, you can run the tool using:
```bash
python3 main.py
```
### 2. Choose an Operation
The tool will prompt you to choose between encrypting or decrypting an image.
### 3. Input the Image Path
Enter the full path of the image you wish to encrypt or decrypt.
### 4. Enter the Key
Provide an integer key for encryption/decryption. Ensure the key is between 0 and 255.
### 5. View and Save Output
The encrypted or decrypted image will be displayed, and you will have the option to save it in the `output` directory.


## Developed by
### Suhail M 
Ethical Hacker, Penetration Tester, and AI Researcher in Cybersecurity
<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://twitter.com/suhailm_in" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="suhailm_online" height="30" width="40" /></a>
<a href="https://linkedin.com/in/suhailm-in" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="suhailm-online" height="30" width="40" /></a></p>






