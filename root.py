import math
def root():
    a =  input("Enter the value of a:")
    b =  input("Enter the value of b:")
    c =  input("Enter the value of c:")
    D = b*b - 4*a*c
    if D>0:
       print("The roots are real.")
       root1 = (-b + math.sqrt(D))/2.0*a
       root2 = (-b - math.sqrt(D))/2.0*a
       print "The roots are : " ,root1,root2
    elif D==0:
       print("The roots are equal.")
       root1 = root2 = -b/2.0*a
       print "The roots are : Root 1 = Root 2 = " ,root1
    else:
       print("The roots are imaginary.")
       realp = -b/(2.0*a)
       imgp = math.sqrt(math.fabs(D))/(2.0*a)
       print "The roots are : {0} + {1}i , {0} - {1}i".format(realp, imgp)
root()
