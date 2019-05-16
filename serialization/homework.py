"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""

from objects_and_classes.homework.homework import Cesar, Garage, Car
import json
from ruamel.yaml import YAML
import ruamel.yaml
import pickle

# -------------------------- JSON ----------------------------

# Instances of Cesar, Garage and Car
cesar_1 = Cesar('Axelrod')
garage_1 = Garage(5)
car_1 = Car(45000, 5000)


# Method to convert custom object of class Cesar to JSON convertible format
def cesar_to_json(obj: Cesar):
    data = {'name': obj.name}
    return data


# Method to convert custom object of class Garage to JSON convertible format
def garage_to_json(obj: Garage):
    data = {'places': obj.places, 'owner': None}
    return data


# Method to convert custom object of class Car to JSON convertible format
def car_to_json(obj: Car):
    data = {'price': obj.price, 'mileage': obj.mileage}
    return data


# Method to convert JSON string into object of class Cesar
def cesar_from_json(data):
    name = data['name']
    cr = Cesar(name=name)
    return cr


# Method to convert JSON string into object of class Garage
def garage_from_json(data):
    places = data['places']
    owner = data['owner']
    gr = Garage(places=places, owner=owner)
    return gr


# Method to convert JSON string into object of class Car
def car_from_json(data):
    price = data['price']
    mileage = data['mileage']
    car = Car(price=price, mileage=mileage)
    return car


# Convert instances of Cesar, Garage and Car into JSON strings
encoded_cesar = json.dumps(cesar_1, default=cesar_to_json)

encoded_garage = json.dumps(garage_1, default=garage_to_json)

encoded_car = json.dumps(car_1, default=car_to_json)


# Create instances of Cesar, Garage and Car from json strings
decoded_cesar = json.loads(encoded_cesar, object_hook=cesar_from_json)

decoded_garage = json.loads(encoded_garage, object_hook=garage_from_json)

decoded_car = json.loads(encoded_car, object_hook=car_from_json)


# Save instances of Cesar, Garage and Car into JSON files
with open('cesar_1.json', 'w') as file:
    json.dump(cesar_1, file, default=cesar_to_json)

with open('garage_1.json', 'w') as file:
    json.dump(garage_1, file, default=garage_to_json)

with open('car_1.json', 'w') as file:
    json.dump(car_1, file, default=car_to_json)


# Create instances of Cesar, Garage and Car from JSON files
with open('cesar_1.json', 'r') as file:
    decoded_cesar = json.load(file, object_hook=cesar_from_json)

with open('garage_1.json', 'r') as file:
    decoded_garage = json.load(file, object_hook=garage_from_json)

with open('car_1.json', 'r') as file:
    decoded_car = json.load(file, object_hook=car_from_json)


# -------------------------------YAML------------------------------
# Save instances of Cesar, Garage and Car into YAML files

yaml = YAML()
yaml.register_class(Cesar)
with open('cesar_1.yaml', 'w') as file:
    ruamel.yaml.dump(cesar_1, file)

yaml.register_class(Garage)
with open('garage_1.yaml', 'w') as file:
    ruamel.yaml.dump(garage_1, file)

yaml.register_class(Car)
with open('car_1.yaml', 'w') as file:
    ruamel.yaml.dump(car_1, file)

# Create instances of Cesar, Garage and Car from YAML files

with open('cesar_1.yaml', 'r') as file:
    cesar_1 = ruamel.yaml.load(file)

with open('garage_1.yaml', 'r') as file:
    garage_1 = ruamel.yaml.load(file)

with open('car_1.yaml', 'r') as file:
    car_1 = ruamel.yaml.load(file)


# -------------------------------PICKLE------------------------------

# Save instances of Cesar, Garage and Car into Pickle files

with open('cesar_1.txt', 'wb') as file:
    pickle.dump(cesar_1, file)

with open('garage_1.txt', 'wb') as file:
    pickle.dump(garage_1, file)

with open('car_1.txt', 'wb') as file:
    pickle.dump(car_1, file)


# Create instances of Cesar, Garage and Car from Pickle files

with open('cesar_1.txt', 'rb') as file:
    cesar_1 = pickle.load(file)

with open('garage_1.txt', 'rb') as file:
    garage_1 = pickle.load(file)

with open('car_1.txt', 'rb') as file:
    car_1 = pickle.load(file)


# Convert instances of Cesar, Garage and Car into Pickle strings

encoded_cesar = pickle.dumps(cesar_1)

encoded_garage = pickle.dumps(garage_1)

encoded_car = pickle.dumps(car_1)


# Create instances of Cesar, Garage and Car from Pickle strings

decoded_cesar = pickle.loads(encoded_cesar)

decoded_garage = pickle.loads(encoded_garage)

decoded_car = pickle.loads(encoded_car)
