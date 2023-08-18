import numpy as np
import math as mt
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

#Sample size
simlen = 10000
#Possible outcomes
n = range(0,7)
# Generate X1 and X2
y = np.random.randint(0,2, size=(6, simlen))

#Generate X
X = np.sum(y, axis = 0) 
#Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)
#Simulated probability
psim = counts/simlen
#Theoretical probability
p=0.5
panal=[]
#For every case append the probability value into the list 
for k in range(0,7):
	combination = mt.comb(6, k)*(p**k)*((1-p)**(6-k))
	panal.append(combination)
#Now find the max and its index to find the most likely outcome 
print(f"Therefore the most likely outcome is for X = {panal.index(max(panal))}")
#Plotting
plt.stem(n,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(n,panal, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.legend()
plt.grid()# minor

#If using termux
#plt.savefig('figs/pmf.pdf')
#plt.savefig('figs/pmf.png')
#subprocess.run(shlex.split("termux-open figs/pmf.pdf"))
#else
plt.savefig('/home/karthikeya/Desktop/Probability/New_assignment1/figs/figure1.png')
plt.show()

