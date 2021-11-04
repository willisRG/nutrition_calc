import requests, json, os
from datetime import date

api_key = open("api_key.key").read()

class s_object:

    def __init__(self,qry_str):
        self.qry_str = qry_str

    def search_food(food="apple"):
        query_string = "https://api.nal.usda.gov/fdc/v1/foods/search?query=" + food + "&pageSize=10&api_key=" + api_key
        response = requests.get(query_string, json=True)
        return response.json()
        #print(json.dumps(response.json(), indent=4, sort_keys=1))

    def get_nutrition(fcid="454004"):
        query_string = "https://api.nal.usda.gov/fdc/v1/food/" + fcid + "?api_key=" + api_key
        response = requests.get(query_string, json=True)
        print(json.dumps(response.json(), indent=4, sort_keys=1))

class f_json:

    def __init__(self, j):
        self.raw_json = j

    def get_name(self):
        return self.raw_json[""]

def get_nut(fn_list, nutname="Energy"):
    nut_dict = {}
    for fn in fn_list.get("foodNutrients"):
        if fn.get("nutrientName") == nutname:
            nut_dict = fn
            return nut_dict
    return nut_dict

fval_list = ["description", "fdcID", "brandName", "name", "brandOwner", "foodCategory", "servingSizeUnit", "servingSize"]
nut_name_list = ["Energy", "Protein", "Total lipid (fat)", "Carbohydrate, by difference"]

def get_info(food_qry=""):
    if food_qry == "":
        food_qry = input("Please enter a food to search: ")
    search = s_object.search_food(food_qry)["foods"]
    nut_info = [] 
    for f in search:
        print("-" * 20)
        print(f["description"] + " : " + str(f["fdcId"]))
        for val in fval_list:
            print(val + ": " + str(f.get(val)))
        for nut in nut_name_list:
            print(nut + ": " + str(get_nut(f,nut).get("value")))
        print("")

#get_info("apple")