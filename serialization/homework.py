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


# Convert instances of Cesar, Garage and Car into JSON strings
encoded_cesar = json.dumps(cesar_1.convert_to_dict())

encoded_garage = json.dumps(garage_1.convert_to_dict())

encoded_car = json.dumps(car_1.convert_to_dict())


# Create instances of Cesar, Garage and Car from json strings
decoded_cesar = json.loads(encoded_cesar, object_hook=Cesar.convert_from_dict)

decoded_garage = json.loads(encoded_garage, object_hook=Garage.convert_from_dict)

decoded_car = json.loads(encoded_car, object_hook=Car.convert_from_dict)


# Save instances of Cesar, Garage and Car into JSON files
with open('cesar_1.json', 'w') as file:
    json.dump(cesar_1.convert_to_dict(), file)

with open('garage_1.json', 'w') as file:
    json.dump(garage_1.convert_to_dict(), file)

with open('car_1.json', 'w') as file:
    json.dump(car_1.convert_to_dict(), file)


# Create instances of Cesar, Garage and Car from JSON files
with open('cesar_1.json', 'r') as file:
    decoded_cesar = json.load(file, object_hook=Cesar.convert_from_dict)

with open('garage_1.json', 'r') as file:
    decoded_garage = json.load(file, object_hook=Garage.convert_from_dict)

with open('car_1.json', 'r') as file:
    decoded_car = json.load(file, object_hook=Car.convert_from_dict)


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
