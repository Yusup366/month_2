from urllib.parse import uses_query

from main import Hero

class CustomHero(Hero):
    def __init__(self, name, health, energy=50):
        super().__init__(name, health)
        self.energy = energy
    def use_skill(self):
        if self.energy >= 10:
            self.energy -= 10
            return f"{self.name} использует уникальное умение! Осталось энергии: {self.energy}"
        else:
            return f"{self.name} недостаточно энергии для использования умения."
    def action(self):
        hero_action = super().action()
        skill_action = self.use_skill()
        return f"{hero_action}\n{skill_action}"