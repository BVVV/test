
content = "haha"
def pretalk():
    print("prepare for talking.")

class Person(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        pretalk()
        print("%s is talking %s" % (self.name, content))


p = Person("sanmao")
p.talk()