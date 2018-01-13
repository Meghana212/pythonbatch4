class iter_protocol:
    def __init__(self,n):
        self.i = 0
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self
    def next(self):
        if self.i<self.n:
            item = self.a
            self.a,self.b = self.b,(self.a+self.b)
            self.i+=1
            return item
        else:
            raise StopIteration
        
def lists(n):
    a=0
    b=1
    i=2
    fiblist=[a,b]
    while i<n:
        fiblist.insert(i,a+b)
        a,b=b,a+b
        i=i+1
    return fiblist

def generators(n):
    a=0
    b=1
    i=0
    while i<n:
        if i==0:
            yield 0
            i = i+1
        elif i==1:
            yield 1
            i=i+1
        else:
            yield (a+b)
            a,b=b,a+b
            i=i+1

while(1):
    a = input("(1)Iterate using iteration protocol.\n(2)Iterate using lists.\n(3)Iterate using generators.\n(4)Exit.\nEnter your choice : ")
    if a==1:
        n = input("Enter the number of elements of the fibonacci series to be printed : ")
        for item in iter_protocol(n):
            print item
    elif a==2:
        n = input("Enter the number of elements of the fibonacci series to be printed : ")
        for item in lists(n):
            print item
    elif a==3:
        n = input("Enter the number of elements of the fibonacci series to be printed : ")
        for item in generators(n):
            print item
    elif a==4:
        break
    else:
        print("Invalid choice.\n")



        
            
            
