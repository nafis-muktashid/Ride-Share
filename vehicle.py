from abc import ABC

class Vehicle(ABC):
    speed = {
        "Car" : 50,
        "MotorCycle" : 60,
        "CNG" : 15
    }
    def __init__(self, vehicle_tye, license_plate, rate):
        self.vehicle_type = vehicle_tye
        self.license_plate = license_plate
        self.rate = rate


class Car(Vehicle):
    def __init__(self, vehicle_tye, license_plate, rate):
        super().__init__(vehicle_tye, license_plate, rate)

class MotorCycle(Vehicle):
    def __init__(self, vehicle_tye, license_plate, rate):
        super().__init__(vehicle_tye, license_plate, rate)