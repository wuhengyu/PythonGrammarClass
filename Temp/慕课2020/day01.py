class Person(object):
    name = '吴恒宇'

    def dump(self):
        print(f'{self.name} is dumping')


xiaomu = Person()
print(xiaomu.name)
xiaomu.dump()
