class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.num_served = 0
    

    def describe_restaurant(self):
        msg = f"{self.name} serves {self.cuisine_type} to {self.num_served} with a large amout of quality."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} is open to serve all."
        print(f"\n{msg}")
    
    def set_num_served(self, num_served):

        self.num_served = num_served

    def increment_number_served(self, additional_served):

        self.num_served += additional_served


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f" - {flavor.title()}")

ice_box = IceCreamStand('the ice box')

ice_box.flavors = ['iguana', 'tangy vanilla', 'black ice']

ice_box.describe_restaurant()
ice_box.show_flavors()

