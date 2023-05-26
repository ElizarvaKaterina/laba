class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print('Ресторан {} предлагает кухню {}.'.format(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print('Ресторан {} открыт!'.format(self.restaurant_name))

newRestaurant = Restaurant('Ресторан', 'кухня')
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
