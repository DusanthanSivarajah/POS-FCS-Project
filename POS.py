# so we have a system that needs to be in a menu which consist of:
# who are you?
# 1. Admin
# 2. Customer 
# 3. Exit program

# if admin:
# step1: order the dictionary by quantity in alphabetical order and the admin will have its own menu which consist of:
# step2: create Admin menu, - modify quantities of an item: the user should type the item name and modify its quantity, and price in the dictionary, if item does not exist, add it to the dictionary 
#                           - quantity = 0 means remove items 
#                           - display items sorted by quantity
# if customer:
# step 3: type items to purchasing items , if items doesnt exist or quantity doenst exist , show message 
# step 4: if user perchase all the quantity, then updated quantity in stock = Out stock 
# step 5: -1 on item or quantity to check out 
# step 6: email or download to local repository  


#fucntions for Admin
def addToStock(adminStock,productName):# admin adds products to the stock
  productQuantity = int(input(f"Enter the quantity added to the Stock for {productName}: "))
  productPrice = float(input(f"Enter the Price for {productName}:  "))
  if productName in adminStock and productQuantity==0:
      del adminStock[productName]
  elif productName in adminStock:
    originalQuantitiy = adminStock[productName][0]
    adminStock[productName]=[productQuantity+originalQuantitiy,productPrice]
    print(f"the Quantity of {productName} has been updated")
  else:
    adminStock[productName]=[productQuantity,productPrice]
    print(f"{productName} has been added to the stock, with Quantity of {productQuantity} and Price {productPrice}")
  return adminStock

def removeFromStock(adminStock,productName): # might not need this 
    del adminStock[productName]

def sortByProduct(adminStock): # sorts products in alphabetical order 
    adminStock = dict(sorted(adminStock.items())) 
    for items, info in adminStock.items():
        print(f"Product Name: {items}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" )
    return adminStock

def sortByQuantity(adminStock): # converts to a list then back to a dictionary and sorts Quantity by decending order 
    adminStock= dict(sorted(adminStock.items(), key=lambda x: x[1], reverse=True))
    for items, info in adminStock.items():
        print(f"Product Name: {items}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" )
    
#Functions for Costomer
def addToCart(marketStock, productName, cart): # adds item to cart and updates the stock
    itemPrice =  marketStock[productName][1]
    stockQuantity = marketStock[productName][0]
    buyQuantity = int(input(f"Enter the quantity of {productName}'s you would like to purchase: "))
    if buyQuantity > stockQuantity: # if the customer wants to buy more than the quantity in the stock available , he has a choice to buy the remaining products
        choice=input(f" Unfortunatly we dont have that much supplies for {productName}, there is only {stockQuantity}, would you like to purchase all of the remaining product?(type 'yes' to make a purchase)")
        if choice=="yes":
            cart[productName] = [stockQuantity, itemPrice]
            marketStock[productName] = [0, itemPrice]
        else:
            print("\n Thats alright, theres plenty of other items you can still buy")
    elif productName in cart:# if the product is already in the cart, only add the quantity to the cart and update the stock
        quantityInCart = cart[productName][0]
        cart[productName] = [buyQuantity+quantityInCart, itemPrice]
    else:
        cart[productName] = [buyQuantity, itemPrice]
    marketStock[productName] = [stockQuantity-buyQuantity, itemPrice]
    return cart
    
def removeFromCart(marketStock, cart):# removes products from the customer cart and sends it back to the stock
    productName = input("Which product would you like to remove from the cart? ")  
    
    ## check if issues , i think the issues is if im romoving from the cart , its not adding back to the stock
    
    if productName in cart:
        itemPrice =  cart[productName][1]
        
        quantityInCart = cart[productName][0]
        
        removeQuantity =  int(input(f"How much quantity of {productName} would you like to put back on the shelf? "))
        if removeQuantity>quantityInCart:
            returnAll=input(f"Would you like to return all {quantityInCart} of {productName}? (type yes)")# returning all qantities in the cart 
            if returnAll == "yes" and productName  not in marketStock:
                marketStock[productName] = [quantityInCart,itemPrice]
                cart[productName] = [0,itemPrice]
            else:# removing all items in the cart and adding it to the quantitiy in the stock 
                stockQuantity = marketStock[productName][0]
                marketStock[productName] = [stockQuantity+quantityInCart,itemPrice]
                cart[productName] = [0,itemPrice]
          
         
        else:
            stockQuantity = marketStock[productName][0]
            marketStock[productName] = [stockQuantity+removeQuantity,itemPrice]
            cart[productName] = [quantityInCart-removeQuantity,itemPrice]

def recipt(cart):
    totalSum=0
    for items, info in cart.items():
        print(f"\nProduct Name: {items}------ Quantity: {info[0]}------Price per item: {info[1]}------Product Sum: ${info[0]*info[1]:.2f}" )
        totalSum+= info[0]*info[1]
    print(f"\n Your total is ${totalSum:.2f} \n Thank you, come again!\n\n")

