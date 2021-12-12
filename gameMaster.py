import cases
import players
import random
import time
import choiceBet

print("Bienvenu sur le jeu de la roulette de casin'oline")
time.sleep(0.5)

def askPlayerInfos():
    players.player.creatPlayer()
    time.sleep(0.5)

def welcome():
    print("Bienvenu " +  str(players.player.profile[0].surname))
    time.sleep(0.5)


"""
renvoi les règles à l'utilisateur si il le souhaite
PRE :   "y", "yes", "oui", "ouaip", "ouais"
        "n", "no", "nope", "non", "nan"
POST :  print les règles si l'utilisateur répond positivement
        pass la fonction si l'utilisateur repond negativement
"""
def askPlayerRules():
    knowledge = input("Souhaitez-vous un bref rappel des règles ?")
    if knowledge == "y" or knowledge =="yes" or knowledge =="oui" or knowledge =="ouaip" or knowledge =="ouais":
        print("\n Une roue composée de 37 cases. Chacune d'elle comporte un chiffre ou une couleur.\n "
              "si vous pariez sur une couleur et gagnez, vous remportez 2 fois votre mise \n "
              "si vous pariez sur un chiffre et gagnez, vous remportez 36 fois votre mise\n")
        time.sleep(0.5)
    elif knowledge == "n" or knowledge =="no" or knowledge =="nope" or knowledge =="non" or knowledge =="nan":
        time.sleep(0.5)
    else:
        print("je n'ai pas compris")
        time.sleep(0.5)
        askPlayerRules()


"""
fonction qui compare le choix de la case aléatoire avec celui de l'utilisateur et renvoi si l'utilisateu à gagner ou perdu
"""
def turnOfWeel():
    cases.case.creatCase()

    tourRoulette = random.randrange(0, 37)
    print(cases.case.roulette[tourRoulette].color, cases.case.roulette[tourRoulette].number)
    print("la roue tourne")
    time.sleep(2)

    if choiceBet.choiceBet.betTemp[0].choice == cases.case.roulette[tourRoulette].color or choiceBet.choiceBet.betTemp[0].choice == cases.case.roulette[tourRoulette].number:
        print("vous avez gagné")
    else:
        print("vous avez perdu")




