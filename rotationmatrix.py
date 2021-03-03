import numpy as np
import math as m 

//  Original point in frame B
Bp = np.matrix([[2],
                [3],
                [0]])

//  Rotation matrix around x
Rx = np.matrix([[ 1, 0           , 0           ],
                   [ 0, m.cos(30),-m.sin(30)],
                   [ 0, m.sin(30), m.cos(30)]])

//  Rotation matrix around y
Ry = np.matrix([[ m.cos(30), 0, m.sin(30)],
                   [ 0           , 1, 0           ],
                   [-m.sin(30), 0, m.cos(30)]])

Rz = np.matrix([[  m.cos(30),-m.sin(30),0],
                   [  m.sin(30), m.cos(30)],0
                   [0       ,0          1]])

P1 = Rx * Bp
P2 = Ry * P1
P3 = Rz * P2

//  Point in frame A
print(P3)




