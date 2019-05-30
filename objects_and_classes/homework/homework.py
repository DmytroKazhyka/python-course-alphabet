"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""

from objects_and_classes.homework import constants
import random
import uuid


class Cesar:

    def __init__(self, name):
        self.name = name
        self.garages = []
        self.register_id = uuid.uuid4()

    def convert_to_dict(self):
        data = {'name': self.name}
        return data

    @classmethod
    def convert_from_dict(cls, data):
        name = data['name']
        cr = Cesar(name=name)
        return cr

    def add_garage(self, garage):
        self.garages.append(garage)
        garage.owner = self.name

    def choose_garage(self):
        list_of_places = []
        for garage in self.garages:
            list_of_places.append(garage.free_places())
        for garage in self.garages:
            if garage.free_places() == max(list_of_places):
                return garage

    def add_car(self, car, garage=None):
        if garage:
            if garage in self.garages:
                garage.add(car)
        else:
            chosen_garage = self.choose_garage()
            chosen_garage.add(car)

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        number_of_cars = 0
        for garage in self.garages:
            number_of_cars += len(garage.cars)
        return number_of_cars

    def hit_hat(self):
        sum_price = 0
        for garage in self.garages:
            for car in garage.cars:
                sum_price += car.price
        return sum_price

    def __ne__(self, other):
        return self.hit_hat() != other.hit_hat()

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    def __ge__(self, other):
        return self.hit_hat() >= other.hit_hat()

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()


class Car:

    def __init__(self, price, mileage):
        self.price = price
        self.mileage = mileage
        self.type = random.choice(constants.CARS_TYPES)
        self.producer = random.choice(constants.CARS_PRODUCER)
        self.number = uuid.uuid4()

    def convert_to_dict(self):
        data = {'price': self.price, 'mileage': self.mileage}
        return data

    @classmethod
    def convert_from_dict(cls, data):
        price = data['price']
        mileage = data['mileage']
        car_inst = Car(price=price, mileage=mileage)
        return car_inst

    def __repr__(self):
        return 'price: {}, mileage: {}, type: {}, producer: {}, number: {}'.format(self.price, self.mileage, self.type,
                                                                                   self.producer, self.number)

    def __ne__(self, other):
        return self.price != other.price

    def __eq__(self, other):
        return self.price == other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def change_number(self):
        self.number = uuid.uuid4()


class Garage:

    def __init__(self, places, owner=None):
        self.places = places
        self.owner = owner
        self.cars = []
        self.town = random.choice(constants.TOWNS)

    def convert_to_dict(self):
        data = {'places': self.places, 'owner': self.owner}
        return data

    @classmethod
    def convert_from_dict(cls, data):
        places = data['places']
        owner = data['owner']
        gar_inst = Garage(places=places, owner=owner)
        return gar_inst

    def add(self, car):
        if len(self.cars) < self.places:
            self.cars.append(car)
        else:
            print('No free places left')

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)

    def hit_hat(self):
        sum_of_car_prices = 0
        for car in self.cars:
            sum_of_car_prices += car.price
        return sum_of_car_prices

    def free_places(self):
        return self.places - len(self.cars)


# cesar_1 = Cesar('Axelrod')
# garage_1 = Garage(5)
#
# ser_to_json_garage_1 = json.dumps(garage_1.convert_to_dict())
# print(type(ser_to_json_garage_1), ser_to_json_garage_1)
#
#
# deser_from_json_garage_1 = json.loads(ser_to_json_garage_1, object_hook=Garage.convert_from_dict)
# print(type(deser_from_json_garage_1), deser_from_json_garage_1)
