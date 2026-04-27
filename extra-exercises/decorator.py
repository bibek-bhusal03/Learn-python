
class Coffee:
    def cost(self):
        return 100

class Milk:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 20

coffee = Coffee()

coffee = Milk(coffee)
print(f"debug cofee {coffee.cost()}")
