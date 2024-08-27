class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.engine = None
        self.transmission = None

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Engine: {self.engine}, Transmission: {self.transmission}"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_transmission(self, transmission):
        self.car.transmission = transmission
        return self

    def build(self):
        return self.car


builder = CarBuilder()
car = (
    builder
    .set_make("UAZ")
    .set_model("Patriot")
    .set_engine("2.7L")
    .set_transmission("4x4")
    .build()
)

print(car)
