mat = [[3,1,1,20], [1,5,1,60], [2,3,6,40]]
x = y = z = 0
coorndinates = [x,y,z]
e = 0.1
x1 = (1/mat[0][0])*(mat[0][3] - mat[0][1]*y- mat[0][2]*z)
y1 = (1/mat[1][1])*(mat[1][3] - mat[1][0]*x1- mat[1][2]*z)
z1 = (1/mat[2][2])*(mat[2][3] - mat[2][0]*x1- mat[2][1]*y1)
iteration = 1
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
print(f"x{iteration} = {x1}")
print(f"y{iteration} = {y1}")
print(f"z{iteration} = {z1}")

while (abs(x1 - x) >= e) | (abs(y1 - y) >= e) | (abs(z1 - z) >= e):
    x = x1
    y = y1
    z = z1
    x1 = (1/mat[0][0])*(mat[0][3] - mat[0][1]*y- mat[0][2]*z)
    y1 = (1/mat[1][1])*(mat[1][3] - mat[1][0]*x1- mat[1][2]*z)
    z1 = (1/mat[2][2])*(mat[2][3] - mat[2][0]*x1- mat[2][1]*y1)
    iteration += 1
    print(f"x{iteration} = {x1}")
    print(f"y{iteration} = {y1}")
    print(f"z{iteration} = {z1}")
    

