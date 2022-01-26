
class Order :
    def __init__(self,cup,flavor,topping) :
        self.cup = cup
        self.flavor = flavor
        self.topping = topping
        self.count = 0
        self.price = 0
        
    
    def getIcecream(self):
        print("Yor order Ice-cream Size : " + self.cup)
        print("flavor : " + str(self.flavor))
        print("topping : " + str(self.topping))

    def SetCalculateOrder(self):
        if self.cup == 'S':
            self.price += 15
        elif self.cup == 'M':
            self.price += 25
        elif self.cup == 'L':
            self.price += 45

        for i in range(0,len(self.topping)):
            self.count += 1
        self.count *= 5
        self.price += self.count

        return self.price 
    
    def SetShowPrice(self):
        print("Your ice-cream's price is  " + str(self.price)+" Baht")
       

class Customer :
    def __init__(self,crash) :
        self.crash = crash

    def SetOrder(self,size,flavor,topping):
        O = Order(size,flavor,topping)
        return O 

    def Payment(self,price):
        Return = self.crash - price
        print("Return : "+ str(Return) + " Baht")

class Officer :
    

    def GetOrder(self,order):
        print(order.getIcecream())

    def CalculateOrder(self,order):
        price = order.SetCalculateOrder()
        return price

    def ShowPrice(self,order):
        order.SetShowPrice()

        

Customer1 = Customer(100) # you have 100 baht
Officer1 = Officer()
Customer2 = Customer(200) # you have 200 baht
Officer2 = Officer()



order1 = Customer1.SetOrder('S',['Vanila'],['Cookie','Jelly','Stickyrice'])
Officer1.GetOrder(order1)
total1 = Officer1.CalculateOrder(order1)
Officer1.ShowPrice(order1)
Customer1.Payment(total1)
print("\n")

order2 = Customer2.SetOrder('M',['Vanila','Chocolate'],['Jelly','Pumpkin'])
Officer2.GetOrder(order2)
total2 = Officer2.CalculateOrder(order2)
Officer2.ShowPrice(order2)
Customer2.Payment(total2)

