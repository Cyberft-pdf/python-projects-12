import random 

def play():
    user = input("Jaká je tvoje volba: R pro kámen, p pro papír, s pro nuzky\n")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "Je\" remíza"
    
    if is_win(user, computer):
        return "Ty si vyhrál"

    return "prohrál si:("


def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
        or (player == "p" and opponent == "r"):
        return True 



#z nějákeho důvodu to nefunguje, fakt nevím :(

