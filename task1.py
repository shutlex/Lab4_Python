class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed



car = Car("Honda", "Civic", 2008)


for _ in range(5):
    car.accelerate()
    print("Поточна швидкість після прискорення:", car.get_speed())


for _ in range(5):
    car.brake()
    print("Поточна швидкість після гальмування:", car.get_speed())