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

class order:
        def __init__(self):
                self.Ord={}
        def add(self,x,y):
                self.Ord[x] = y
        def show(self):
                print '\nOrdered items:'
                for key,value in self.Ord.items():
                        print("{0} - Rs.{1}".format(key,value))
class keyerror(Exception):
        pass
                        
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
                        try:
                                if a in c.Menu:
                                        o.add(a,c.Menu[a])
                                        b=raw_input("Do you want to order more items(yes/no)?")
                                        if b=='yes':
                                                continue
                                        else:
                                                o.show()
                                                break
                                else:
                                        raise keyerror

                        except keyerror:
                                print 'Item is not in menu.order another item.'
                                
        elif a==3:
                c.add(raw_input("Enter the item to be added : "),input("Enter the price of the item : "))
        elif a==4:
                break
        else:
                print("\nInvalid choice.")

