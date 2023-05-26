class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.rating = 0
    def describe_restaurant(self):
        print(f"Ресторан {self.name} предлагает {self.cuisine_type} кухню.")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.name} : {self.rating}.")

restaurant1 = Restaurant('Ресторан', 'кухня')
restaurant2 = Restaurant('Токио hotel', 'европейская')
restaurant3 = Restaurant('Евразия', 'японская')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant1.update_rating(10/10)
restaurant2.update_rating(9/10)
restaurant3.update_rating(8/10)
