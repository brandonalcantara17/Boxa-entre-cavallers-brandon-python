import random

class Boxer:
    def __init__(self, nom, hp):
        self.nom = nom
        self.hp = hp
        self.parts = ["cap", "panxa", "esquerra", "dreta"]

    def block(self):
        return random.sample(self.parts, 3)

    def hit(self):
        return random.choice(self.parts)

    def recieved(self):
        self.hp -= 1

    def fall(self):
        return self.hp <= 0

def combat(b1, b2):
    print(f"Combat entre {b1.nom} i {b2.nom}")
    print("-------------------------------------")

    turn = 0
    while True:
        attack = b1 if turn % 2 == 0 else b2
        defend = b2 if turn % 2 == 0 else b1

        part_hit = attack.hit()
        part_blocked = defend.block()

        if part_hit in part_blocked:
            print(f"— {attack.nom} pica: Protegit")
        else:
            print(f"— {attack.nom} pica: Cop a {part_hit}")
            defend.recieved()

        if defend.fall():
            print(f"{defend.nom} CAU!")
            print(f"GUANYADOR: {attack.nom}")
            break

        turn += 1

def main():
    nom1 = "Matxaca"
    hp1 = 10
    nom2 = "Destrossa"
    hp2 = 10

    b1 = Boxer(nom1, hp1)
    b2 = Boxer(nom2, hp2)
    combat(b1, b2)

if __name__ == "__main__":
    main()