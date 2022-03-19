#!/usr/bin/env python


def rot13(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for letter in message:
        if letter in alphabet:
            pos = (alphabet.find(letter) + key) % 26
            encrypted += alphabet[pos]
        else:
            encrypted += " "

    return encrypted


def decrypt(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ""
    for letter in message:
        if letter in alphabet:
            pos = (alphabet.find(letter) + 26 - key) % 26
            decrypted += alphabet[pos]
        else:
            decrypted += " "

    return decrypted


if __name__ == "__main__":
    key = 13
    original = "the c programming language"
    print(f"Original message: {original}")
    enc = rot13(original, key)
    print(f"Encrypted message is: {enc}")
    dec = decrypt(enc, key)
    print(f"Encrypted message is: {dec}")
