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
    try:
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
    except ValueError:
        print("\nPlease enter a NUMBER\n")
    
    return adminStock
    

def sortByProduct(adminStock): # sorts products usiing merge sort alphabetical order
    def mergeSort(list1,start,end):
        if start==end:
            return
        mid=(start+end)//2
        mergeSort(list1,start,mid)
        mergeSort(list1,mid+1,end)
        merge(list1,start,end)
        return list1
    def merge(list1,start,end):
        mid=(start +end) //2
        bigList=[]
        ind1 =  start
        ind2 = mid+1

        while ind1 <= mid and ind2 <=end:
            if list1[ind1]<list1[ind2]:
                bigList.append(list1[ind1])
                ind1+=1
            else:
                bigList.append(list1[ind2])
                ind2+=1
        while ind1 <= mid:
            bigList.append(list1[ind1])
            ind1+=1
        while ind2 <= end:
            bigList.append(list1[ind2])
            ind2+=1
        
        list1[start:end+1]=bigList


    sortingStock = list(adminStock)# puts all the keys in a list 

    mergeSort(sortingStock,0,len(sortingStock)-1)
    for word in sortingStock:  #moves all the Uppercase to the end of the list.
        if word[0] != word[0].lower():
            poppedElement=sortingStock.pop(0)
            sortingStock.append(poppedElement)


    tempSortedStock={}

    for key in sortingStock:
        tempSortedStock[key] = adminStock[key] # puts the values from stock for each key

    adminStock = tempSortedStock
  
    for items, info in adminStock.items():
        print(f"Product Name: {items}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" )
    return adminStock

def sortByQuantity(adminStock): # Using selection sort to sort the quantity in descending order 
    def selectionSort(list1):
        for border in range(0, len(list1)-1):
            minIndex = border
            for i in range(border+1,len(list1)):
                if list1[i][1]>list1[minIndex][1]:
                    minIndex=i
            list1[border],list1[minIndex] = list1[minIndex],list1[border]
        return list1
    stockAsList = []
    for key, values in adminStock.items(): #puts the key and values as a list in the list stockAsList
        stockElement = [key]+list(values)
        stockAsList.append(stockElement)
    selectionSort(stockAsList)

   

    for element in stockAsList:
        print(f"Product Name: {element[0]}        Quantity: {element[1]}        Price per item: ${element[2]:.2f}" )
        
            
    
#Functions for Costomer
def addToCart(marketStock, productName, cart): # adds item to cart and updates the stock
    try:
        itemPrice =  marketStock[productName][1]
        stockQuantity = marketStock[productName][0]
        buyQuantity = abs(int(input(f"Enter the quantity of {productName}'s you would like to purchase: ")))
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
    except ValueError:
        print("Please Enter a NUMBER for the Quantity")
    return cart
    
def removeFromCart(marketStock, cart):# removes products from the customer cart and sends it back to the stock
    try:
        productName = input("Which product would you like to remove from the cart? ")  
        
        ## check if issues , i think the issues is if im romoving from the cart , its not adding back to the stock
        
        if productName in cart:
            itemPrice =  cart[productName][1]
            
            quantityInCart = cart[productName][0]
            
            removeQuantity =  abs(int(input(f"How much quantity of {productName} would you like to put back on the shelf? ")))
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
        else: 
            print("this Product is not in your Cart")
    except ValueError:
        print("Please Enter NUMBERS for Quantity")

def receipt(cart):
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
    
def sendEmail(cart):
    import smtplib # the module needed to send a email
    import os # the module needed to delete a file 
    fileEmail = open("myEmailReceipt.txt","w")
    totalSum=0
    fileEmail.write("-------------------------------------- YOUR RECEIPT -------------------------------------------")
    for items, info in cart.items():
        fileEmail.write(f"\nProduct Name: {items}------ Quantity: {info[0]}------Price per item: {info[1]}------Product Sum: ${info[0]*info[1]:.2f}" )
        totalSum+= info[0]*info[1]
    fileEmail.write(f"\n Your total is ${totalSum:.2f} \n Thank you, come again!\n\n")
    fileEmail.close()

    fileMessage= open("myEmailReciept.txt","r")
    emailMessage=fileMessage.read()
    fileMessage.close()
    

    email = "@gmail.com" #enter your email
    receiverEmail = input("Enter your Email: ")
    subject = "Receipt"
    text = f'Subject: {subject}\n\n{emailMessage}'
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,"")#enter password from google 2fa 
    server.sendmail(email, receiverEmail ,text)
    os.remove("myEmailReceipt.txt")
    print("Email Sent!")

    
