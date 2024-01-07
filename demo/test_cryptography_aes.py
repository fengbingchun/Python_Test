import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Blog: https://blog.csdn.net/fengbingchun/article/details/135436712

def aes_gcm_encrypt(plain_text, key, iv, aad):
    # Construct an AES-GCM Cipher object with the given key and iv
    encryptor = Cipher(algorithms.AES(key), modes.GCM(iv),).encryptor()

    # associated_data will be authenticated but not encrypted, it must also be passed in on decryption
    encryptor.authenticate_additional_data(aad)

    # Encrypt the plaintext and get the associated ciphertext. GCM does not require padding
    cipher_text = encryptor.update(plain_text) + encryptor.finalize()

    return (cipher_text, encryptor.tag)

def aes_gcm_decrypt(cipher_test, key, iv, aad, tag):
    # Construct a Cipher object, with the key, iv, and additionally the GCM tag used for authenticating the message
    decryptor = Cipher(algorithms.AES(key), modes.GCM(iv, tag),).decryptor()

    # We put associated_data back in or the tag will fail to verify when we finalize the decryptor
    decryptor.authenticate_additional_data(aad)

    # Decryption gets us the authenticated plaintext. If the tag does not match an InvalidTag exception will be raised
    return decryptor.update(cipher_test) + decryptor.finalize()

if __name__ == "__main__":
    # reference: https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
    plain_test = b"https://github.com/fengbingchun"
    key = os.urandom(32) # bytes, secret key: either 128, 192, or 256 bits long
    iv = os.urandom(12) # bytes, initialisation vector
    aad = os.urandom(16) # authenticated encryption with additional data
    print("key: {}\niv: {}\naad: {}\n".format(key, iv, aad))

    cipher_text, tag = aes_gcm_encrypt(plain_test, key, iv, aad)
    print("cipher text: {}\ntag: {}\n".format(cipher_text, tag))

    plain_test2 = aes_gcm_decrypt(cipher_text, key, iv, aad, tag)
    print("before encryption, plaintext:{}\nafter  decryption, plaintext:{}".format(plain_test, plain_test2))

    if plain_test != plain_test2:
        print("Error: the decrypted content does not match the original plaintext")
        raise

    print("test finish")
