import cmath
import math
def root(a,b,c):
    D = b*b - 4*a*c
    if D>0:
       root1 = (-b + math.sqrt(D))/2.0*a
       root2 = (-b - math.sqrt(D))/2.0*a
       return (root1,root2)
    elif D==0:
       root1 = root2 = -b/2.0*a
       return (root1,root2)
    else:
       realp = -b/(2.0*a)
       imgp = cmath.sqrt(math.fabs(D))/(2.0*a)
       root1 = complex(realp,imgp)
       root2 = complex(realp,-imgp)
       return (root1,root2)

a =  input("Enter the value of a:")
b =  input("Enter the value of b:")
c =  input("Enter the value of c:")
root(a,b,c)
root1,root2 = root(a,b,c)
print "The roots are : " ,root1,root2


