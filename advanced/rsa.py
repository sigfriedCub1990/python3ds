#!/usr/bin/env python
import random
from modexp import ext_gcd, gcd_improved, modexp


def gen_keys(p, q):
    """There is a problem in this function it needs some debugging"""
    n = p * q
    m = (p - 1) * (q - 1)
    e = int(random.random() * n)
    while gcd_improved(m, e) != 1:
        e = int(random.random() * n)
    d, _, b = ext_gcd(m, e)
    if b < 0:
        d = m + b
    else:
        d = b
    return (e, d, n)


def encrypt(msg, pub_key, n):
    chunk_size = n.bit_length() // 8
    all_chunks = str_to_chunks(msg, chunk_size)
    return [modexp(msg_chunk, pub_key, n) for msg_chunk in all_chunks]


def decrypt(cipher_chunks, priv_key, n):
    chunk_size = n.bit_length() // 8
    plain_chunks = [modexp(cipher_chunk, priv_key, n) for cipher_chunk in cipher_chunks]
    return chunks_to_str(plain_chunks, chunk_size)


def str_to_chunks(msg, chunk_size):
    msg_bytes = bytes(msg, "utf-8")
    hex_str = "".join([f"{b:02x}" for b in msg_bytes])
    num_chunks = len(hex_str) // chunk_size
    chunk_list = []
    for i in range(0, num_chunks * chunk_size + 1, chunk_size):
        chunk_list.append(hex_str[i : i + chunk_size])
    chunk_list = [eval("0x" + x) for x in chunk_list if x]
    return chunk_list


def chunks_to_str(chunk_list, chunk_size):
    hex_list = []
    for chunk in chunk_list:
        hex_str = hex(chunk)[2:]
        clen = len(hex_str)
        hex_list.append("0" * ((chunk_size - clen) % 2) + hex_str)

    hstring = "".join(hex_list)
    msg_array = bytearray.fromhex(hstring)
    return msg_array.decode("utf-8")


if __name__ == "__main__":
    msg = "python"
    e, d, n = gen_keys(5563, 8191)
    c = encrypt(msg, e, n)
    print(f"Encrypted {c}")
    m = decrypt(c, d, n)
    print(f"Original {m}")
