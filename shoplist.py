class FoodOrder:
    def __init__(self, food, amount):
        self.__food_name = food
        self.__amount_in_pounds = amount
        self.__standard_price = self.__set_standard_price()
        self.__calculated_price = self.calculate_cost()

    def __set_standard_price(self):
        prices = {
            'Dry Cured Iberian Ham': 177.80,
            'Wagyu Steaks': 450.00,
            'Matsutake Mushrooms': 272.00,
            'Kopi Luwak Coffee': 306.50,
            'Moose Cheese': 487.20,
            'White Truffles': 3600.00,
            'Blue Fin Tuna': 3603.00,
            'Le Bonnotte Potatoes': 270.81
        }
        return prices.get(self.__food_name, 0.00)

    def calculate_cost(self):
        return self.__amount_in_pounds * self.__standard_price

    def get_food_name(self):
        return self.__food_name

    def get_amount_in_pounds(self):
        return self.__amount_in_pounds

    def get_standard_price(self):
        return self.__standard_price

    def get_calculated_price(self):
        return self.__calculated_price

    def __str__(self):
        return f"Item: {self.__food_name}\nAmount ordered: {self.__amount_in_pounds} pounds\nPrice per pound: ${self.__standard_price:.2f}\nPrice of order: ${self.__calculated_price:.2f}"
