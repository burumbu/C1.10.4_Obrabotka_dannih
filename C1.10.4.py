class User:
    def __init__(self, name=None): # init with 2 '_'->__init__
        self.name = name
class Stat(User):
    def __init__(self, name, city=None, status=None): ## init with 2 '_'->__init__
        super().__init__(name)
        self.status = status
        self.city = city
    def get_info(self):
            return f"{self.name} {self.city}. {self.status}" # add f in string
    def get_name(self):
            return self.name
    def get_city(self):
            return self.city
    def get_status(self):
            return self.status
if __name__ == '__main__':
        Man_1 = Stat("Иван Петров", "г. Москва", "Наставник")
        print(Man_1.get_info())