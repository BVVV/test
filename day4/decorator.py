
class Person(object):
    def __init__(self, name):
        self.name = name
        self.s = ""

    @staticmethod
    def eat(food):
        print(" is eating %s" % food)


def pretalk(func):
    def inner(name):
        print("%s is prepare for talking" % name)
        func(name)
    return inner
def pretalk2(func):
    def inner(name):
        print("%s is prepare 2 for talking" % name)
        func(name)
    return inner
def pretalk3(func):
    def inner(name):
        print("%s is prepare 3 for talking" % name)
        func(name)
    return inner
@pretalk3
@pretalk2
@pretalk
def talk(name):
    print("%s is talking" % name)


talk("dog")