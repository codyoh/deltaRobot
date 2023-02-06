import math
import time
import serial

E_x = 0
E_y = 0
E_z = -150

# theta = -49.2

r_b = 100
r_e = 35
l_b = 100
l_f = 150

def quadraticEqn(a, b ,c):
    discriminant = (b ** 2 - 4*a*c)
    plus = (-b + math.sqrt(discriminant)) / (2 * a)
    minus = (-b - math.sqrt(discriminant)) / (2 * a)
    return plus, minus

def findOneArmAngle(E_x, E_y, E_z):
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

    y1 = quadraticEqn(a, b, c)[0]
    y2 = quadraticEqn(a, b, c)[1]

    x1 = y1 * gamma + delta
    x2 = y2 * gamma + delta

    y_j1_1 = x1 - r_b
    y_j1_2 = x2 - r_b

    z_j1_1 = y1
    z_j1_2 = y2

    theta1 = math.atan2(z_j1_1, y_j1_1) * 57.29
    theta2 = math.atan2(z_j1_2, y_j1_2) * 57.29

    print("theta2 = ", theta2)
    # print("theta1 = ", theta1)
    # output = f"({x1}, {y1}) => theta = {theta1}  \n  ({x2}, {y2}) => theta = {theta2} "
    # print("gamma = ", gamma)
    # print("x1 = ", x1)
    # print("y1 = ", y1)
    # print("x2 = ", x2)
    # print("y2 = ", y2)

    # print("y_j1_1 = ", y_j1_1)
    # print("z_j1_1 = ", z_j1_1)

    # print("y_j1_2 = ", y_j1_2)
    # print("z_j1_2 = ", z_j1_2)

    return theta2

def rotatePt(x0, y0, angle):
    x1 = math.cos(angle) * x0 - math.sin(angle) * y0
    y1 = math.sin(angle) * x0 + math.cos(angle) * y0
    return x1, y1

def findReverseKinematicAngles(E_x, E_y, E_z):
    
    theta2InputCoordinates = rotatePt(E_x, E_y, 120/57.29)
    theta3InputCoordinates = rotatePt(E_x, E_y, -120/57.29)

    th1 = findOneArmAngle(E_x, E_y, E_z)
    th2 = findOneArmAngle(theta2InputCoordinates[0], theta2InputCoordinates[1], E_z)
    th3 = findOneArmAngle(theta3InputCoordinates[0], theta3InputCoordinates[1], E_z)

    print(th1, th2, th3)
    return th1, th2, th3
    
# findReverseKinematicAngles(E_x, E_y, E_z)






    # print("z0 entered", E_z)
    # print("z0 by analysis", z0)

    # print("theta by analysis: ", math.atan2(-75.72, 65.32)*57.29)
    # print(output)

    # print("atan test (3, 4): ", math.atan2(3, (3 * math.sqrt(3))) * 57.29)
    # print("asin test (3/5): ", math.asin(3/6) * 57.29)

    # theta2Test = math.asin(z_j1_2/l_b) * 57.29
    # print("theta2Test = ", theta2Test)

    # theta1Test = math.asin(z_j1_1/l_b)
    # print("theta1Test = ", theta1Test)

def z0calculator(theta, l_b, l_f, r_b, r_e):
    z1 = (l_b * math.sin(theta))
    print("sinTheta", math.sin(theta))
    internal = (r_b - r_e + l_b*math.cos(theta))**2
    print("internal: ", internal)
    x = math.sqrt(l_f**2 - internal )
    print("x", x)
    z0 = z1 + x
    return z0

# z0 = z0calculator(theta2, l_b, l_f, r_b, r_e)