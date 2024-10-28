import string

def encrypt_char(char, key):
    """
    Encrypts a single character using Ceasar cipher.
    """
    if char.islower():
        return chr((ord(char) - ord('a') + key) % 26 + ord('a'))
    elif char.isupper():
        return chr((ord(char) - ord('A') + key) % 26 + ord('A'))
    else:
        return char


def decrypt_char(char, key):
    """
    Decrypts a single character using Ceasar cipher.
    """
    return encrypt_char(char, -key)


def encrypt_ceasar(text, key):
    """
    Encrypts a text using Ceasar cipher.
    """
    return ''.join(encrypt_char(char, key) for char in text)


def decrypt_ceasar(ciphertext, key):
    """Decryptes a text using Ceasar cipher.
    """
    return ''.join(decrypt_char(char, key) for char in ciphertext)


def break_ceasar(ciphertext):
    """
    Attempts to break the Ceasar cipher by trying all possible keys.
    """
    for key in range(1, 26): # Try all keys from 1 to 25
        decrypted_text = decrypt_ceasar(ciphertext, key)
        print(f"Key {key}: {decrypted_text}\n")


def main():
    ciphertext = """
    Jylbujm nby gimn zugiom nblyy qilxm onnylyx ch fcnylunoly, 
    “Yn no, Vlony?” (Ypyh sio, Vlonom?) nbcm yrjlymmcih bum wigy xiqh ch 
    bcmnils ni gyuh nby ofncguny vynlusuf vs ihy’m wfimymn zlcyhx. Nbcm mwyhy, 
    ch qbcwb nby wihmjclunilm ch nby Myhuny ummummchuny Wuymul, cm ihy iz 
    nby gimn xluguncw gigyhnm ih nby Mbueymjyulyuh mnuay. Nby uoxcyhwy bum 
    domn qcnhymmyx nby ulliauhwy uhx bovlcm iz u lofyl qbi bum mioabn, qcnbch 
    u lyjovfcw, ni vywigy u gihulwb, wigjulcha bcgmyfz ni nby aixm. Vlonom, u 
    zlcyhx iz Wuymul uhx syn u guh qbi fipym Ligy (uhx zlyyxig) gily, bum dichyx 
    nby wihmjclunilm ch nby ummummchuncih, u vynlusuf qbcwb cm wujnolyx vs nby 
    nblyy qilxm uvipy ch nbcm zugiom Mbueymjyuly koiny.
    """

    # Break the Ceasar cipher
    break_ceasar(ciphertext)


if __name__ == "__main__":
    main()
