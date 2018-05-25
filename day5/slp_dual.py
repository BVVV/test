# single layer perceptron dual form
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
    if (w[0] == 0) and (w[1] == 0):
        print("Can not draw a line with w = [0,0] !!!")
        return
    elif w[1] == 0:
        line_x = [-b/w[0], -b/w[0]]
        line_y = [0, 10]
    else:
        for i in range(len(line_x)):
            line_y[i] = (-w[0] * line_x[i] - b)/w[1]
    plt.plot(line_x, line_y)

x = np.array([[3,3], [4,3], [1,1]])
y = np.array([1,1,-1])

gram = np.dot(x, x.T)
print(gram)

a = np.array([0, 0, 0])
for j in range(100):
    wrong_pt_cnt = 0
    for i in range(len(y)):
        c = 0
        b = 0
        for k in range(len(y)):
            c += a[k] * y[k] * gram[k][i]
            b += a[k] * y[k]

        if y[i] != np.sign(c + b):
            a[i] += 1
            wrong_pt_cnt += 1

    if wrong_pt_cnt == 0:
        break

print(a)

w = [0, 0]
for k in range(len(y)):
    w += a[k] * y[k] * x[k]

draw_pts(x, y)
draw_line(w, b)
plt.show()
