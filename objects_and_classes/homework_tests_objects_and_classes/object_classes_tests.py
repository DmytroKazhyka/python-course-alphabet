from objects_and_classes.homework.homework import Cesar, Car, Garage
import unittest


class CesarTest(unittest.TestCase):

    def test_convert_to_dict(self):
        cesar = Cesar('Ahmetov')
        expected_dict = {'name': 'Ahmetov'}
        self.assertEqual(cesar.convert_to_dict(), expected_dict)

    def test_convert_from_dict(self):
        data = {'name': 'Ahmetov'}
        self.assertEqual(Cesar.convert_from_dict(data), Cesar('Ahmetov'))

    def test_add_garage(self):
        cesar = Cesar('Ahmetov')
        garage_1 = Garage(4)
        cesar.add_garage(garage_1)
        self.assertEqual(len(cesar.garages), 1)

    def test_choose_garage(self):
        cesar = Cesar('Ahmetov')
        garage_1 = Garage(4)
        garage_2 = Garage(1)
        garage_3 = Garage(8)
        cesar.garages = [garage_1, garage_2, garage_3]
        self.assertEqual(cesar.choose_garage(), garage_3)

    def test_add_car(self):
        cesar = Cesar('Ahmetov')
        garage_1 = Garage(4)
        garage_2 = Garage(1)
        garage_3 = Garage(8)
        car_1 = Car(25000, 10000)
        car_2 = Car(30000, 5000)
        cesar.add_garage(garage_1)
        cesar.add_garage(garage_2)
        cesar.add_garage(garage_3)

        # adding car_1 to garage_1
        cesar.add_car(car_1, garage_1)

        # adding car_2 without mentioning any of garages
        cesar.add_car(car_2)

        # checking if car_1 was added to garage_1. We had 4 places in garage_1,
        # so after adding car_1 should be left 3 places
        self.assertEqual(garage_1.free_places(), 3)

        # checking if car_2 was added to garage_3. We didn't mention any of garages, so according to Cesar's method
        # "add_garage" car_2 should be added to garage which has the biggest number of free places, it's garage_3
        # in our case, which had 8 places, so after adding car_2 should be left 7 places.
        self.assertEqual(garage_3.free_places(), 7)

    def test_garages_count(self):
        cesar = Cesar('Ahmetov')
        garage_1 = Garage(4)
        garage_2 = Garage(1)
        cesar.add_garage(garage_1)
        cesar.add_garage(garage_2)
        self.assertEqual(cesar.garages_count(), 2)

    def test_cars_count(self):
        cesar = Cesar('Ahmetov')
        garage_1 = Garage(4)
        garage_2 = Garage(1)
        car_1 = Car(25000, 10000)
        car_2 = Car(30000, 5000)

        cesar.add_garage(garage_1)
        cesar.add_garage(garage_2)

        # adding car_1 to garage_1
        cesar.add_car(car_1, garage_1)

        # adding car_2 to garage_2
        cesar.add_car(car_2, garage_2)

        self.assertEqual(cesar.cars_count(), 2)

    def test_hit_hat(self):
        cesar = Cesar('Ahmetov')
        garage_1 = Garage(4)
        garage_2 = Garage(1)
        car_1 = Car(25000, 10000)
        car_2 = Car(30000, 5000)

        cesar.add_garage(garage_1)
        cesar.add_garage(garage_2)

        # adding car_1 to garage_1
        cesar.add_car(car_1, garage_1)

        # adding car_2 to garage_2
        cesar.add_car(car_2, garage_2)

        self.assertEqual(cesar.hit_hat(), 55000)

    def test_non_equal(self):
        cesar_1 = Cesar('Ahmetov')
        cesar_2 = Cesar('Firtash')
        garage_1 = Garage(4)
        garage_2 = Garage(1)
        car_1 = Car(25000, 10000)
        car_2 = Car(30000, 5000)

        cesar_1.add_garage(garage_1)
        cesar_2.add_garage(garage_2)

        cesar_1.add_car(car_1, garage_1)
        cesar_2.add_car(car_2, garage_2)

        self.assertNotEqual(cesar_1.hit_hat(), cesar_2.hit_hat())

    def test_equal(self):
        cesar_1 = Cesar('Ahmetov')
        cesar_2 = Cesar('Firtash')
        garage_1 = Garage(4)
        garage_2 = Garage(1)
        car_1 = Car(25000, 10000)
        car_2 = Car(25000, 5000)

        cesar_1.add_garage(garage_1)
        cesar_2.add_garage(garage_2)

        cesar_1.add_car(car_1, garage_1)
        cesar_2.add_car(car_2, garage_2)

        self.assertEqual(cesar_1.hit_hat(), cesar_2.hit_hat())

    def test_less_equal(self):
        cesar_1 = Cesar('Ahmetov')
        cesar_2 = Cesar('Firtash')
        garage_1 = Garage(4)
        garage_2 = Garage(1)
        car_1 = Car(25000, 10000)
        car_2 = Car(30000, 5000)
        car_3 = Car(5000, 3000)

        cesar_1.add_garage(garage_1)
        cesar_2.add_garage(garage_2)

        cesar_1.add_car(car_1, garage_1)
        cesar_2.add_car(car_2, garage_2)

        # checking if method "__le__" works properly when cost of cesar_1 cars is less than other cesar's
        self.assertLessEqual(cesar_1.hit_hat(), cesar_2.hit_hat())

        cesar_1.add_car(car_3, garage_1)
        # checking if method "__le__" works properly when cost of cesar_1 cars is equal to other cesar's cost
        self.assertLessEqual(cesar_1.hit_hat(), cesar_2.hit_hat())

    def test_greater_equal(self):
        cesar_1 = Cesar('Ahmetov')
        cesar_2 = Cesar('Firtash')
        garage_1 = Garage(4)
        garage_2 = Garage(2)
        car_1 = Car(30000, 10000)
        car_2 = Car(25000, 5000)
        car_3 = Car(5000, 3000)

        cesar_1.add_garage(garage_1)
        cesar_2.add_garage(garage_2)

        cesar_1.add_car(car_1, garage_1)
        cesar_2.add_car(car_2, garage_2)

        # checking if method "__ge__" works properly when cost of cesar_1 cars is greater than other cesar's
        self.assertGreaterEqual(cesar_1.hit_hat(), cesar_2.hit_hat())

        cesar_2.add_car(car_3, garage_2)
        # checking if method "__ge__" works properly when cost of cesar_1 cars is equal to other cesar's cost
        self.assertGreaterEqual(cesar_1.hit_hat(), cesar_2.hit_hat())

    def test_less_than(self):
        cesar_1 = Cesar('Ahmetov')
        cesar_2 = Cesar('Firtash')
        garage_1 = Garage(4)
        garage_2 = Garage(1)
        car_1 = Car(25000, 10000)
        car_2 = Car(30000, 5000)

        cesar_1.add_garage(garage_1)
        cesar_2.add_garage(garage_2)

        cesar_1.add_car(car_1, garage_1)
        cesar_2.add_car(car_2, garage_2)

        self.assertLess(cesar_1.hit_hat(), cesar_2.hit_hat())

    def test_greater_than(self):
        cesar_1 = Cesar('Ahmetov')
        cesar_2 = Cesar('Firtash')
        garage_1 = Garage(4)
        garage_2 = Garage(2)
        car_1 = Car(30000, 10000)
        car_2 = Car(25000, 5000)

        cesar_1.add_garage(garage_1)
        cesar_2.add_garage(garage_2)

        cesar_1.add_car(car_1, garage_1)
        cesar_2.add_car(car_2, garage_2)

        self.assertGreater(cesar_1.hit_hat(), cesar_2.hit_hat())


