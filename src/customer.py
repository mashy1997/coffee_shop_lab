class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy_level = 0

    def decrease_money(self, amount):
        self.wallet -= amount

    def increase_energy_level(self, energy):
        self.energy_level += energy
    
    def decrease_energy_level(self, rej_energy):
        self.energy_level -= rej_energy
        

