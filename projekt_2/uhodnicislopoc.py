#zde opakuji random 

import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Uhádni číslo mezi 1 a {x}:"))
        if guess < random_number :
            print("Promin tvoje císlo je moc malé")
        elif guess > random_number:
            print("Tvoje cislo je moc vysoke:")
    
    print("Gratuluju, nasel si císlo:)")

guess(10)

