import requests, json, os
import fdc_api, diet
from datetime import date

class food:
    
    def __init__(self, f_name, s_s):
        cache_path = os.path.join(os.path.dirname(__file__), "cache\\" + f_name + ".json")
        f_json = json.load(open(cache_path))
        self.name = f_json["name"]
        if s_s == -1:
            self.n_mult = 1
        else:
            self.n_mult = s_s / f_json["servingSize"]
        self.units = f_json["servingSizeUnit"]
        self.nutrition = f_json["labelNutrients"]
        self.f_summary = {}
        self.calc_nutrition()

    def get_name(self):
        return self.name

    def calc_nutrition(self):
        for n_unit in self.nutrition:
            #print(n_unit + " " + str(round(self.n_mult * self.nutrition[n_unit]["value"], 2)))
            self.f_summary[n_unit] = {"value": round(self.n_mult * self.nutrition[n_unit]["value"], 2)}
        return

    def get_macro(self, m_name):
        return self.f_summary[m_name]["value"]

    def pprint_summary(self):
        print(self.f_summary)

class meal:
    
    def __init__(self, meal_name):
        self.meal_name = meal_name
        self.foods = []
        self.summary = {
            "calories" : 0,
            "protein" : 0,
            "fat" : 0,
            "carbohydrates" : 0
        }

    def calc_summary(self):
        for f in self.foods:
            self.summary["calories"] += f.get_macro("calories")
            self.summary["protein"] += f.get_macro("protein")
            self.summary["fat"] += f.get_macro("fat")
            self.summary["carbohydrates"] += f.get_macro("carbohydrates")
        return

    def add_food(self, f_name, s_size=-1):
        new_food = food(f_name, s_size)
        self.foods.append(new_food)
        self.calc_summary()

    def remove_food(self, food):
        self.foods.remove(food)
        self.calc_summary()
    
    def get_summary(self):
        return self.summary

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

    def get_meal(self, name):
        return self.meals.get(name)

    def get_date(self):
        return self.date