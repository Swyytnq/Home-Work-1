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

    def print(self):
        print(f'--- {self.name} ---')
        print(f'HP: {self.health}')
        print(f'Damage: {self.damage}')
        print(f'Defence: {self.defence}')