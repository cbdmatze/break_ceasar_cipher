

# Caesar Cipher Breaker

## Overview

The **Caesar Cipher Breaker** is a Python program designed to:
1. Encrypt and decrypt text using the Caesar cipher, a classic substitution cipher that shifts each letter of the text by a fixed number of positions.
2. Attempt to **break a Caesar cipher** encrypted message by brute-forcing all possible shift keys and displaying the decrypted text for each key. This allows users to find the correct decryption even when the key is unknown.

## Features

- **Encrypt text**: Encrypts a given string using the Caesar cipher with a specified key.
- **Decrypt text**: Decrypts a Caesar cipher-encrypted string using a known key.
- **Break Caesar cipher**: Attempts to crack an encrypted message with an unknown key by trying all possible shifts (from 1 to 25).
- **Supports upper and lower-case letters**: The program preserves the case of letters during encryption/decryption.
- **Handles special characters and spaces**: The program leaves punctuation, spaces, and special characters unmodified during encryption and decryption.

## Getting Started

### Prerequisites

- **Python 3.x** must be installed on your system.

### Installation

1. Clone the repository or download the `caesar.py` file.

   ```bash
   git clone https://github.com/yourusername/caesar-cipher-breaker.git
   cd caesar-cipher-breaker
   ```

2. Ensure you have Python 3.x installed. You can check by running:

   ```bash
   python3 --version
   ```

### Usage

The main script provides several functions for encryption, decryption, and breaking the Caesar cipher.

#### 1. Encrypting a Message

To encrypt a message using a Caesar cipher, call the `encrypt_caesar()` function with the message and the key.

Example:
```python
from caesar import encrypt_caesar

# Encrypt message
message = "Learning Python is Fun!"
key = 3
encrypted_message = encrypt_caesar(message, key)
print(encrypted_message)  # Output: Ohduqlqj Sbwkrq lv Ixq!
```

#### 2. Decrypting a Message

If you know the encryption key, you can decrypt the message by calling the `decrypt_caesar()` function.

Example:
```python
from caesar import decrypt_caesar

# Decrypt message
ciphertext = "Ohduqlqj Sbwkrq lv Ixq!"
key = 3
decrypted_message = decrypt_caesar(ciphertext, key)
print(decrypted_message)  # Output: Learning Python is Fun!
```

#### 3. Breaking the Caesar Cipher

If the key is unknown, use the `break_caesar()` function to try all possible keys and print the resulting decrypted text for each one.

Example:
```python
from caesar import break_caesar

# Ciphertext with unknown key
ciphertext = """
Jylbujm nby gimn zugiom nblyy qilxm onnylyx ch fcnylunoly, “Yn no, Vlony?” 
(Ypyh sio, Vlonom?) nbcm yrjlymmcih bum wigy xiqh ch bcmnils ni gyuh nby 
ofncguny vynlusuf vs ihy’m wfimymn zlcyhx. Nbcm mwyhy, ch qbcwb nby wihmjclunilm
"""

# Break Caesar cipher
break_caesar(ciphertext)
```

The program will print the possible decryptions for each key (1 to 25). The user can visually inspect the output to find the correct decryption.

### Example Output (Brute Force Decryption)

When you run `break_caesar()` on an encrypted message, the program will try each key and print the resulting text. Example output:

```
Key 1: Kzmcvkn ocz hjon avhjp ncmzz rjmyo poozozy di gdozmovomz, “Zo op, Wmpoz?”
...
Key 5: Mdpweqp qez ilop bxjns pdobb tknqo rrpszsy fk hetprsxrqp, “Bp qr, Yrnqp?”
...
Key 10: Jylbujm nby gimn zugiom nblyy qilxm onnylyx ch fcnylunoly, “Yn no, Vlony?”
...
```

## Code Structure

- `encrypt_char(char, key)`: Encrypts a single character using the Caesar cipher.
- `decrypt_char(char, key)`: Decrypts a single character using the Caesar cipher.
- `encrypt_caesar(text, key)`: Encrypts a text string using the Caesar cipher.
- `decrypt_caesar(ciphertext, key)`: Decrypts a Caesar cipher-encrypted string using the key.
- `break_caesar(ciphertext)`: Attempts to decrypt a Caesar cipher-encrypted message with an unknown key by brute-forcing all possible keys.

## Running the Program

To run the program:

```bash
python3 caesar.py
```

If you include the breaking function in the main program, it will try to break the cipher and output the results for each possible key.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
