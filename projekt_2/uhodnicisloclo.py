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

def computer_guess(x):
    low = 1
    hight = x
    feedback = ""
    while feedback != "c" : 
        if low != hight:
            guess = random.randint(low, hight)
        else: 
            guess = low 
        feedback = input(f"Je {guess} moc vysoký (H), moc malý(L) nebo správně(C):").lower()
        if feedback == "h":
            hight = guess - 1
        elif feedback == "l":
            low = guess + 1


    print("Ano! pocitac uhodl tvoje císlo:)")



computer_guess(10) # Tady se upravuje rozhraní, odkud počítač bude vybírat císlo napr. 1 az 10 
