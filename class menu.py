class menu:
        def __init__(self):
                self.Menu = {'Plain dosa':'25','Idly':'20','Upma':'30','Rava idly':'35'}
        def show(self):
                print '\n'
                for key,value in self.Menu.items():
                        #print("%s\tRs.%s" %(key,value))
                        print("{0} - Rs. {1}".format(key, value))
        def add(self,s,n):
                #self.item = raw_input("\nEnter the item to be added : ")
                #self.Menu[self.item] = input("Enter the price of the item : ")
                self.Menu[s] = n
                
c=menu()
d=menu()
while (1):
        a = input("\n(1)Display menu.\n(2)Add item.\n(3)Exit.\nEnter your choice : ")
        if a==1:
                c.show()
        elif a==2:
                #c.add("Pongal",20)
                c.add(raw_input("Enter the item to be added : "),input("Enter the price of the item : "))
        elif a==3:
                break
        else:
                print("\nInvalid choice.")
d.show()
