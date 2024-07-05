import numpy as np

mat = np.array([[28,21,5,1000],[7,17,3,500],[12,11,24,750]])
x = y = z = 20
w = 0.1
e = 0.01


x1 = (w/mat[0][0])*(mat[0][3] - mat[0][1]*y- mat[0][2]*z) + (1-w)*x
y1 = (w/mat[1][1])*(mat[1][3] - mat[1][0]*x1- mat[1][2]*z) + (1-w)*y
z1 = (w/mat[2][2])*(mat[2][3] - mat[2][0]*x1- mat[2][1]*y1) + (1-w)*z

print("SOR")
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}\n")

iteration = 1
print(f"x{iteration} = {x1}")
print(f"y{iteration} = {y1}")
print(f"z{iteration} = {z1}\n")

while (abs(x1 - x) >= e) | (abs(y1 - y) >= e) | (abs(z1 - z) >= e):
    x = x1
    y = y1
    z = z1
    x1 = (w/mat[0][0])*(mat[0][3] - mat[0][1]*y- mat[0][2]*z) + (1-w)*x
    y1 = (w/mat[1][1])*(mat[1][3] - mat[1][0]*x1- mat[1][2]*z) + (1-w)*y
    z1 = (w/mat[2][2])*(mat[2][3] - mat[2][0]*x1- mat[2][1]*y1) + (1-w)*z
    iteration += 1
    print(f"x{iteration} = {x1}")
    print(f"y{iteration} = {y1}")
    print(f"z{iteration} = {z1}\n")
    if iteration == 5:
        break