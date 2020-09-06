"""
This crackme is made by Crudd and was uploaded on crackmes.de under the name Splish Splash
"""

import operator


def generate_key(name):
    serial_key = [(operator.xor(ord(letter) % 10, count) + 4) % 10 for count, letter in enumerate(name)]
    return ''.join(str(number) for number in serial_key)


if __name__ == '__main__':
    serial = generate_key(name="steven")
    print(f"Key is {serial}")
