class Person(object):
    n = 123

    def __init__(self, name):
        self.name = name
        self.s = ""
    @classmethod
    def talk(self):
        print("%s is talking" % self.n)

    @staticmethod
    def eat(food):
        print(" is eating %s" % (food))

    @property
    def status(self):
        if self.s:
            print("my status is : %s" % self.s)
        else:
            print("I have no status")

    @status.setter
    def status(self, state):
        self.s = state

    @status.deleter
    def status(self):
        print("my status is deleted!")

p1 = Person("zhangsan")
p1.talk()
p1.eat("baozi")
p1.status
p1.status = "unhappy"
p1.status
del p1.status
p1.status