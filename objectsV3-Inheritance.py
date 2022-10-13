class Game:
    def __init__(self, name, gameStudio):
        self.name = name;
        self.gameStudio = gameStudio
    def printTheGame(self):
        print("Game: " + self.name + ", is: " + self.category + " category, gameStudio is: " + self.gameStudio)

class SandBox(Game):
    category = 'Sandbox'
    def __init__(self, name, gameStudio, platform):
        self.platform = platform
        Game.__init__(self, name, gameStudio)
        print("Platform: " + self.platform)

sandBox = SandBox("GTA V", "Rockstar", 'Epic')
print(sandBox.printTheGame)
sandBox.printTheGame()