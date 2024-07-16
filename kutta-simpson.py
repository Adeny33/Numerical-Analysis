import math
#Slope
def f(x: int, y: int):
    return 35 * (math.e)**(x) * math.sin(y)


x = [0.4, 0.6, 0.8, 1.0]
y_rk = [0.7, 0, 0, 0]
h = 0.2


for i in range(1, 4):
    k1 = h*f(x[i-1],y_rk[i-1])
    k2 = h*f(x[i-1] + h/2,y_rk[i-1] + k1/2)
    k3 = h*f(x[i-1] + h/2,y_rk[i-1] + k2/2)
    k4 = h*f(x[i-1] + h,y_rk[i-1] + k3)
    y_rk[i] = y_rk[i-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    print(f"k1 = {k1}, k2 = {k2}, k3 = {k3}, k4 = {k4}\ny_rk{i} = {y_rk[i]}\n")


print("y_rk: ", y_rk)
#Corrector method
max_iter = 5
iter = 0
y_ms1 = 0
y_ms2 = 0
y_ms = y_rk.copy()
for i in range(1, 3):
    
    f1 = f(x[1],y_rk[1])
    f2 = f(x[2],y_rk[2])
    f3 = f(x[3],y_rk[3])
    y_ms[i] = y_rk[1] + (h/3)*(f3 + 4*f2 +f1)
    y_rk[3] = y_ms[-1]
    print(f"f1 = {f1}, f2 = {f2}, f3 = {f3}")
    print(f"y_ms{i}: ", y_ms[-1])
    if i >= 2:
        print("Error: ", abs(y_ms[i] - y_ms[i-1]), "\n")