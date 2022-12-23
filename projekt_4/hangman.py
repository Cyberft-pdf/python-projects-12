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

    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print("Zbýváti",lives, "životů už si použil tyhle slova: ", " ". join(used_letters))
        print(" ")
        word_list= [letter if letter in used_letters else "-" for letter in word] 
        print("Slovo které máte ted: "," ".join(word_list))
        print(" ")

        user_letter = input("Typlni si písmeno:").upper()
        print(" ")
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 
                print("Písmenko není ve slově.")
                print(" ")

        elif user_letter in used_letters:
            print("Tohle písmeno sí uz použil. Pouzí jiný")
            print(" ")

        else:
            print("Neplatný charakter. Pouzí jiný")
            print(" ")
    if lives == 0:
        print("Promin, prohrál si:(", word)
    else:
        print("Uhodl si správné slovo", word, ":)")

        
hangman()


