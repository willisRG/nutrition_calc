# Devin Willis
# Nutrition Calculator
# 10/30/2021

api_key = "Kh9qrxgE9UIzfU8jWi4AY1aFFSL54TXMVWUuWuot"

import requests, json, os
from datetime import date

def search_food():
    food = "apple"
    query_string = "https://api.nal.usda.gov/fdc/v1/foods/search?query=" + food + "&pageSize=2&api_key=" + api_key
    response = requests.get(query_string, json=True)
    print(json.dumps(response.json(), indent=4, sort_keys=1))

def get_nutrition(fcid="454004"):
    query_string = "https://api.nal.usda.gov/fdc/v1/food/" + fcid + "?api_key=" + api_key
    response = requests.get(query_string, json=True)
    print(json.dumps(response.json(), indent=4, sort_keys=1))

class food:
    
    def __init__(self, f_name):
        cache_path = os.path.join(os.path.dirname(__file__), "cache\\" + f_name + ".json")
        f_json = json.load(open(cache_path))
        self.name = f_json

    def get_name(self):
        return self.name

class meal:
    
    def __init__(self, meal_name):
        self.meal_name = meal_name
        self.foods = []

    def add_food(self, f_name, s_size):
        new_food = food(f_name)
        self.foods.append(new_food)

    def remove_food(self, food):
        self.foods.remove(food)

    def get_foods(self):
        return self.foods

    def get_food(self, i):
        return self.foods[i]

    def get_name(self):
        return self.meal_name

class day:

    def __init__(self,date=date.today()):
        self.meals = {}
        self.date = date

    def new_meal(self, meal_name):
        newmeal = meal(meal_name)
        self.meals[newmeal.get_name()] = newmeal

    def remove_meal(self, meal):
        self.meals.remove[meal]

    def get_meals(self):
        return self.meals

    def get_mealnames(self):
        return list(self.meals.keys())

    def get_meal(self, i):
        return self.meals[i]

    def get_date(self):
        return self.date

my_day = day()
my_day.new_meal("breakfast")
my_meal = my_day.get_meal("breakfast")
my_meal.add_food("bread", 0)
my_meal.add_food("steak", 0)
my_meal.add_food("olive_oil", 0)
foods = [food.get_name() for food in my_meal.get_foods()]
print(my_day.date)
print(my_day.get_mealnames())
print(foods)