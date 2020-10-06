class store:
    __itemcode=[]
    __price=[]
    def getd(self):
        for i in range (5):
            self.__itemcode.append(int(input("\n Enter the item code : ")))
            self.__price.append(float(input("\n Enter price : ")))

    def display(self):
         print("\n Item code \t\t\t price")
         for i in range(5):
             print(self.__itemcode[i],"\t\t\t\t",self.__price[i])

    def bill(self,quantity):
         t=0
        
         print("\n ----------------------------------------------Bill---------------------------------------------------------")
         print("\n********************************************************************")   
         print("Itemcode\t\t Quantity \t\t price\item \t sub total " )    
         for i in range (5):
             print(self.__itemcode[i],"\t\t",quantity[i],"\t\t",self.__price[i],"\t\t",self.__price[i]*quantity[i])
         print("\n********************************************************************")
         for i in range(5):
             t=t+self.__price[i]*quantity[i]
         print("\n Total : \t\t\t\t\t\t",t)

         
s=store()
s.getd()
s.display()
q=[]
for i in range(5):
    print("\n Enter the quantity of item code ",s._store__itemcode[i])
    q.append(int(input()))         
s.bill(q)
