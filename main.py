from character import Character
from random import randint

player1 = Character('Sigismund', damage=randint(1, 10), health=randint(50, 100))
player2 = Character('Brundmir', damage=randint(1, 10), health=randint(50, 100))


print(player1)
print(player2)

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    player2.attack(player1)
    print('=================')
    print(player1)
    print(player2)
