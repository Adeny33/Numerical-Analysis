#Single Step with Modified Euler

x = [0.7, 1.4, 2.1, 2.8, 3.5, 4.0]
y_me = [0.3, 0, 0, 0, 0, 0]
h = 0.7

#Slope 
def f(x: int, y: int):
    return 6 + x*y + y**2

#Finding initial ys with modified euler method
for i in range(1, 5):
    y_me[i] = y_me[i-1] + h*f((x[i-1] + h/2), (y_me[i-1] + (h/2)*f(x[i-1], y_me[i-1])))
    print(f"x = {x[i]}, y = {y_me[i]}")


# #y'(2.8)
# #Finding Predictior with Adams-Bashford
# y = y_me.copy()
# i = 2
# y_ab = y_me[i] + h/24 * (55*f(x[i], y_me[i]) -59*f(x[i-1], y_me[i-1]) + 37*f(x[i-2], y_me[i-2]) - 9*f(x[i-3], y_me[i-3]))
# y[i+1] = y_ab
# print("y values after predictor for f'(2.8): \n", y[:3])

# #Finding corrector with Adams-Moulton
# y_am = y[i] + (h/24)*(9*f(x[i+1], y[i+1]) + 19*f(x[i], y[i]) - 5*f(x[i-1], y[i-1]) + f(x[i-2], y[i-2]))
# print("Corrector first iteration: \n", y_am)

# #2nd Adams-Moulton iteration
# y_am2 = y[i] + (h/24)*(9*f(x[i+1], y_am) + 19*f(x[i], y[i]) - 5*f(x[i-1], y[i-1]) + f(x[i-2], y[i-2]))
# print("Corrector second iteration: \n", y_am2)


#y'(3.5)
#Finding Predictior with Adams-Bashford
y = y_me.copy()
i = 3
y_ab = y_me[i] + h/24 * (55*f(x[i], y_me[i]) - 59*f(x[i-1], y_me[i-1]) + 37*f(x[i-2], y_me[i-2]) - 9*f(x[i-3], y_me[i-3]))
y[i+1] = y_ab
print("y values after predictor for f'(3.5): \n", y[:5])
print("Predictor: ", y_ab)

#Finding corrector with Adams-Moulton
y_am = y[i] + (h/24)*(9*f(x[i+1], y[i+1]) + 19*f(x[i], y[i]) - 5*f(x[i-1], y[i-1]) + f(x[i-2], y[i-2]))
print("Corrector first iteration: \n", y_am)

#2nd Adams-Moulton iteration
y_am2 = y[i] + (h/24)*(9*f(x[i+1], y_am) + 19*f(x[i], y[i]) - 5*f(x[i-1], y[i-1]) + f(x[i-2], y[i-2]))
print("Corrector second iteration: \n", y_am2)
