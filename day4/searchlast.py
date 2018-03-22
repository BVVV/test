
import re


s = "name1.name2.name3"
s1 = "parent.parent.parent.xxx.yyy"
s = "."+s
print(s)


while True:
    if re.search("^parent\.", s1):
        index = s.rfind(".")
        s = s[0:index]
        s1 = re.sub("^parent\.", "", s1)
    else:
        break
s2 = (s+"."+s1)
s = "xxx.aaa.bbb[yyy]"
s1 = re.sub("\[.*]", "", s)
print(s1)
