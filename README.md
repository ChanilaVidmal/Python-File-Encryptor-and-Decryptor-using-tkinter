# File Encryptor

This is a Python application that allows you to encrypt and decrypt files using the Fernet encryption algorithm from the `cryptography` library. The application provides a graphical user interface (GUI) built with the `tkinter` library.
## Features

- Encrypt a file: Select a file from your system and encrypt it using a randomly generated encryption key.
- Export encryption key: Option to export the encryption key to a separate file for future use.
- Copy encryption key to clipboard: Option to copy the encryption key to the clipboard for easy sharing or storage.
- Decrypt a file: Select an encrypted file and provide the encryption key to decrypt it.


## Prerequisites

Make sure you have the following dependencies installed:
- Python 3.11
- `clipboard==0.0.4` library
- `cryptography==39.0.0` library
- `psutil==5.9.4` library

You can install the required libraries using pip:
```console
pip install -r requirements.txt
```
## Usage

1. Clone the repository or download the source code files.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the following command to execute the application:


```console
main.py
```
4. The File Encryptor GUI window will appear.
5. Select the operation (Encrypt or Decrypt) from the dropdown menu.

### Encrypt

1. Select the "Encrypt" option from the dropdown menu.

2. Click the "Select File" button and choose the file you want to encrypt.

3. Optionally, you can choose the following options:

- **Export encryption key**: Check this option to export the encryption key to a separate file.
- **Copy encryption key to clipboard**: Check this option to copy the encryption key to the clipboard.

4. Click the "Encrypt" button to encrypt the selected file.

### Decrypt

1. Select the "Decrypt" option from the dropdown menu.

2. Click the "Select File" button and choose the encrypted file you want to decrypt.

3. Choose one of the following options to provide the encryption key:

- **Select key file**: Check this option to select a file containing the encryption key.
- **Enter key manually**: Check this option to manually enter the encryption key.

4. Click the "Decrypt" button to decrypt the selected file.
## Notes

- If you choose to export the encryption key or copy it to the clipboard, make sure to keep it secure and accessible for future decryption.

- The application provides basic error handling and validation. However, it's always recommended to have backups of your important files before performing any encryption or decryption operations.

- The GUI is designed for simplicity and ease of use. You can customize the GUI elements and styling according to your preferences.
## License

- [Copyright (c) 2023 Chanila Vidmal](https://github.com/ChanilaVidmal)

- [Attribution-NonCommercial-NoDerivatives 4.0 International](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode)
## Acknowledgements

 - This project utilizes the `tkinter` library for building the GUI.
 - The encryption and decryption functionality is provided by the `cryptography` library.
 - The `psutil` library is used to retrieve the current user's name for default file paths.


## Authors

- [@ChanilaVidmal](https://github.com/ChanilaVidmal)

