import string
import random

def generate_password(characters: int) -> str:
    charList = string.ascii_letters + string.digits + string.punctuation
    pw = ''

    for _ in range(characters):
        char = charList[random.randint(0, len(charList)-1)]
        pw = pw + char

    return pw



print(generate_password(10))