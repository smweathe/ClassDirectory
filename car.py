class Car:
    def __init__(self, year_model, make, speed):
        self.year_model = year_model
        self.make = make
        self.speed = 0
        
    def setYear_model(self, year_model):
        self.year_model = year_model

    def getYear_model(self):
        return self.year_model

    def setMake(self, make):
        self.make = make

    def getMake(self):
        return self.make

    def setSpeed(self, speed):
        if speed < 0:
            print("fail")
        else:    
            self.speed = speed

    def getSpeed(self):
        return self.speed

    def accelerate(self):
        self.speed += 5
        return self.speed

    def brake(self):
        self.speed -= 5
        return self.speed 

def main():
    my_car = Car("1999", "Pontiac Firebird",0)

    for i in range(5):
        my_car.accelerate()
        print (my_car.getSpeed())

    for i in range(5):
        my_car.brake()
        print (my_car.getSpeed())
        
main()
