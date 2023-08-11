import numpy as np

#Given that, 
A = np.array([[1],[-1]])
B = np.array([[-4],[6]])
C = np.array([[-3],[-5]])

#From A and B, we can say that AB and BC are
AB=A-B
BC=B-C

#Now we calculate the constant terms of the vector equations of the lines perpendicular to AB and BC
constant_AB=np.dot(AB.T,C)
constant_BC=np.dot(BC.T,A)

#Now the cooefficient terms of the vector equations will be 
P=np.block([[AB.T],[BC.T]])

#and the constant terms of the vector equations will be
R=np.block([[constant_AB],[constant_BC]])

#Now we use the below commmand to solve both the equations and find orthocenter 
H = np.linalg.solve(P,R) #Orthocenter 
print(H)
#Now we calculate the LHS of the question
product = np.dot((A - H).T,(B - C))
print(product)
#Hence proved..



