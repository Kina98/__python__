class Vehicule:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along ..")

    def get_make_model(self):
        print(f"I'am {self.make} {self.model}")

mycar = Vehicule("Tesla", "Model 3")

# print(mycar.make)
# print(mycar.model)
mycar.get_make_model()
mycar.moves()

yourcar = Vehicule("Toyota", "Hilux")

yourcar.get_make_model()
yourcar.moves()


class Airplane(Vehicule):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies along ..")

class Truck(Vehicule):
    def moves(self):
        print("Rumbles along ..")

class Golfcart(Vehicule):
    pass

cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'pinnacle')
golfwagon = Golfcart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print('\n\n')

for v in (mycar, yourcar, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()