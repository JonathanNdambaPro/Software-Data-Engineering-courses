class Car:
    def __init__(self, name: str, cost: int | float, brand: str):
        self.name = name
        self.cost = cost
        self.brand = brand

def print_car(car: Car) -> None:
    print(f"name : {car.name} | cost : {car.cost} | brand : {car.brand}")


car = Car(name="Série 1", cost=10000, brand="BMW")
