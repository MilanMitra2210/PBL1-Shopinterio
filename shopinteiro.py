class Product:

    """*****for storing product*****"""

    def __init__(self , name , price):
      self.name = name
      self.price = price

class ProductStock:

    """*****for storing ProductStock*****"""

    def __init__(self , product , quantity):
      self.product = product
      self.quantity = quantity

class Shop:

    """*****for storing Shop details*****"""

    stock = []

    @classmethod
    def changeStock(cls , newStock):
        cls.stock.append(newStock)


class Customer:

    """*****for storing Customer Details*****"""

    shoppingList = []
    def __init__(self , name , budget):
        self.name = name
        self.budget = budget

    @classmethod
    def changeShoppingList(cls , item):
        cls.shoppingList.append(item)

def printProduct(p):

    """*****Function to print product name and price*****"""

    print("-------------\n")
    print("PRODUCT NAME:", p.name ," \nPRODUCT PRICE: \u20B9" , p.price ,"\n")

def printCustomer(c):

    """*****Function to print whole details of customer i.e. name , budget , shopping List and its details*****"""

    print("CUSTOMER NAME:" , c.name ,"\nCUSTOMER BUDGET: \u20B9" ,c.budget ,"\n")
    # print("-------------\n")
    for item in c.shoppingList:
        printProduct(item.product)
        print(c.name ,"ORDERS", item.quantity ,"OF MENTIONED PRODUCT\n")
        cost = item.quantity * item.product.price
        print("The cost to " , c.name ," will be \u20B9" ,cost ,"\n")

def createAndStockShop():

    """*****for retrieving data from stock.csv FILE and use it accordingly.*****"""
    shop = Shop()
    fp = open("stock.csv","r") #*****FILE pointer which is opening the file stock.csv as in read mode*****
    
    if(fp == None):
        exit()     #*****if file is empty ...*exit****

    first = fp.readline()
    split_line = first.split(",")
    cash = float(split_line[0])
    shop.cash = cash

    for line in fp:
        split_line = line.split(",")   #*****spliting the line by ","*****
        name = split_line[0]
        
        if(split_line[1] != ''):
            price = float(split_line[1])    #*****converting to float*****
        else:
            price = 0.0

        if(split_line[2] != ''):
            quantity = int(split_line[2])   #*****converting to float*****
        else:
            quantity = 0
        
        #*****Now creating a new product and adding it to ProductStock as well as including it inm shop*****#

        product = Product(name , price)

        stockItem = ProductStock(product , quantity)

        shop.changeStock(stockItem)
        

        # print("NAME OF PRODUCT ",name, " PRICE ",price, " QUANTITY ", quantity, "\n")

    fp.close()       #closing file
    return shop

def printShop(s):

    """******Function to print the details of shop i.e. cash , product stock and product details as well as quantity of each*****"""
    print("------------------------\n")
    print("Shop has \u20B9" ,s.cash ," in cash\n")
    for item in s.stock:
        printProduct(item.product)
        print("The Shop has ",item.quantity , " of the mentioned\n")

def checkStock(name , s):
    for i in range(len(s.stock)):
        if(s.stock[i].product.name == name):
            return i
    return -1

def initiateShopping(customer , shop):
    index = 0
    totalCost = 0.0

    fp = open(customer,"r")

    if(fp == None):
        exit()     #*****if file is empty ...*exit****

    first = fp.readline()
    split_line = first.split(",")
    name = split_line[0]
    budget = float(split_line[1])

    c = Customer(name , budget)

    for line in fp:
        split_line = line.split(",")   #*****spliting the line by ","*****
        pName = split_line[0] 
        if(split_line[1] != ''):
            quantity = int(split_line[1])    #*****converting to float*****
        else:
            quantity = 0

        index = checkStock(pName,shop)


        if(index != -1):
            if(shop.stock[index].quantity > quantity):
                cStock = ProductStock(shop.stock[index].product , quantity)
                c.changeShoppingList(cStock)
                shop.stock[index].quantity -= quantity
                cost = quantity * shop.stock[index].product.price
                totalCost += cost
            else:
                print("-------------\n")
                print("We have only",shop.stock[index].quantity , pName)
        else:
            print("-------------\n")
            print(pName," not available\n")
    printCustomer(c)
    shop.cash += totalCost

    return shop

def operatorOnline(shop):
    val = 0
    totalCost = 0

    name = input("Enter Your Name: ")
    
    c = Customer(name , 0)

    while(val < 256):
        pName = input("Enter name of Product: ")

        index = checkStock(pName , shop)
        if(index != -1):
            quantity = int(input("Enter quantity of Product: "))
            if(shop.stock[index].quantity > quantity):
                cStock = ProductStock(shop.stock[index].product , quantity)
                c.changeShoppingList(cStock)
                shop.stock[index].quantity -= quantity
                cost = quantity * shop.stock[index].product.price
                totalCost += cost

            else:
                print("-------------\n")
                print("We have only",shop.stock[index].quantity , pName)
        else:
            print(pName," not available\n")
        val = int(input("If you want to add more product enter 0 else 1--->"))
        if(val == 1):
            break

    print("-------------\n")
    printCustomer(c)
    print(name ," pay the total Amount of \u20B9",totalCost)
    shop.cash += totalCost
    return shop











#****Here  calling of function and real programming take place****#

# coke = Product("Can Coke",1.62)
# bread = Product("Bread",0.7)
# printProduct(coke)

# cokeStock = ProductStock(coke,20)
# breadStock = ProductStock(bread,2)

# dominic = Customer("Dominic",100)

# dominic.changeShoppingList(cokeStock)
# dominic.changeShoppingList(breadStock)


# printCustomer(dominic)


shop = createAndStockShop()
# printShop(shop)

shop = initiateShopping("customer.csv",shop)
printShop(shop)

# shop = operatorOnline(shop)
# printShop(shop)


# print("The shop has " , cokeStock.quantity ," of the product" , cokeStock.product.name)

