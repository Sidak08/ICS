# SuperSpy Encryption Suite

## Overview

The SuperSpy Encryption Suite is a sophisticated cryptographic software package designed to facilitate the secure encoding and decoding of textual data. This suite comprises three primary components: `Encryption.py`, `EncryptionUI.py`, and `FileAccess.py`. Each module is meticulously crafted to ensure robust encryption and decryption processes, leveraging both manual and automated key generation methodologies.

## Components

### Encryption.py

#### Description

`Encryption.py` is the core encryption module responsible for the dynamic generation of encryption keys, as well as the encoding and decoding of individual characters and entire sentences using a advanced cryptographic algorithm. The module is designed to handle various character types, including uppercase letters, lowercase letters, and special characters.

### EncryptionUI.py

#### Description

`EncryptionUI.py` provides a graphical user interface (GUI) for the SuperSpy Encryption Suite, enabling users to interact with the encryption and decryption functionalities in a user-friendly manner. The GUI is built using the Tkinter library and supports both manual and automatic key generation modes.

### FileAccess.py

#### Description

`FileAccess.py` is responsible for file operations, including loading the contents of a text file into a list and saving a list of phrases to a new file. This module ensures seamless integration with the encryption and decryption processes.

## Usage

### Running the GUI

To launch the graphical user interface, execute the `EncryptionUI.py` script. This will open a window where you can input messages or file names for encryption and decryption. The GUI supports both manual and automatic key generation modes, which can be toggled using radio buttons.

### Encrypting and Decrypting Files

1. **Encrypting a File**:
   - Enter the name of the input file in the "Enter File Name" field.
   - Enter the desired name for the output file in the "Enter Output File Name" field.
   - Click the "Done" button to encrypt the file.

2. **Decrypting a File**:
   - Enter the name of the input file in the "Enter File Name" field.
   - Enter the desired name for the output file in the "Enter Output File Name" field.
   - Click the "Done" button to decrypt the file.

### Encrypting and Decrypting Messages

1. **Encrypting a Message**:
   - Enter the message in the "Enter Message" field.
   - If in manual mode, enter the encryption key in the "Enter Encryption Key" field.
   - The encrypted message will be displayed in the "Encrypted Output" field.

2. **Decrypting a Message**:
   - Enter the message in the "Enter Message" field.
   - If in manual mode, enter the decryption key in the "Enter Decryption Key" field.
   - The decrypted message will be displayed in the "Decrypted Output" field.

## Testing

The `if __name__ == "__main__":` blocks in each module contain test cases to validate the functionality of the respective functions. These tests can be executed by running the scripts individually.

## Dependencies

- Python 3.x
- Tkinter library (for GUI)

## Authors

- Sidak Singh

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Special thanks to me for putting the effort and finishing this project. I am proud of myself. Hope you liked it :)
