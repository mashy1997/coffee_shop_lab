class CoffeeShop:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        

    def increase_cash_in_till(self, amount):
        self.till += amount 

    def put_drinks_in_shop(self, drinks):
        for drink in drinks:
            self.drinks.append(drink)

    def customer_transaction(self, drink, customer):
        if customer.age >= 16 and customer.energy_level <= 9:
            self.increase_cash_in_till(drink.price)
            customer.decrease_money(drink.price)
            customer.increase_energy_level(drink.caff_level)
        
    def customer_food_transaction(self, food, customer):
        self.increase_cash_in_till(food.price)
        customer.decrease_money(food.price)
        customer.decrease_energy_level(food.rej_level)

    # def drinks_add_dict(self, drinks_list):


    # def check_stock_value(self):
    #     total_value = 0
    #     for drink in self.drinks:
    #         total_value += (drink.price * drink.stock)

    #     return total_value

