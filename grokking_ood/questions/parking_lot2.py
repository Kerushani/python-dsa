import enum

"""
vehicle
Variables: license plate, vehicle type
methods:
Children: car, truck, motorcycle
"""
class VehicleType(enum):
    TRUCK = 1
    CAR = 2
    MOTORCYCLE = 3

class RateType(enum):
    HourlyRate = 4
    DailyRate = 2
    EventRate = 5

class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().init(license_plate, VehicleType.CAR)
        
class Truck(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.TRUCK)

class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__ini__t(license_plate, VehicleType.MOTORCYCLE)

"""
PricingStrategy
variable: (time, rate_type)
methods:
HourlyRate
DailyRate
EventRate
"""
class PricingStrategy():
    def __init__(self, pricing_strategy: RateType, time: int):
        self.pricing_strategy = pricing_strategy

class HourlyRatePricingStrategy(PricingStrategy):
    def __init__(self, time: int):
        super().__init__(time,RateType.HourlyRate)
    def calculate_price(self):
        return self.time*self.pricing_strategy.value

class DailyRatePricingStrategy(PricingStrategy):
    def __init__(self, time: int):
        super().__init__(time,RateType.DailyRate)
    def calculate_price(self):
        return self.time*self.pricing_strategy.value
class EventRatePricingStrategy(PricingStrategy):
    def __init__(self, time: int):
        super().__init__(time,RateType.EventRate)
    def calculate_price(self):
        return self.time*self.pricing_strategy.value

"""
Parking Spot
variable: vehicle_type, parking_spot_number
methods:
get_parking_spot_number
get_vehichle_type
"""

class ParkingSpot():
    def __init__(self, parking_spot_number: int, vehicle_type: VehicleType):
        self.vehicle_type = vehicle_type
        self.parking_spot_number = parking_spot_number
        self.parkedVehicle = None
    def get_parking_spot_number(self):
        return self.parking_spot_number
    def get_vehicle_type(self):
        return self.vehicle_type
    def isTaken(self) -> bool:
        return self.parkedVehicle is None
    def park_car(self, vehicle):
        self.parkedVehicle = vehicle
        return f"{self.parkedVehicle} is parked"

"""
Level
variables: [parking_spots]
methods:
park_vehicle
get_spot_availablities -> len(parking_spots)
"""

class Level():
    def __init__(self, number_of_spots_available: int):
        self.number_of_spots = number_of_spots_available
        self.parking_spots = [ParkingSpot(i) for i in range(number_of_spots_available)]
    def get_number_of_spots(self) -> int:
        return self.number_of_spots_available
    def park_car(self, vehicle):
        for spot in self.parking_spots:
            if spot.isTaken() == False:
                spot.park_car(vehicle)
    def get_spot_availabilities(self):
        available_spots = 0
        for spot in self.parking_spots:
            if spot.isTaken() == False:
                available_spots += 1
    

"""
main ParkingGarage
variable: levels -> [Level]
methods:
add parking lot floor -> +level
fee_calculation -> Pricing Strategy
park_car
unpark_car
relations between methods here and the functions are going to be by vehicle_type
"""

class ParkingGarage():
    def __init__(self, levels):
        self.levels = []
    def add_floor(self, level: Level) -> Level:
        self.levels.append(level)
    def fee_calculation(self, pricing_strategy, time):
        return PricingStrategy(pricing_strategy, time)
    def park_car(self, vehcile):
        for level in self.levels:
            level.park_car(self.vehicle)




"""
test
"""
