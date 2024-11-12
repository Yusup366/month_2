from abc import ABC,abstractmethod


class Room(ABC):
    def __init__(self,features,price):
        self._features = features
        self._price = price

        @abstractmethod
        def get_price(self):
            pass
        @abstractmethod
        def get_features(self):
            pass

class StandardRoom(Room):
    def get_price(self):
        return self._price

    def get_features(self):
        return self._features

class LuxuryRoom(Room):
    def get_price(self):
        return self._price

    def get_features(self):
        return self._features

class FamilyRoom(Room):
    def get_price(self):
        return self._price

    def get_features(self):
        return self._features

class WiFiService:
    def get_wifi_description(self):
        return 'бесплатный WI-FI'

class BreakfastService:
    def get_breakfast_description(self):
        return 'бесплатный завтрак включен'

class LuxuryRoom(Room,WiFiService,BreakfastService):
    def get_price(self):
        return self._price

    def get_features(self):
        features = self._features
        features.append(self.get_wifi_description())
        features.append(self.get_breakfast_description())
        return features

class FamilyRoom(Room,WiFiService,):

    def get_price(self):
        return self._price

    def get_features(self):
        features = self._features
        features.append(self.get_wifi_description())
        return features


standard_room = StandardRoom(['ТВ','Кондиционер'], 200)
luxury_room = LuxuryRoom(['ТВ','Кондиционер','мини бар','джакузи'],500)
family_room = FamilyRoom(['ТВ','Кондиционер','Детская комната'],300)

print('StandardRoom:')
print('Price:',standard_room.get_price())
print('Features:',standard_room.get_features())

print('\nLuxuryRoom')
print('Price:',luxury_room.get_price())
print('Features:',luxury_room.get_features())

print('\nFamilyRoom')
print('Price:',family_room.get_price())
print('Features:',family_room.get_features())


