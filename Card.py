class Card(object):
    def __init__(self, name, health, aramor, damage, side, amountOfAction):
        self.name = name
        self.health = health
        self.armor = aramor
        self.damage = damage
        self.amountOfAction = amountOfAction
        self.side = side
        self.amountOfActions = amountOfAction
        self.x = 0
        self.y = 0
        self.alife = True
        self.fortune = 0.01

    def setCoord(self, x, y):
        self.x = x
        self.y = y

    def getDamag(self, list, side):
        for i in range (len(list)):
            self.health -= list[i]*(1 - self.armor[i])*self.side
        if self.health <=0:
            self.alife = False

    def giveDamag (self, card):
        card.getDamag(card, self.damage)

    def move (self, x1, y1):
        self.amountOfActions -= 1
        self.x += x1
        self.y += y1

    def reset(self):
        self.amountOfActions = self.amountOfAction

    def wait(self):
        self.amountOfActions = 0

    def dice(self):
        self.fortune = self.fortune
    def outCooords(self):
        return [self.x, self.y]
class Player (object):

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
