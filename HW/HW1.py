class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
    def introduce(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}.')
    def is_adult(self):
        return self.age >=18
    def __str__(self):
        return f"Имя: {self.name},Возраст: {self.age},Город: {self.city}"
person1 = Person(name='Виталик',age=30,city='Бишкек')
person2 = Person(name='Рома',age=17,city='Бишкек')
print(person1)
print(person2)