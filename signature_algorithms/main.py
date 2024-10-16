import time
import uuid
import hashlib
import codecs
import random
import string

shared_key = "TurnOnTheLights!"
base_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_base(number, base):
    result = ""
    while number:
        result += base_string[number % base]
        number //= base
    return result[::-1] or "0"

def randstring(size):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))    

def main():
    algs = [
        "md5",
        "sha1",
        "sha224",
        "sha256",
        "sha384",
        "sha512",
        "sha3_224",
        "sha3_256",
        "sha3_384",
        "sha3_512",
        "shake_128",
        "shake_256",
        "blake2b",
        "blake2s"
    ]

    plaintext = f"1:w:b:{str(uuid.uuid4()).lower()}:{int(time.time())}"

    for a in algs:
        #import pdb;pdb.set_trace()
        h = hashlib.new(a, shared_key.encode('utf-8'))
        print(f"{a} Digest Size: {h.digest_size} Block Size: {h.block_size}")
        print(f"Plaintext: {plaintext} length={len(plaintext)}")
        try:
            h.update(plaintext.encode('utf-8'))
            d = h.hexdigest()
            ba = codecs.decode(d, 'hex_codec')
            b36 = to_base(int.from_bytes(ba, 'little'), 36)
            ciphertext = f"{plaintext}:{d}"
            print(f"Cipher: {ciphertext} length={len(ciphertext)}")
            b36_cipher = f"{plaintext}:{b36}"
            print(f"b36: {b36_cipher} length={len(b36_cipher)}")
            print(f"Algo = {a} {len(d)} {d}")
        except Exception as e:
            print(f"{a} {e}")
        print("----------------------------")
if __name__ == "__main__":
    main()