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

# -------------------------- JSON ----------------------------

# Instances of Cesar, Garage and Car
cesar_1 = Cesar('Axelrod')
garage_1 = Garage(5)
car_1 = Car(45000, 5000)
#
#
# # Method to convert custom object of class Cesar to JSON convertible format
# def cesar_to_json(obj: Cesar):
#     data = {'name': obj.name}
#     return data
#
#
# # Method to convert custom object of class Garage to JSON convertible format
# def garage_to_json(obj: Garage):
#     data = {'places': obj.places, 'owner': None}
#     return data
#
#
# # Method to convert custom object of class Car to JSON convertible format
# def car_to_json(obj: Car):
#     data = {'price': obj.price, 'mileage': obj.mileage}
#     return data
#
#
# # Method to convert JSON string into object of class Cesar
# def cesar_from_json(data):
#     name = data['name']
#     cr = Cesar(name=name)
#     return cr
#
#
# # Method to convert JSON string into object of class Garage
# def garage_from_json(data):
#     places = data['places']
#     owner = data['owner']
#     gr = Garage(places=places, owner=owner)
#     return gr
#
#
# # Method to convert JSON string into object of class Car
# def car_from_json(data):
#     price = data['price']
#     mileage = data['mileage']
#     car = Car(price=price, mileage=mileage)
#     return car
#
#
# # Convert instances of Cesar, Garage and Car into JSON strings
# encoded_cesar = json.dumps(cesar_1, default=cesar_to_json)
# print(type(encoded_cesar), encoded_cesar)
#
# encoded_garage = json.dumps(garage_1, default=garage_to_json)
# print(type(encoded_garage), encoded_garage)
#
# encoded_car = json.dumps(car_1, default=car_to_json)
# print(type(encoded_car), encoded_car)
#
#
# # Create instances of Cesar, Garage and Car from json strings
# decoded_cesar = json.loads(encoded_cesar, object_hook=cesar_from_json)
# print(type(decoded_cesar), decoded_cesar)
#
# decoded_garage = json.loads(encoded_garage, object_hook=garage_from_json)
# print(type(decoded_garage), decoded_garage)
#
# decoded_car = json.loads(encoded_car, object_hook=car_from_json)
# print(type(decoded_car), decoded_car)
#
#
# # Save instances of Cesar, Garage and Car into JSON files
# with open('cesar_1.json', 'w') as file:
#     json.dump(cesar_1, file, default=cesar_to_json)
#
# with open('garage_1.json', 'w') as file:
#     json.dump(garage_1, file, default=garage_to_json)
#
# with open('car_1.json', 'w') as file:
#     json.dump(car_1, file, default=car_to_json)
#
#
# # Create instances of Cesar, Garage and Car from JSON files
# with open('cesar_1.json', 'r') as file:
#     decoded_cesar = json.load(file, object_hook=cesar_from_json)
#     print(type(decoded_cesar), decoded_cesar)
#
# with open('garage_1.json', 'r') as file:
#     decoded_garage = json.load(file, object_hook=garage_from_json)
#     print(type(decoded_garage), decoded_garage)
#
# with open('car_1.json', 'r') as file:
#     decoded_car = json.load(file, object_hook=car_from_json)
#     print(type(decoded_car), decoded_car)


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
    cesar_1 = yaml.load(file)

with open('garage_1.yaml', 'r') as file:
    garage_1 = yaml.load(file)

with open('car_1.yaml', 'r') as file:
    car_1 = yaml.load(file)

print(cesar_1)