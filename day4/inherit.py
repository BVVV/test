
class A(object):
    def say(self):
        print("A")


class B(A):
    pass
    # def say(self):
    #     print("B")

class C(A):
    name = 'zhangsan'
    def s(self):
        self.say()

class D(B,C):
    def __init__(self):
        print("D")

def _say():
    print("hello")

if __name__ == "__init__":
    d = D()
    d.s()
    d.__init__()
