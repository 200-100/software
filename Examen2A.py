import numpy as np

sen=.7071
cos=.7071
tan=1

CosA=.7071
SenA=.7071
##########################################################
#Vértices del cubo unitario
v1 = np.matrix([[0],[1],[1],[1]])
v2 = np.matrix([[0],[0],[1],[1]])
v3 = np.matrix([[1],[0],[1],[1]])
v4 = np.matrix([[1],[1],[1],[1]])
v5 = np.matrix([[0],[1],[0],[1]])
v6 = np.matrix([[0],[0],[0],[1]])
v7 = np.matrix([[1],[0],[0],[1]])
v8 = np.matrix([[1],[1],[0],[1]])
###########################################################

#Rotación en Y
Ry = np.matrix([[cos,0,sen,0],
		[0,1,0,0],
		[-sen,0,cos,0],
		[0,0,0,1]])

p1=Ry*v1
p2=Ry*v2
p3=Ry*v3
p4=Ry*v4
p5=Ry*v5
p6=Ry*v6
p7=Ry*v7
p8=Ry*v8

print("Rotación en Y")
print("1\n",p1)
print("\n2\n",p2)
print("\n3\n",p3)
print("\n4\n",p4)
print("\n5\n",p5)
print("\n6\n",p6)
print("\n7\n",p7)
print("\n8\n",p8)

#Rotación en Z
Rz = np.matrix([[cos,sen,0,0],
		[-sen, cos, 0,0],
		[0,0,1,0],
		[0,0,0,1]])

pp1=Rz*p1
pp2=Rz*p2
pp3=Rz*p3
pp4=Rz*p4
pp5=Rz*p5
pp6=Rz*p6
pp7=Rz*p7
pp8=Rz*p8

print("\nRotación en Z")
print("\n1\n",pp1)
print("\n2\n",pp2)
print("\n3\n",pp3)
print("\n4\n",pp4)
print("\n5\n",pp5)
print("\n6\n",pp6)
print("\n7\n",pp7)
print("\n8\n",pp8)


#Rotación en X de todos los vértices a un cierto ángulo
Rx = np.matrix([[1,0,0,0],
		[0,CosA, -SenA,0],
		[0,SenA,CosA,0],
		[0,0,0,1]])

CR1=Rx*pp1
CR2=Rx*pp2
CR3=Rx*pp3
CR4=Rx*pp4
CR5=Rx*pp5
CR6=Rx*pp6
CR7=Rx*pp7
CR8=Rx*pp8

print("\nRotación en X con 45°")
print("\n1\n",CR1)
print("\n2\n",CR2)
print("\n3\n",CR3)
print("\n4\n",CR4)
print("\n5\n",CR5)
print("\n6\n",CR6)
print("\n7\n",CR7)
print("\n8\n",CR8)

#Rotación en z de regreso
Rz2 = np.matrix([[cos,-sen,0,0],
		[sen, cos, 0,0],
		[0,0,1,0],
		[0,0,0,1]])

CoR1=Rz2*CR1
CoR2=Rz2*CR2
CoR3=Rz2*CR3
CoR4=Rz2*CR4
CoR5=Rz2*CR5
CoR6=Rz2*CR6
CoR7=Rz2*CR7
CoR8=Rz2*CR8

print("\nRotación en Z de regreso")
print("\n1\n",CoR1)
print("\n2\n",CoR2)
print("\n3\n",CoR3)
print("\n4\n",CoR4)
print("\n5\n",CoR5)
print("\n6\n",CoR6)
print("\n7\n",CoR7)
print("\n8\n",CoR8)


#Rotación en y de regreso
Ry2 = np.matrix([[cos,0,sen,0],
		[0,1,0,0],
		[-sen,0,cos,0],
		[0,0,0,1]])

CoR1p=Ry2*CoR1
CoR2p=Ry2*CoR2
CoR3p=Ry2*CoR3
CoR4p=Ry2*CoR4
CoR5p=Ry2*CoR5
CoR6p=Ry2*CoR6
CoR7p=Ry2*CoR7
CoR8p=Ry2*CoR8

#Impresión de los vértices en su posición anterior
print("\nRotación en Y de regreso")
print("\n1\n",CoR1p)
print("\n2\n",CoR2p)
print("\n3\n",CoR3p)
print("\n4\n",CoR4p)
print("\n5\n",CoR5p)
print("\n6\n",CoR6p)
print("\n7\n",CoR7p)
print("\n8\n",CoR8p)
