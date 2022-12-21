#zde opakuji random 

import random
from words import words
import string 

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    user_letter = input("Typlni si písmeno:").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(used_letters)

    elif user_letter in used_letters:
        print("Tohle písmeno sí uz použil. Pouzí jiný")

    else:
        print("Neplatný charakter. Pouzí jiný")

print(hangman())


