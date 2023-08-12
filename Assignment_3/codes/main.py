import numpy as np

#Given that, 
A = np.array([[1],[-1]])
B = np.array([[-4],[6]])
C = np.array([[-3],[-5]])

#From A and B, we can say that AB and BC are
AB=A-B
BC=B-C

#Now we calculate the constant terms of the vector equations of the lines perpendicular to AB and BC
constant_AB=AB.T@C
constant_BC=BC.T@A
print(constant_AB)
#Now the cooefficient terms of the vector equations will be 
P=np.block([[AB.T],[BC.T]])

#and the constant terms of the vector equations will be
R=np.block([[constant_AB],[constant_BC]])

#Now we use the below commmand to solve both the equations and find orthocenter 
H = np.linalg.solve(P,R) #Orthocenter 
#Now we calculate the LHS of the question
product = (A - H).T@(B - C)
print(product)
#Hence proved..



