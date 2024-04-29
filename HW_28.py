# class BunkUser:
#     def __init__(self, name, surname, age, qart, balance, password):
#         if not (self._is_valid_n_s(name, surname) and self._is_valid_age(age)
#                 and self.__is_valid_cart(qart) and self.__is_valid_cash(balance)
#                 and self.__is_valid_password(password)):
#             raise ValueError('Invalid parameters')
#         self._name = name
#         self._surname = surname
#         self._age = age
#         self.__qart = qart
#         self.__balance = balance
#         self.__password = password
#
#     @staticmethod
#     def _is_valid_n_s(name, surname):
#         if name.istitle and surname.istitle:
#             return "True name and surname"
#         return "invalid name or surname"
#
#     @staticmethod
#     def _is_valid_age(age):
#         if type(age) is int:
#             return f"True age"
#         return "invalid age"
#
#     @staticmethod
#     def __is_valid_cart(qart):
#         if type(qart) is str:
#             if len(qart) == 16 and qart.isdigit():
#                 return "True balance"
#             if len(qart) == 19 and (
#                     qart[:3].isdigit
#                     and qart[5:9].isdigit()
#                     and qart[10:15].isdigit()
#                     and qart[16:19].isdigit()) and qart[::5] == " ":
#                 return "True balance"
#
#         return "invalid cart"
#
#     @staticmethod
#     def __is_valid_cash(cash):
#         if type(cash) is float or (type(cash) is int):
#             return "True input cash"
#         return "invalid input cash"
#
#     @staticmethod
#     def __is_valid_password(password):
#         if type(password) is str and len(password) >= 18:
#             return "True password"
#         return "invalid password"
#
#     @staticmethod
#     def get_name_surname(name, surname):
#         return f"{name} {surname}"
#
#     @staticmethod
#     def get_age(age):
#         return f"{age} years old"
#
#     def get_qart_balance(self, input_password):
#         i = 0
#         while i < 3:
#             if input_password != self.__password:
#                 i += 1
#                 raise "Incorrect password"
#             break
#         return self.__qart, self.__balance
#
#     def deposit(self, input_password, price):
#         i = 0
#         while i < 3:
#             if input_password != self.__password:
#                 i += 1
#                 raise "Incorrect password"
#             break
#
#         self.__balance += price
#
#     def withdraw(self, input_password, price):
#         i = 0
#         while i < 3:
#             if input_password != self.__password:
#                 i += 1
#                 raise "Invalid password"
#             else:
#                 if price <= self.__balance:
#                     self.__balance -= price
#                     break

# a = "1234 1234 1234 1234"
# print(list(a))

# class Car:
#     def __init__(self, car_id):
#         self.car_id = car_id
#
#     def car_ID(self):
#         return f'car ID: {self.car_id}'
#
#
# class ParkingLot:
#     def __init__(self, total_spots):
#         self.total_spots = total_spots
#         self.spots = total_spots
#         self.cars_parked = {}
#         self.cash = 0
#
#     def park(self, car):
#         if self.spots == 0:
#             print("Parking lot is full")
#         else:
#             self.cars_parked[car.car_id] = car
#             self.spots -= 1
#
#     def release(self, car):
#         if car.car_id not in self.cars_parked:
#             print("Car not found in the parking lot")
#         else:
#             user_input = float(input("Hours : "))
#             self.cash += user_input * 500
#             self.spots += 1
#
#     def spots_let(self):
#         return self.spots
#
#     def cash_register(self):
#         return self.cash
#
#
# car1 = Car("BMW1")
# car2 = Car("BMW2")
# car3 = Car("BMW3")
# car4 = Car("BMW4")
# car5 = Car("BMW5")
# Parking = ParkingLot(7)
# Parking.park(car1)
# Parking.park(car2)
# Parking.park(car3)
# Parking.park(car4)
# Parking.park(car5)
# Parking.release(car1)
# print(Parking.cash_register())
# print(Parking.spots_let())
