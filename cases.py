class case:
    """
    sert à la création des cases de la roulette et contient le dictionnaire roulette qui contient les cases
    """
    roulette = {}

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number):
        self.__number = number

    def __init__(self, color, number):
        self.__color = color
        self.__number = number

    @staticmethod
    def creatCase():
        """
        fonction qui sert à initialiser la roulette
        :return: none
        """
        case.roulette[0]=case("vert", 0)
        case.roulette[1]=case("rouge", 1)
        case.roulette[2]=case("noir", 2)
        case.roulette[3]=case("rouge", 3)
        case.roulette[4]=case("noir", 4)
        case.roulette[5]=case("rouge", 5)
        case.roulette[6]=case("noir", 6)
        case.roulette[7]=case("rouge", 7)
        case.roulette[8]=case("noir", 8)
        case.roulette[9]=case("rouge", 9)
        case.roulette[10]=case("noir", 10)
        case.roulette[11]=case("noir", 11)
        case.roulette[12]=case("rouge", 12)
        case.roulette[13]=case("noir", 13)
        case.roulette[14]=case("rouge", 14)
        case.roulette[15]=case("noir", 15)
        case.roulette[16]=case("rouge", 16)
        case.roulette[17]=case("noir", 17)
        case.roulette[18]=case("rouge", 18)
        case.roulette[19]=case("rouge", 19)
        case.roulette[20]=case("noir", 20)
        case.roulette[21]=case("rouge", 21)
        case.roulette[22]=case("noir", 22)
        case.roulette[23]=case("rouge", 23)
        case.roulette[24]=case("noir", 24)
        case.roulette[25]=case("rouge", 25)
        case.roulette[26]=case("noir", 26)
        case.roulette[27]=case("rouge", 27)
        case.roulette[28]=case("noir", 28)
        case.roulette[29]=case("noir", 29)
        case.roulette[30]=case("rouge", 30)
        case.roulette[31]=case("noir", 31)
        case.roulette[32]=case("rouge", 32)
        case.roulette[33]=case("noir", 33)
        case.roulette[34]=case("rouge", 34)
        case.roulette[35]=case("noir", 35)
        case.roulette[36]=case("rouge", 36)