def checkQuantity(compartment): # this is to check the quantity of either stock or cart is =0 , if yes , it removes the item 
    storageCopy =  compartment.copy() # creating a copy of the dictionary beacuse we cant delete items while iterating over the orginal dictionary
    for item,info in storageCopy.items():
        if info[0]<=0:
            del compartment[item]
    for items, info in compartment.items():
        print(f"Product Name: {items}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" )
    return compartment
    
def sendEmail():
    pass
def downloadInvoice():
    pass

def adminControl(stock):
    print("Admin Contorl")
    adminSelection = None
    adminUsername = input("Enter Username:")
    adminPassword = input("Enter Password:")
    if adminUsername == "Admin" and adminPassword == "Admin123": #Dummy authentication, Acess granted to admin contorl 
    
        stock=sortByProduct(stock)  # look for a better sorting method that allows the  user to take big data.
        # print(stock)

        
        while adminSelection !=-1:
            print("\n 1.Select item to modify") # if the item exist, the admin can change the quantity or the price. 
                                        # if the item does not exit, ask the admin if he wants to add that item to the stock , if yes , append to the stock items with the quantity and price
                                        # if no , then return admin contol 
                                        # if admin says quantity 0 then delete the item from the list 
        
            print(" 2.Sort by Quantity\n 3.Press -1 to exit")
        
            adminSelection= int(input("Select your choice: "))
            if adminSelection == 1:
                product = input("Which item would you like to modify?")
                if product in stock:
                    stock = addToStock(stock,product) #modify the sock ******, if quantity = 0 remove the product from the stock
                    stock = checkQuantity(stock) 

                else:
                    addProduct= int(input("would you like to add this product to the stock?\n 1.Yes \n 2.No \n Awaiting your choice "))
                    if addProduct == 1:
                        stock= addToStock(stock,product) # append product to the stock with quantity and price
                        stock = checkQuantity(stock)
                    elif addProduct == 2:
                        pass # admin is taken back to admin selection menu 
                    else:
                        print("please select appropriate choice")# take admin back to addproduct
            elif adminSelection==2:
                sortByQuantity(stock) # sort the stock dictionary by quantity 
            else:
                print("please select the appropriate choice")# take the admin back to the admin selection menu

    else:
        print("Wrong Authenticatons, Access Denied!!")
        # go back to who_am_i

def customerPanel(stock):
    customerCart = {}
    buyProduct = None
    print("Hello dear Customer, have fun shopping")
    print ("    ---------------------Market items------------------- \n")
    checkQuantity(stock)
    while buyProduct != "-1": # or quantity not = -1  , repeatedly ask the cutomer to by products
        customerSelect= int(input("What would you like to do?\n 1. buy a product ?\n 2. remove product from cart?\n 3. Checkout\n Awaiting for your response: "))
        
        
        
        if int(customerSelect)==1:
            buyProduct= input("\nWhich product would you like to purchase dear? ")
            if buyProduct in stock:
                customerCart= addToCart(stock,buyProduct,customerCart) # append the item in customerCart and add quantity , subtract the quantitiy from the stock, 
                print ("    ---------------------Market items------------------- \n")
                stock = checkQuantity(stock)
                print ("    ---------------------Items in Cart------------------- \n")
                customerCart = checkQuantity(customerCart)
                
                    #if quantity > stock quantity , then display a message if the customer wants to buy the remaining stock ,
                    # if yes , set the customer quantity to the remaining quantity in the stock then remove the item from the stock
                    # if no then send the customer back to buyProduct   
            else:
                print("This product does not exit , please check the stock to see all available products") #send the cutomer back to buyProdcuts 
        elif int(customerSelect)==2:
            removeFromCart(stock,customerCart)
            print ("    ---------------------Market items------------------- \n")
            stock = checkQuantity(stock)
    
            print ("    ---------------------Items in Cart------------------- \n")
            customerCart= checkQuantity(customerCart)
        elif int(customerSelect)==3:
            invoice= int(input("Would you like a invoice?\n 1. by email\n 2. Download invoice\n 3. No\n Select your choice "))# create a message that showes the order details and total price 
            if invoice == 1:
                pass # import smtp to send email by gmail
            elif invoice==2:
                pass # save invoice as a txt document in local repository, give directory location. 
            else:
                break
        

    print(f"Here is your recipt\n")
    recipt(customerCart)
            
def mainMenu(stock):
    checkQuantity(stock)
    whoAmI = None
    while whoAmI !=3:
        whoAmI = int(input("Hello and Welcome! Who are you?(1,2,3)\n 1.Admin \n 2.Customer \n 3.Exit Program \n Awaiting for your Response: "))
        if whoAmI==1: #Admin Control 
            adminControl(stock)

        elif whoAmI==2:#Customer 
            customerPanel(stock)

        elif whoAmI==3:
            print("Exiting program") # create a 5 second timer to close the application 
    
    print("Program stopped")




#Start system menu:
stock = {"Apples":[100,1.3],
         "books":[10,4.3],
         "lights":[18,10.50],
         "chocolates":[122,1.3],
         "rat":[50,270],
         "apples":[100,1.3], 
         "Bananas":[737,2.30],
         "bbq":[15,2.13] }

mainMenu(stock)


