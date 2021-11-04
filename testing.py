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

def main():
    exit = False
    test_day = diet.day()
    welcome_str = ("#"*20 + "\n"
    "Welcome to Devin's nutrition calculator!\n"
    "Please select a following action:\n"
    "1) Get today's nutrition summary\n"
    "2) Get today's meals\n"
    "3) Get a meals summary\n"
    "4) Search for a food\n"
    "5) Add a meal\n"
    "6) Add a food to a meal\n"
    "E) Exit")
    while not exit:
        print(welcome_str)
        userin = input("")
        if userin.upper() == "E":
            exit = True
        elif userin == "1":
            for m in test_day.get_meals().values():
                print(m.get_summary())
        elif userin == "2":
            print(test_day.get_mealnames())
        elif userin == "3":
            meal_name = input("Please enter meal name: ")
            meal = test_day.get_meal(meal_name)
            print(meal.get_summary())
        elif userin == "4":
            food_name = input("Please enter food to search: ")
            fdc_api.get_info(food_name)
        elif userin == "5":
            meal_name = input("Please enter a meal name: ")
            test_day.new_meal(meal_name)
        elif userin == "6":
            meal_name = input("Please enter meal name to add to: ")
            fdc_id = input("Please enter a food ID:")
            meal = test_day.get_meal(meal_name)
            meal.add_food(fdc_id)

if __name__ == "__main__":
    main()