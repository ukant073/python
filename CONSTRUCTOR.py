class car:
    def __init__(self,car_id,car_name):
        self.__car_id= car_id
        self.car_name= car_name

    def get__car_id(self):
        return self.__car_id

car1 = car(123,"volvo")
print(car1.get__car_id(),car1.car_name)
        
