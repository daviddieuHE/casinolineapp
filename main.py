import gameMaster
import asciiArt
import choiceBet

if __name__ == "__main__":
    gameMaster.askPlayerInfos()
    gameMaster.welcome()
    gameMaster.askPlayerRules()
    asciiArt.rouletteGraphic()
    choiceBet.choiceBet.askChoiceBet()
    gameMaster.turnOfWeel()