class GarageTest(unittest.TestCase):

    def test_convert_to_dict(self):
        garage = Garage(5)
        expected_dict = {'places': 5, 'owner': None}
        self.assertEqual(garage.convert_to_dict(), expected_dict)

    def test_convert_from_dict(self):
        data = {'places': 5}
        self.assertEqual(Garage.convert_from_dict(data), Garage(5))

    def test_add(self):
        garage = Garage(1)
        car_1 = Car(5000, 2000)
        car_2 = Car(7000, 1500)
        garage.add(car_1)
        self.assertEqual(garage.free_places(), 0)
        self.assertEqual(len(garage.cars), 1)
        self.assertEqual(garage.add(car_2), 'No free places left')

    def test_remove_car(self):
        garage = Garage(1)
        car_1 = Car(5000, 2000)
        garage.add(car_1)
        garage.remove_car(car_1)
        self.assertEqual(len(garage.cars), 0)

    def test_hit_hat(self):
        garage = Garage(3)
        garage.cars = [Car(15000, 3300), Car(16000, 4000), Car(11000, 3100)]
        self.assertEqual(garage.hit_hat(), 42000)

    def test_free_places(self):
        garage = Garage(3)
        garage.add(Car(12000, 5000))
        self.assertEqual(garage.free_places(), 2)


class CarTest(unittest.TestCase):

    def test_convert_to_dict(self):
        car = Car(12000, 3000)
        expected_dict = {'price': 12000, 'mileage': 3000}
        self.assertEqual(car.convert_to_dict(), expected_dict)

    def test_convert_from_dict(self):
        data = {'price': 12000, 'mileage': 5000}
        self.assertEqual(Car.convert_from_dict(data), Car(12000, 5000))

    def test_change_number(self):
        car = Car(12000, 3000)
        car_number_original = car.number
        car_number_changed = car.change_number()
        self.assertNotEqual(car_number_original, car_number_changed)

    def test_non_equal(self):
        car_1 = Car(25000, 10000)
        car_2 = Car(30000, 5000)

        self.assertNotEqual(car_1.price, car_2.price)

    def test_equal(self):
        car_1 = Car(25000, 10000)
        car_2 = Car(25000, 5000)

        self.assertEqual(car_1.price, car_2.price)

    def test_less_equal(self):
        car_1 = Car(25000, 10000)
        car_2 = Car(30000, 5000)

        self.assertLessEqual(car_1.price, car_2.price)

        car_3 = Car(30000, 12000)
        # checking if method "__le__" works properly when cost of car_1 price is equal to car_3 price
        self.assertLessEqual(car_1.price, car_3.price)

    def test_greater_equal(self):
        car_1 = Car(30000, 10000)
        car_2 = Car(25000, 5000)
        car_3 = Car(30000, 3000)

        # checking if method "__ge__" works properly when cost of car_1 is greater than car_2
        self.assertGreaterEqual(car_1.price, car_2.price)

        # checking if method "__ge__" works properly when cost of car_1 is equal to car_3
        self.assertGreaterEqual(car_1.price, car_3.price)

    def test_less_than(self):
        car_1 = Car(25000, 10000)
        car_2 = Car(30000, 5000)

        self.assertLess(car_1.price, car_2.price)

    def test_greater_than(self):
        car_1 = Car(30000, 10000)
        car_2 = Car(25000, 5000)

        self.assertGreater(car_1.price, car_2.price)


if __name__ == "__main__":
    unittest.main()

