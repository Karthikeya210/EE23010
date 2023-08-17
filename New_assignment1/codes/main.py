import numpy as np
import math as mt

#Declaring n,p and the list that contains all the probabilities of eeach case 
n=6
p=0.5
P=[]
#For every case append the probability value into the list 
for k in range(0,7):
	combination = mt.comb(n, k)*(p**k)*((1-p)**(n-k))
	P.append(combination)
#Now find the max and its index to find the most likely outcome 
print(f"Therefore the most likely outcome is for X = {P.index(max(P))}")
