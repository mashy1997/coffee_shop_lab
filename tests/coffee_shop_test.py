import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drinks import Drinks
from src.food import Food

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("Costa Coffee Branch 101", 1000)
        self.drink1 = Drinks("Mocha", 3, 2, 3)
        self.drink2 = Drinks("Espresso", 4, 5, 7)
        self.all_drinks = [self.drink1, self.drink2]
        self.food1 = Food("falafel_wrap", 5, 2)
        self.food2 = Food("brownie", 3, 4)
        self.all_foods = [self.food1, self.food2]



    def test_coffee_shop_has_name(self):
        self.assertEqual("Costa Coffee Branch 101", self.coffee_shop.name)
        # self.assertEqual(expected, actual)

    def test_increase_cash(self):
        self.coffee_shop.increase_cash_in_till(15) #action
        self.assertEqual(1015, self.coffee_shop.till) #results

    def test_putting_drinks_in_list(self): 
        self.coffee_shop.put_drinks_in_shop(self.all_drinks)
        self.assertEqual(2, len(self.coffee_shop.drinks))

    def test_customer_transaction(self):
        self.coffee_shop.put_drinks_in_shop(self.all_drinks)
        self.customer1 = Customer("Becca", 30, 21)
        self.coffee_shop.customer_transaction(self.drink2, self.customer1)
        self.coffee_shop.customer_transaction(self.drink1, self.customer1)
        self.coffee_shop.customer_food_transaction(self.food1, self.customer1)

        
        self.assertEqual(18, self.customer1.wallet)
        self.assertEqual(1012, self.coffee_shop.till)
        self.assertEqual(5, self.customer1.energy_level)

    # def test_check_coffee_shop_stock(self):
        
    #     self.assertEqual(37, self.coffee_shop.check_stock_value())



    

#Add caffeine_level to the Drink, and a energy level to the Customer. Every time a Customer buys a drink, the energy level should go up by the caffeine_level.