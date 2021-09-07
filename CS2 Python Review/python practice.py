class Funko:
    increase = float(input("put in a decimal increase for the funko\n"))

    numFunkos = 0
    def __init__(self, name, price, franchise, year):
        self.name = name
        self.price = price
        self.franchise = franchise
        self.year = year

        Funko.numFunkos += 1

    def nameAndPrice(self):
        return '{} costs ${}'.format(self.name, self.price)

    def priceIncrease(self):
        self.price = int(self.price * self.increase)

    @classmethod
    def set_priceIncrease(cls, amount):
        cls.increase = amount

    @classmethod
    def from_string(cls, fnk_str):
        name, price, franchise, year = fnk_str.split('-')
        return cls (name, price, franchise, year)

    @staticmethod
    def is_MarvelMovieReleaseDay(day):
        if day.weekday()== 4 or  day.weekday()==3:
            return True
        else:
            return False

import datetime
my_date = datetime.date (2021, 9,3)




class Dorbz (Funko):
    def __init__(self, name, price, franchise, year,size):
        super().__init__(name,price,franchise,year)
        self.size=size
    increase = 0.5
class MysteryMinis (Dorbz):
    def __init__(self,name,price,franchise,year, size,spring):
        super().__init__(name,price,franchise, year, size)
        self.spring=spring
    increase = 1.25
fnk_1 = Dorbz('Batman', 12, 'DC Comics', 2008,3)
fnk_2 = MysteryMinis('Pink Batman', 1500, 'DC Comics', 2018,8,"no spring")

print(fnk_2.price)
fnk_2.priceIncrease()
print(fnk_2.price)
print(fnk_2.spring)
print(isinstance(fnk_1,MysteryMinis))