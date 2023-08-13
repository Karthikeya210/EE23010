# #Code by GVV Sharma
# #December 7, 2019
# #released under GNU GPL
# #Drawing a triangle given 3 sides

# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# image = mpimg.imread('exit-ramp.jpg')
# plt.imshow(image)
# plt.show()

import sys                                          #for path to external scripts
#sys.path.insert(0, '/home/user/txhome/storage/shared/gitlab/res2021/july/conics/codes/CoordGeo')        #path to my scripts
sys.path.insert(0, '/home/karthikeya/Desktop/Probability/Assignment_3/codes/CoordGeo')        #path to my scripts
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
from params import omat

#sys.path.insert(0, '/home/user/txhome/storage/shared/gitlab/res2021/july/conics/codes/CoordGeo')        #path to my scripts

#if using termux
import subprocess
import shlex
#end if


#Given that,
A = np.array([1,-1])
B = np.array([-4, 6])
C = np.array([-3,-5])

#The foot of the altitudes from A,B,C are respectively
D1 = alt_foot(A,B,C)
E1 = alt_foot(B,A,C)
F1 = alt_foot(C,A,B)

#The normal vectors of BE1 and CF1 are 
n_BE1 = C - A
n_CF1 = B - A

print(f"The equation of BE1 in vector form {n_BE1}x = {n_BE1@B}")
print(f"The equation of BE1 in vector form {n_CF1}x = {n_CF1@C}")







