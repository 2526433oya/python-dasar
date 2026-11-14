from abc import ABC, abstractmethod


class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass


class Kucing(Hewan):
    def suara(self):
        return "Meow"


class Anjing(Hewan):
    def suara(self):
        return "Guk guk"


k = Kucing()
a = Anjing()
print(k.suara())
print(a.suara())
