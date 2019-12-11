import random

INVITE = 'Propose un nombre : '

QUIT_CONFIRM = 'Es-tu certain de vouloir quitter (O/n) ?'
QUIT_TXT = 'q'
QUITTER = -1
QUIT_MSG = 'Merci pour tout !'

def confirm_quit():
    confi = raw_input(QUIT_CONFIRM)
    if confi == 'n':
        return False
    else:
        return True

    
def jouer_tour():
    nbr_secret = random.randint(1, 100)
    nbr_saisies = 0
    nbr_saisies += 1
    while True:
        nbr_joueur = raw_input(INVITE)
        if nbr_joueur == QUIT_TXT:
            if confirm_quit():
                return QUITTER
            else:
                continue
        nbr_saisies += 1
        if nbr_secret == int(nbr_joueur):
            print('Correct !')
            return nbr_saisies
        elif nbr_secret > int(nbr_joueur):
            print("Trop petit")
        else:
            print("Trop grand")

total_tours = 0
total_saisies = 0
msg_stat = 0
         
while True:
    total_tours += 1
    print("On passe au tour " + str(total_tours))
    print("En avant les devinettes !")
    
    ce_tour = jouer_tour()

    if ce_tour == QUITTER:
        total_tours -= 1
        if total_tours == 0:
            mdg_stat = "1er tour pas fini ! " +\
                       "Tu veux recommencer ?"
        else:
            moy = str(total_saisies / float(total_tours))
            msg_stat = "Tu as fait " + str(total_tours) +\
                       " tours. Moyenne de " + str(moy)
        break

    total_saisies += ce_tour
    print("Tu as fait " + str(ce_tour) + " saisies.")
    moy = total_saisies / float(total_tours)
    print("Ta moyenne de saisies/tour est de " + str(moy))
    print(" ")

print(QUIT_MSG)
print(msg_stat)
