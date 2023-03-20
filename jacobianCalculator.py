import math
import numpy as np

#this calculates a value for theta3 of a given arm
#forearm length is the length of the forearm link of the arm
#y_i is the distance from the x_i, z_i plane that the bicep link of this arm rotates in
def theta3Calculator(forearmLength, y_i):
    theta3 = math.acos((y_i/forearmLength))
    return theta3

# calculating the length of the AiCi projection in the Xi, Zi plane
# this is how far away the base-bicep joint is from the forearm-endEffector joint, projected onto xi, Zi plane
# this is used in calculating the value of theta2 for the given arm
# inputs: the positions of Ai and Ci
def A_i_C_iCalculator(AiPosition, CiPosition):
    Ai_Ci_length = math.sqrt( (AiPosition[0] - CiPosition[0]) ** 2 + (AiPosition[2] - CiPosition[2]) ** 2 )
    return Ai_Ci_length

#calculates the value of theta2 for a given arm
def theta2Calculator(bicepLength, forearmLength, theta3i, AiCi):
    # psi is an intermediate variable that represents the internal angle between the bicep and forearm projection onto the XiZi plane
    # it is the supplement of theta2
    # we find it using the law of cosines
    psi = math.acos(( AiCi ** 2 - forearmLength ** 2 - (forearmLength * math.sin(theta3i)) ** 2 ) / ( -2 * bicepLength * forearmLength * math.sin(theta3i) ) )
    theta2i = 180 - psi
    return theta2i


#compiles all the values of thetas for x,y,z of each arm
# returns a 3x3 matrix
def thetaCompiler():
    


#calculate elements of the jacobian pose matrix
# inputs: matrix of all the theta values, the index of those to use, phi value
def J_ix(thetaMatrix):