from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Blog: https://blog.csdn.net/fengbingchun/article/details/135436712

def rsa_public_key_encrypt(plain_text, public_key):
    return public_key.encrypt(
        plain_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def rsa_private_key_decrypt(cipher_test, private_key):
    return private_key.decrypt(
        cipher_test,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

if __name__ == "__main__":
    # reference: https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
    plain_test = b"https://blog.csdn.net/fengbingchun/"

    with open("test_data/rsa_private.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None,)

    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    #print("private key: {}\n".format(pem.splitlines()))

    public_key = private_key.public_key()
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    #print("public key: {}\n".format(pem.splitlines()))

    cipher_text = rsa_public_key_encrypt(plain_test, public_key)
    print("cipher text:{}\n".format(cipher_text))

    plain_test2 = rsa_private_key_decrypt(cipher_text, private_key)
    print("before encryption, plaintext:{}\nafter  decryption, plaintext:{}".format(plain_test, plain_test2))

    if plain_test != plain_test2:
        print("Error: the decrypted content does not match the original plaintext")
        raise

    print("test finish")
