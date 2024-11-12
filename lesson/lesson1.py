# ооп
#
# types_python = 1, 'str', 1.2, True, {}, [], ()
#
# print(type(types_python))


class Car:



    def drive(self):
        print('машина едит',self.model)

    def __init__(self,model,volume,age):
        self.model = model
        self.volume = volume
        self.age = age

    def start(self):
        print('машина завелась',self.age)

    def __str__(self):
        return f'{audi.model} {audi.volume}'

#экземпяр
audi = Car(model='a8',age='2000',volume='2.8')
