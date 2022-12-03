class Character:
    name = ''
    health = 100
    damage = 1
    defence = 0

    def __init__(self, name, health=100, damage=1, defence=0 ):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence

    def __str__(self):
        return f'--- {self.name} ---\n' \
            f'HP: {self.health} \n' \
            f'Damage: {self.damage} \n' \
            f'Defence: {self.defence} \n'





    def print(self):
        print(f'--- {self.name} ---')
        print(f'HP: {self.health}')
        print(f'Damage: {self.damage}')
        print(f'Defence: {self.defence}')

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, target):
        target.take_damage(self.damage)
        print('Attack!')