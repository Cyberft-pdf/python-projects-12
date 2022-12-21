import random 
jmeno = input("Napiš jak se jmenuješ:")
print(jmeno)


def play():
    user = input("Jaká je tvoje volba: R pro kámen, p pro papír, s pro nuzky\n")
    computer = random.choice(["r", "p", "s"])
    print("ahoj1")
    if user == computer:
        return "Je\" remíza"
    print("ahoj2")
    if is_win(user, computer):
        return "Ty si vyhrál"
    print("ahoj3")
    return "prohrál si:("


def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
        or (player == "p" and opponent == "r"):
        print("ahoj4")
        return True 

print(play())

#z nějákeho důvodu to nefunguje, fakt nevím :(

