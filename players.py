import time

class player:

    profile = {}
    betTemp = {}

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def wallet(self):
        return self.__wallet
    @wallet.setter
    def wallet(self, wallet):
        self.__wallet = wallet



    def __init__(self, surname, wallet):
        self.__surname = surname
        self.__wallet = wallet

    def creatPlayer():
        """
        fonction qui sert à créer le profil du joueur en lui demandant son surnom ainsi que la valeur de son wallet
        PRE :   pour le surnom :    - minimum 3 caractères
                pour le wallet :    - 0 > int
        POST :
        """
        #player.profile[0]=player((input("Quel est votre surnom ?")), int((input("Quelle est la valeur de votre wallet ?"))))

        validSurname = False
        validWallet = False
        while not validSurname:
            surnameTemp = input("Quel est votre surnom ?")
            if len(surnameTemp) >= 3:
                validSurname = True
                time.sleep(0.3)
            else:
                print("votre surnom doit comporter minimum 3 caractères")
                time.sleep(0.3)

        while not validWallet:
            walletTemp = input("Combien comporte votre wallet?")
            try:
                walletTemp = int(walletTemp)
                if walletTemp >= 1:
                    validWallet = True
                else:
                    print("votre wallet doit comporter au moins 1 token")
                    time.sleep(0.3)
            except:
                print("Veuillez entrer un nombre naturel")
        if validWallet == True and validSurname == True:
            player.profile[0] = player((surnameTemp), (walletTemp))
