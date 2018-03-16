import pickle
import os


class Crowd(object):
    def  __init__(self):
        self.persons = {}

    def add_person(self,person):
        self.persons[person.name] = person

    def show_person(self):
        for person in self.persons.values():
            print("name: "+person.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)


crowd = Crowd()
a = Person("A")
b = Person("B")
c = Person("C")
crowd.add_person(a)
crowd.add_person(b)
crowd.add_person(c)
#crowd.show_person()
# with open("po1", "wb") as f:
#     pickle.dump(crowd, f)
# with open("po1",  "rb") as f:
#     po = pickle.load(f)
ps = pickle.dumps(crowd)
print(ps)
po = pickle.loads(ps)
po.show_person()


