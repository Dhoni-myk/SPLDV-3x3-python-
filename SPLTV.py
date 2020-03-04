import numpy as np

print('masukkan nilai dengan "a1X + b1Y + c3Z = C1 dan a2X + b1Y = C2"') 
a1 = int(input('Masukkan nilai a1= '  ))
b1 = int(input('Masukkan nilai b1= '  ))
c1 = int(input('Masukkan nilai c1= '  ))
d1 = int(input('Masukkan nilai d1= '  ))
a2 = int(input('Masukkan nilai a2= '  ))
b2 = int(input('Masukkan nilai b2= '  ))
c2 = int(input('Masukkan nilai c2= '  ))
d2 = int(input('Masukkan nilai d2= '  ))
a3 = int(input('Masukkan nilai a3= '  ))
b3 = int(input('Masukkan nilai b3= '  ))
c3 = int(input('Masukkan nilai c3= '  ))
d3 = int(input('Masukkan nilai d3= '  ))

D = np.array([[a1,b1,c1],[a2,b2,c2],[a3,b3,c3]])
Dx = np.array([[d1,b1,c1],[d2,b2,c2],[d3,b3,c3]])
Dy = np.array([[a1,d1,c1],[a2,d2,c2],[a3,d3,c3]])
Dz = np.array([[a1,b1,d1],[a2,b2,d2],[a3,b3,d3]])

det = np.linalg.det(D)
det1 = np.linalg.det(Dx)
det2 = np.linalg.det(Dy)
det3 = np.linalg.det(Dz)

x = det1/det
y = det2/det
z = det3/det
print(x)
print(y)
print(z)
