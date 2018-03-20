import re

condition = "usb_t.WIR!=9'h02 && broadcasten && 1'b1 && True && P1687A_SIB == 9'B0001101 || usb_t.BROADCASTEN && usb_t.BYPASSEN==0 && usb_t.WIR!=9'h02"
condition = re.sub("\d+'[bB]", "0b", condition)
condition = re.sub("\d+'[hH]", "0x", condition)
condition = re.sub("\s+", "", condition)
print(condition)
condlist = re.split("\|\|", condition)
print(condlist)
cond0 = condlist[0]
condlist1 = re.split("&&", cond0)
print(condlist1)

def get_relative_reg(name):
    return name
def get_field(name):
    return name
t = []
for cond in condlist1:
    if "==" in cond:
        tmp = re.split("==", cond)
        if '[' not in tmp[0]:
            reg = get_relative_reg(tmp[0])
        else:
            reg = get_field(tmp[0])
        t.append([reg, tmp[1]])
    elif "!=" in cond:
        print("Error in condition: %s" % cond)
    else:
        try:
            if eval(cond):
                pass
        except Exception:
            t.append([get_relative_reg(cond), True])

print(t)