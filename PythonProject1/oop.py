class Person:


    def __init__(self, age):
        self.age = age


    def set_age(self, p ,get_age):
        self.age = p
        self.get_age = get_age


p = Person()
p.set_age(25)
print(p.get_age)
p.set_age(-5)