def downloadInvoice(cart):
    file = open("myReceipt.txt","w")
    totalSum=0
    file.write("-------------------------------------- YOUR RECEIPT -------------------------------------------")
    for items, info in cart.items():
        file.write(f"\nProduct Name: {items}------ Quantity: {info[0]}------Price per item: {info[1]}------Product Sum: ${info[0]*info[1]:.2f}" )
        totalSum+= info[0]*info[1]
    file.write(f"\n Your total is ${totalSum:.2f} \n Thank you, come again!\n\n")
    file.close()

def adminControl(stock):
    print("Admin Control")
    adminSelection = None
    adminUsername = input("Enter Username:")
    adminPassword = input("Enter Password:")
    if adminUsername == "Admin" and adminPassword == "Admin123": #Dummy authentication, Acess granted to admin contorl 
    
        stock=sortByProduct(stock)  # look for a better sorting method that allows the  user to take big data.
        # print(stock)

        
        while adminSelection != "-1":
            print("\n 1.Select item to modify") # if the item exist, the admin can change the quantity or the price. 
                                        # if the item does not exit, ask the admin if he wants to add that item to the stock , if yes , append to the stock items with the quantity and price
                                        # if no , then return admin contol 
                                        # if admin says quantity 0 then delete the item from the list 
        
            print(" 2.Sort by Quantity\n -1.Logout")
        
            adminSelection= (input("Select your choice: "))
            if adminSelection == "1":
                product = input("Which item would you like to modify?")
                if product in stock:
                    stock = addToStock(stock,product) #modify the sock ******, if quantity = 0 remove the product from the stock
                    stock = checkQuantity(stock) 

                else:
                    addProduct= (input("would you like to add this product to the stock?\n 1.Yes \n 2.No \n Awaiting your choice "))
                    if addProduct == "1":
                        stock= addToStock(stock,product) # append product to the stock with quantity and price
                        stock = checkQuantity(stock)
                    elif addProduct == "2":
                        continue # admin is taken back to admin selection menu 
                    else:
                        print("please select appropriate choice")# take admin back to addproduct
            elif adminSelection=="2":
                sortByQuantity(stock) # sort the stock dictionary by quantity 
            else:
                print("please select the appropriate choice")# take the admin back to the admin selection menu

    else:
        print("Wrong Authenticatons, Access Denied!!")
        # go back to who_am_i
    return(stock)    

def customerPanel(stock):
    customerCart = {}
    buyProduct = None
    print("Hello dear Customer, have fun shopping")
    print ("    ---------------------Market items------------------- \n")
    stock=checkQuantity(stock)
    while buyProduct != "-1": # or quantity not = -1  , repeatedly ask the cutomer to by products
        customerSelect= input("What would you like to do?\n 1. buy a product ?\n 2. remove product from cart?\n 3. Checkout\n Awaiting for your response: ")
        
        
        
        if  customerSelect =="1":
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
        elif customerSelect =="2":
            removeFromCart(stock,customerCart)
            print ("    ---------------------Market items------------------- \n")
            stock = checkQuantity(stock)
    
            print ("    ---------------------Items in Cart------------------- \n")
            customerCart= checkQuantity(customerCart)
        elif customerSelect=="3":
            true=True
            while true:
                invoice= (input("How would you like your receipt?\n 1. By Email\n 2. Download invoice\n 3. Regular\n Select your choice "))# create a message that showes the order details and total price 
                if invoice == "1":
                    sendEmail(customerCart) # import smtp to send email by gmail
                    true = False
                    break
                elif invoice=="2":
                    downloadInvoice(customerCart)
                    print("Invoice Saved!")# save invoice as a txt document in local repository, give directory location. 
                    true = False
                    break
                elif invoice =="3":
                    print(f"Here is your receipt\n")
                    receipt(customerCart)
                    true=False
                    break
                
                else:
                    print("please input 1-3")
        else:
            print("please input 1-3")
    return(stock)
    
            
def mainMenu(stock):
    print(" \n\n----------------------THE PET STORE-----------------------\n")
    checkQuantity(stock)
    whoAmI = None
    while True:
        whoAmI = input("\n\nHello and Welcome! Who are you?(1,2,3)\n 1.Admin \n 2.Customer \n 3.Exit Program \n Awaiting for your Response: ")
        if whoAmI=="1": #Admin Control 
            stock=adminControl(stock)

        elif whoAmI=="2":#Customer 
            customerPanel(stock)

        elif whoAmI=="3":
            print("Exiting program") # create a 5 second timer to close the application 
            break
        else:
            print("Please input a number 1-3")
    print("Program stopped")
    return(stock)



#Start system menu:
stock = {"Dog":[100,1.3],
         "Cat":[10,4.3],
         "hamsters":[18,10.50],
         "bIrDs":[122,1.3],
         "hOrse":[50,270],
         "Frog":[100,1.3], 
         "Rabbit":[737,2.30],
         "fish":[15,2.13] }



mainMenu(stock)



