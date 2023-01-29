class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = f"{self.name} serves {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} is open to serve all."
        print(f"\n{msg}")

restaurant = Restaurant('In n Out', 'borger')
restaurant.describe_restaurant()



restaurant = Restaurant("Mickey D's", "chicken nuggies")
restaurant.describe_restaurant()


restaurant = Restaurant("Texas De Brazil", "an ass ton of meat")
restaurant.describe_restaurant()

print('\n')