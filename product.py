import os
import csv
from main import *

ListOfCategories = []
# FoodItemsDictionary = {}


def functionCategory():
    global ListOfCategories
    os.chdir("csv/")
    for file in os.listdir():
        i = file.split(".")
        ListOfCategories.append(i[0].capitalize())
    ListOfCategories.sort()
    os.chdir("../")


def functionFoodItems(CategorySelect):
    FoodItemsDictionary = {}
    os.chdir("csv/")
    with open(f"{CategorySelect}.csv", "r") as obj:
        fobj = csv.DictReader(obj)
        for file in fobj:
            FoodItemsDictionary[file["FoodItem"]] = file["Price"]
    os.chdir("../")
    return FoodItemsDictionary


def AddItemtoCSV(ListOfNewItems):
    lis1 = [ListOfNewItems[1], ListOfNewItems[2]]
    os.chdir("csv/")
    filename = f"{ListOfNewItems[0]}.csv"
    print(filename)
    with open(filename, "a") as obj:
        fobj = csv.writer(obj)
        if os.stat(filename).st_size == 0:
            fobj.writerow(["FoodItem", "Price"])
        fobj.writerow(lis1)
    os.chdir("../")
            

if __name__ == '__main__':
    pass

    

