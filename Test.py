from Card import Card, Player
card1 = Card("spearman1", 10, [0.1, 0.1, 0.1, 0.1], [1, 1, 1, 1], [1, 1, 1], 2)
card2 = Card("swordsman", 15, [0.3, 0.3, 0.3, 0.3], [2, 2, 2, 2], [0.8, 0.8, 0.8], 3)
card3 = Card("cavalryman", 20, [0.5, 0.5, 0.5, 0.5], [5, 2, 3, 1], [0.6, 0.6, 0.6], 3)
player1 = Player("User", [card1, card2, card3])
j = 0
for i in player1.cards:
    i.setCoord(5, j)
    j+=1
card4 = Card("spearman", 10, [0.1, 0.1, 0.1, 0.1], [1, 1, 1, 1], [1, 1, 1], 2)
card5 = Card("swordsman", 15, [0.3, 0.3, 0.3, 0.3], [2, 2, 2, 2], [0.8, 0.8, 0.8], 3)
card6 = Card("cavalryman", 20, [0.5, 0.5, 0.5, 0.5], [5, 2, 3, 1], [0.6, 0.6, 0.6], 3)
player2 = Player("Enemy", [card4, card5, card6])
j = 0
for i in player2.cards:
    i.setCoord(0, j)
    j+=1
players = {"enemy": player2, "player": player1}
field = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
for i in players.keys():
    player = players.get(i)
    for j in player.cards:
        field[j.x][j.y] = j.name
for k in field:
    print(k)
a = True
while a:
    inputed = input().split(", ")
    user = ""
    for i in inputed:
        if inputed.index(i)==0:
            user = i
        #if inputed.index(i)==0:
            
