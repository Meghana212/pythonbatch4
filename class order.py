class menu:
        def __init__(self):
                self.Menu = {}
        def show(self):
                print '\n'
                for key,value in self.Menu.items():
                        #print("%s\tRs.%s" %(key,value))
                        print("{0} - Rs. {1}".format(key, value))
        def add(self,s,n):
                self.Menu[s] = n
class keyerror(Exception):
        pass
class order:
        def __init__(self):
                self.Ord={}
        def add(self,x,y):                
                try:
                        if x in y.Menu:
                                self.Ord[x] = y.Menu[x]
                        else:
                                raise keyerror
                except keyerror:
                        print '\nItem is not in menu.order another item.\n'
        def show(self):
                print '\nOrdered items:'
                for key,value in self.Ord.items():
                        print("{0} - Rs.{1}".format(key,value))
                        
c=menu()
c.add("plain dosa",25)
c.add("idly",20)
c.add("upma",30)
c.add("rava idly",35)
c.add("pongal",20)
c.add("vada",15)
while (1):
        a = input("\n(1)Display menu.\n(2)Order item.\n(3)Add item to the menu.\n(4)Exit.\nEnter your choice : ")
        if a==1:
                c.show()
        elif a==2:
                o=order()
                while(1):
                        a = raw_input("\nEnter the item to be ordered:")
                        o.add(a,c)
                        b=raw_input("Do you want to order more items(yes/no)?")
                        if b=='yes':
                                continue
                        else:
                                o.show()
                                break                               
        elif a==3:
                c.add(raw_input("Enter the item to be added : "),input("Enter the price of the item : "))
        elif a==4:
                break
        else:
                print("\nInvalid choice.")

