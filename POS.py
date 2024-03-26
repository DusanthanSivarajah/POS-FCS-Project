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



#Start system menu:
stock = {"Apples":[100,1.3],
         "books":[10,4.3],
         "lights":[18,10.50],
         "chocolates":[122,1.3],
         "pigs":[50,270],
         "apples":[100,1.3], 
         "Bananas":[737,2.30],
         "bbq":[15,2.13] }
print(stock)

who_Am_I = int(input("Hello and Welcome! Who are you?(1,2,3)\n 1.Admin \n 2.Customer \n 3.Exit Program \n Awating for your Response: "))
if who_Am_I==1: #Admin Control 
    print("Admin Contorl")
    adminSelection = None
    adminUsername = input("Enter Username:")
    adminPassword = input("Enter Password:")
    if adminUsername == "Admin" and adminPassword == "Admin123": #Acess granted to admin contorl 
    
        stock= dict(sorted(stock.items()))  # look for a better sorting method that allows the  user to take big data.
        print(stock)
        print("1.Select item to modify") # if the item exist, the admin can change the quantity or the price. 
                                        # if the item does not exit, ask the admin if he wants to add that item to the stock , if yes , append to the stock items with the quantity and price
                                        # if no , then return admin contol 
                                        # if admin says quantity 0 then delete the item from the list 
        
        print("2.Sort by Quantity")
        
        
        
        adminSelection= input("select your choice")
        if adminSelection == 1:
            product = input("Which item would you like to modify?")
            if product in stock:
                pass #modify the sock ******, if quantity = 0 remove the product from the stock 
            else:
                addProduct= input("would you like to add this product to the stock?\n 1.Yes \n 2.No \n Awaiting your choice ")
                if addProduct == 1:
                    pass # append product to the stock with quantity and price
                elif addProduct == 2:
                    pass # admin is taken back to admin selection menu 
                else:
                    print("please select appropriate choice")# take admin back to addproduct
        elif adminSelection==2:
            pass # sort the stock dictionary by quantity 
        else:
            print("please select the appropriate choice")# take the admin back to the admin selection menu

    else:
        print("Wrong Authenticatons, Access Denied!!")
        # go back to who_am_i





elif who_Am_I==2:#Customer 
    customerCart = []
    print("Hello dear Customer, have fun shopping")
    while buyProduct != -1: # or quantity not = -1  , repeatedly ask the cutomer to by products
        print(stock)
        buyProduct= input("Which product would you like to purchase dear?")
        if buyProduct in stock:
            pass # append the item in customerCart and add quantity , subtract the quantitiy from the stock, 
                 #if quantity > stock quantity , then display a message if the customer wants to buy the remaining stock ,
                 # if yes , set the customer quantity to the remaining quantity in the stock then remove the item from the stock
                 # if no then send the customer back to buyProduct   
        else:
            print("this product does not exit , please check the stock to see all available products") #send the cutomer back to buyProdcuts 

    print(customerCart)
    invoice= int(input("would you like a invoice?\n 1. by email\n 2. Download invoice"))# create a message that showes the order details and total price 
    if invoice == 1:
        pass # import smtp to send email by gmail
    elif invoice==2:
        pass # save invoice as a txt document in local repository, give directory location. 






elif who_Am_I==3:
    print("Exiting program") # create a 5 second timer to close the application 
  
else:
    print("Invalid Input, please select the appropriate choice") # send the user back to the main application 




