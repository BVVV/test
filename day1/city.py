import os

def ls(path, depth=0):
    if os.path.isdir(path):
        files = os.listdir(path)
        for item in files:
            for i in range(depth):
                print('\t', end='')
            print(item)
            itempath = path+"/"+item
            if os.path.isdir(itempath):
                ls(itempath,depth+1)
    else:
        print('path does not exist')


path = input('please type a dir name:')
ls(path)
