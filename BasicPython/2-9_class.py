class Car:
    def __init__(self, company, cc, grade):
           self.company=company
           self.cc = cc
           self.grade = grade


    def parking(self):
           print('parked')


torres = Car( 'KGM', 1500, '소형')
sonata = Car('HyunDai', 2000, '중형')


print(torres.company, f'{toress.cc}cc', toress.grade)
print(sonata.company, f'{sonata.cc}cc', sonata.grade)


torres.parking()


class Fruits:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    def __str__(self):
        return f'{self.name} : {self.cost}won'


class Sale(Fruits):
    def __init__(self, name, cost, sail):
        super().__init__(name, cost)
        self.sail = sail


    def price(self):
        self.cost = self.cost * self.sail
        return self.cost


apple = Sale('apple', 5000, 0.9)
print(apple)


appleSailResult = str(apple.name) + ' =sail=> ' + f'{apple.price()}'
print(appleSailResult)
