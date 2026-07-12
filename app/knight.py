class Knight:
    def __init__(self, name, hp, power, armour, weapon, potion):
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare(self):
        self.protection = 0

        for piece in self.armour:
            self.protection += piece["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

    def check_hp(self):
        if self.hp <= 0:
            self.hp = 0

    def fight(self, enemy):
        self.hp -= enemy.power - self.protection
        enemy.hp -= self.power - enemy.protection

        self.check_hp()
        enemy.check_hp()


def create_knight(knight_data):
    knight = Knight(
        name=knight_data["name"],
        hp=knight_data["hp"],
        power=knight_data["power"],
        armour=knight_data["armour"],
        weapon=knight_data["weapon"],
        potion=knight_data["potion"],
    )

    knight.prepare()

    return knight
