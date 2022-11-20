import math

E_x = 0
E_y = 0
E_z = -57

theta1 = 0

r_b = 100
r_e = 30
l_b = 140
l_f = 170

h1 = r_b
k1 = 0
R = l_b

h2 = E_y + r_e
k2 = E_z
r = math.sqrt(l_f**2 - E_x**2)


gamma = (k1 - k2) / (h2 - h1)
delta = (R**2 - r**2 - h1**2 + h2**2 - k1**2 + k2**2) / (2 * (h2 - h1))

a = gamma**2 + 1
b = 2 * (gamma * delta - h1 * gamma - k1)
c = delta**2 - (2 * h1 * delta) - R**2 + h1**2 + k1**2

def quadraticEqn(a, b ,c):
    discriminant = (b ** 2 - 4*a*c)
    plus = (-b + math.sqrt(discriminant)) / (2 * a)
    minus = (-b - math.sqrt(discriminant)) / (2 * a)
    return plus, minus

y1 = quadraticEqn(a, b, c)[0]
y2 = quadraticEqn(a, b, c)[1]


print("gamma = ", gamma)


x1 = y1 * gamma + delta
x2 = y2 * gamma + delta

print("x1 = ", x1)
print("y1 = ", y1)

print("x2 = ", x2)
print("y2 = ", y2)

y_j1_1 = x1 - r_b
y_j1_2 = x2 - r_b

z_j1_1 = y1
z_j1_2 = y2

print("y_j1_1 = ", y_j1_1)
print("z_j1_1 = ", z_j1_1)

print("y_j1_2 = ", y_j1_2)
print("z_j1_2 = ", z_j1_2)


theta1 = math.atan2(z_j1_1, y_j1_1) * 57.29
theta2 = math.atan2(z_j1_2, y_j1_2) * 57.29

output = f"({x1}, {y1}) => theta = {theta1}  \n  ({x2}, {y2}) => theta = {theta2} "

print(output)

print("atan test (3, 4): ", math.atan2(3, (3 * math.sqrt(3))) * 57.29)
print("asin test (3/5): ", math.asin(3/6) * 57.29)

theta2Test = math.asin(z_j1_2/l_b) * 57.29
print("theta2Test = ", theta2Test)

theta1Test = math.asin(z_j1_1/l_b)
print("theta1Test = ", theta1Test)