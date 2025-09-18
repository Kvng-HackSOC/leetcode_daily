class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_foods = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            if cuisine not in self.cuisine_to_foods:
                self.cuisine_to_foods[cuisine] = []
            self.cuisine_to_foods[cuisine].append(food)

    def changeRating(self, food, newRating):
        self.food_to_rating[food] = newRating

    def highestRated(self, cuisine):
        foods = self.cuisine_to_foods[cuisine]
        return max(foods, key=lambda f: (self.food_to_rating[f], -ord(f[0])))
