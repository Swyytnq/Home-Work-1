from character import Character

player1 = Character('Sigismund', damage=3)
player2 = Character('Brundmir', health=35)


print(player1)
print(player2)

player1.attack(player2)

print(player1)
print(player2)