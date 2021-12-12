import time
import players
"""
definition de la class choiceBet avec les objets choice et bet afin de saisir le pari et
la mise de l'utilisateur pour les stocker dans un dictionnaire.
"""
class choiceBet:

    betTemp = {}

    @property
    def choice(self):
        return self.__choice
    @choice.setter
    def choice(self, choice):
        self.__choice

    @property
    def bet(self):
        return self.__bet
    @bet.setter
    def bet(self, bet):
        self.__bet = bet

    def __init__(self, choice, bet):
        self.__choice = choice
        self.__bet = bet
    """
    demande à l'utilisateur son pari et sa mise 
    
    PRE :   pour le pari :      -  0 > int > 37
                                - "rouge" ou "noir"
            pour la mise :      - 0 > int
    POST :  le pari et la mise sont enregistrés dans le dictionnaire "betTemp"
    """
    def askChoiceBet():

        validChoice = False
        validBet = False

        while not validChoice:
            choiceTemp = input("Sur quoi souhaitez-vous parrier ?")

            try:
                choiceTemp = int(choiceTemp)
                if choiceTemp:
                    if choiceTemp in range (1, 37):
                        print("votre pari est placé")
                        validChoice = True
                    else:
                        print("Si vous pariez sur un nombre il doit se situer entre 1 et 36 inclus ")
                else:
                    if choiceTemp == "rouge" or choiceTemp == "noir":
                        print("votre pari est placé")
                        validChoice = True
                    else:
                        pass

            except:
                if choiceTemp == "rouge" or choiceTemp == "noir":
                    validChoice = True
                else:
                    print(
                        "Vous pouvez parier soit sur la couleur d'une case (rouge ou noir) soit sur son numéro (ede 1 et 36)")


        while not validBet:
            tempBet = int(input("Combien souhaitez-vous miser ?"))
            if tempBet <= players.player.profile[0].wallet:
                validBet = True
                time.sleep(0.3)
            else:
                print("Le montant de votre mise ne peut excéder la valeur de votre wallet qui s'élève à " + str(players.player.profile[0].wallet))
                time.sleep(0.3)

        if validChoice == True and validBet == True:
            choiceBet.betTemp[0]=choiceBet((choiceTemp), (tempBet))
            print("votre pari est placé")

        time.sleep(1)

