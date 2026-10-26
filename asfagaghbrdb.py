class Car:

    def __init__(self, mark, truk):
        self.__mark = self.set_mark(mark=mark)
        self.__truk = 0

    def set_mark(self, mark):
        if isinstance(mark, str):
            return mark
        else: exit("Нельзя так")

    def get_mark(self):
        return self.__mark


    def drive(self, mark):
        print(f"{mark} едет")


class Gruz(Car):
    def gruzit(self):
        self.__truk += 1
        print("Вы загрузили багажник")
    def razgruz(self):
        self.__truk -=1
        print("Вы разгрузили багажник")


