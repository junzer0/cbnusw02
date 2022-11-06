from math import*

def angle(x1,y1,z1,x2,y2,z2,x3,y3,z3):
    ax,ay,az = x1-x2, y1-y2, z1-z2 ; bx,by,bz = x3-x2, y3-y2, z3-z2
    a = sqrt(ax**2+ay**2+az**2) ; b = sqrt(bx**2+by**2+bz**2)
    adotb=ax*bx+ay*by+az*bz
    temp=adotb/(a*b)
    temp=1 if temp > 1 else temp
    temp=-1 if temp < -1 else temp
    theta=acos(temp)*180/3.141592654
    return theta
    
while True:
    x1,y1,z1 = map(float, input('Point 1: x1,y1,z1').split())
    x2,y2,z2 = map(float, input('Point 2: x2,y2,z2').split())
    x3,y3,z3 = map(float, input('Point 3: x3,y3,z3').split())
    x4,y4,z4 = map(float, input('Point 4: x4,y4,z4').split())
    
    a1=angle(x2,y2,z2,x1,y1,z1,x4,y4,z4)
    a2=angle(x1,y1,z1,x2,y2,z2,x3,y3,z3)
    a3=angle(x2,y2,z2,x3,y3,z3,x4,y4,z4)
    a4=angle(x1,y1,z1,x4,y4,z4,x3,y3,z3)
    
    print('Theta_P1, Theta_P2, Theta_P3, Theta_P4(deg.)={0:7.2f}{1:7.2f}{2:7.2f}{3:7.2f}'.format(a1,a2,a3,a4))
    print('sum of angle(deg.)={0:7.2f}'.format(a1+a2+a3+a4))
    