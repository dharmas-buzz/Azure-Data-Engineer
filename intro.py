class Grandfather:
def house(self):
    print("Grandfather's House")

class Father(Grandfather):
    def guest_house(self):
        print("Father's guest house")

class Son(Father):
    def car(self):
        print("Son won a car")

clild = Son()
child.house()
child.guest_house()
child.car()

print(house)