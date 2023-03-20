import math

#this calculates a value for theta3 of a given arm
#forearm length is the length of the forearm link of the arm
#y_i is the distance from the x_i, z_i plane that the bicep link of this arm rotates in
def theta3Calculator(forearmLength, y_i):
    theta3 = math.acos((y_i/forearmLength))
    return theta3

# calculating the length of the AiCi projection in the Xi, Zi plane
# this is how far away the base-bicep joint is from the forearm-endEffector joint, projected onto xi, Zi plane
# this is used in calculating the value of theta2 for the given arm
# inputs: ba
def A_i_C_iCalculator(baseRadius, eeRadius, ):
