

class Stimgen(object):
    registers = []
    instances = []

    def addreg(self, reg):
        self.registers.append(reg)

    def addins(self, ins):
        self.instances.append(ins)


class Reg(object):
    def __init__(self, name, length, reset, superior, cond=False):
        self.name = name
        self.reset = reset
        self.length = length
        self.value = reset
        self.cond = cond
        self.superior = superior

class Ins(object):
    def __init__(self, name, cond):
        self.name = name
        self.cond = cond


stimgen = Stimgen()
ir = Reg("ir", 8, 0x2, True)
stimgen.addreg(ir)
idcode = Reg("idcode", 32, 0x05dc103d, "ir==0x2")
stimgen.addreg(idcode)
print(idcode.islighten())
print(eval("1+1==0x2"))
