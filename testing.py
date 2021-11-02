# Devin Willis
# Nutrition Calculator
# 10/30/2021

import requests, json, os
import fdc_api, diet
from datetime import date

def test_day():
    my_day = diet.day()
    my_day.new_meal("breakfast")
    my_meal = my_day.get_meal("breakfast")
    my_meal.add_food("apple", 250)
    my_meal.add_food("steak", 50)
    my_meal.add_food("olive_oil", 10)
    foods = my_meal.get_foods()
    print(my_day.date)
    print(my_day.get_mealnames())
    for f in foods:
        print(f.get_name())
        f.pprint_summary()
    print(my_meal.get_summary())
