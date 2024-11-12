class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def introduce(self):
        return f"Я {self.name}, мой уровень здоровья: {self.health}"

    def rest(self):
        self.health += 10
        return f"{self.name} отдыхает и восстанавливает здоровье. Новое здоровье: {self.health}"

    def action(self):
        return f"{self.name} выполняет базовое действие.\n"

# Класс Mage, наследующийся от Hero
class Mage(Hero):
    def __init__(self, name, health, mana=100):
        super().__init__(name, health)
        self.mana = mana

    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"{self.name} использует заклинание! Оставшаяся мана: {self.mana}"
        else:
            return f"{self.name} недостаточно маны для заклинания!"

    def action(self):
        base_action = super().action()
        spell_result = self.cast_spell()  # Вызов метода внутри другого метода
        return f"{base_action} {spell_result}"

def hero_action(hero):
    print(hero.introduce())
    print(hero.rest())
    print(hero.action())

mage = Mage("Гэндальф", 100, 50)

hero_action(mage)