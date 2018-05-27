import numpy as np
import matplotlib.pyplot as plt


def draw_pts(x, y):
    for i in range(len(y)):
        if y[i] == 1:
            plt.plot(*x[i], 'ro')
        else:
            plt.plot(*x[i], 'bo')


def draw_line(w, b):
    line_x = [0, 10]
    line_y = [0, 0]
    if w[0] == 0 and w[1] == 0:
        print("Error: Can't draw a line with w = [0, 0]")
    elif w[1] == 0:
        line_x = [-b / w[0], -b / w[0]]
        line_y = [0, 10]
    else:
        line_y = [(w[0] * line_x[0] + b)/-w[1], (w[0] * line_x[1] + b)/-w[1]]
    plt.plot(line_x, line_y)


x = np.array([[3, 3], [4, 3], [1, 1], [2, 1], [3, 1], [2, 8]])
y = np.array([1, 1, -1, -1, 1, 1])
w = np.array([1, 0])
m = np.dot(x, w)
lr = 1
gram = np.dot(x, x.T)
print(gram)

l = [0] * len(y)
a = np.array(l)
for k in range(100):
    wrong_pts_num = 0
    for j in range(len(y)):
        c = m[j]
        b = 0
        for i in range(len(y)):
            c += a[i] * y[i] * gram[i, j]
            b += a[i] * y[i]
        #print("j = %s, c = %s, b = %s" % (j, c, b))
        if y[j] != np.sign(c + b):
            a[j] += 1
            wrong_pts_num += 1
    if wrong_pts_num == 0:
        break

for i in range(len(y)):
    w += a[i] * y[i] * x[i]

print("w = %s, b = %s, wrong_pts_num = %s" % (w, b, wrong_pts_num))
print("a = %s." % a)

draw_pts(x, y)
draw_line(w, b)
plt.show()
