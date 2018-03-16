#-*-encoding:utf-8-*-

f = open('smth.txt','r+',encoding='utf-8')
text = f.read()
text = text.replace('红黄蓝', '真黑')
f.seek(0)
f.truncate()
f.write(text)
f.close()
