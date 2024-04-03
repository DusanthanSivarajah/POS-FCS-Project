from tkinter import *
import ttkbootstrap as tb


root =  tb.Window(themename = "superhero") 
root.title("Point of Service")
root.geometry('1400x900')
root.resizable(False,False)

def updateWindow():
    # Clear the current content of the window
    for widget in root.winfo_children():
        widget.destroy()
def exitWindow(): #exits the program 
    root.destroy()



def checkout(cart):

    def sendEmail():
        pass
    def download():
        pass
    def leave():
        mainLayout(stock)



    updateWindow()
    checkoutLabel =  tb.Label(text="How would you like your receipt?",
                            font=("Helvetica",28),
                            bootstyle = "default")
    checkoutLabel.pack(pady=(50,0))# creates and moves the label down the y-axis by 50


    emailButton = tb.Button(text="Receipt by Email", bootstyle = "primary", command=sendEmail)
    emailButton.pack(pady=30, padx= (370,200) , side="left")# moves the button west and row is the x-axis and column is the Y-axis

    downloadButton = tb.Button(text="Download Receipt", bootstyle = "primary", command= download)
    downloadButton.pack(pady=30, padx=(0,200) ,side="left")# moves the button west and row is the x-axis and column is the Y-axis

    leaveButton = tb.Button(text="Leave", bootstyle = "primary", command= leave)
    leaveButton.pack( pady=0, padx=0 ,side="left")# moves the button west and row is the x-axis and column is the Y-axis
 


def adminAuthLayout():
    def login():
        
        username = adminUsernameEntry.get()
        password = adminPasswordEntry.get()

        if username == "Admin" and password == "Admin123":
            adminLayout(stock)
        else:
            adminUsernameEntry.delete(0, tb.END)  # Clear the contents of the username Entry
            adminPasswordEntry.delete(0, tb.END)  # Clear the contents of the password Entry
            loginButton.configure(command=login)       
        infoLabel.configure(text="Access Denied")
    
    
    
    updateWindow()


    adminAuthLabel = tb.Label(text="Admin Authentication", font=("Helvetica",28), bootstyle="default" )
    adminAuthLabel.place(x=500,y=150)

    usernameLabel = tb.Label(text="Enter Username", font=("Helvetica"), bootstyle="success" )
    usernameLabel.place(x=550,y=307)

    adminUsernameEntry = tb.Entry()
    adminUsernameEntry.place(x=700,y=300)

    passwordLabel = tb.Label(text="Enter Password", font=("Helvetica"), bootstyle="success" )
    passwordLabel.place(x=550,y=357)

    adminPasswordEntry = tb.Entry(show="*")
    adminPasswordEntry.place(x=700,y=350)

    goBackButton = tb.Button(text="<<Back", bootstyle = "primary", command=lambda:mainLayout(stock))
    goBackButton.place( x = 600, y = 450)

    infoLabel = tb.Label(text="", bootstyle= "Success" )
    infoLabel.place(x=150, y=600)
    
    loginButton = tb.Button(text="Login", bootstyle = "success", command=login)
    loginButton.place( x = 750, y=450)



def adminLayout(stock):
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

        
    def sortByQuantity(): # converts to a list then back to a dictionary and sorts Quantity by decending order 
        stocks= dict(sorted(stock.items(), key=lambda x: x[1][0], reverse=True))
        stockData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in stocks.items()])
        stockLabel.config(text=stockData)
        infoLabel.config(text="The Stock has been sorted by Quantity", bootstyle= "success")
        return


    def addToStock():# admin adds products to the stock
        productName = productNameEntry.get()
        productQuantity = productQuantityEntry.get()
        productPrice = ProductPriceEntry.get()

        def adminYes():
            stock[productName]=[productQuantity,productPrice]
            infoLabel.config(text=f"{productName} has been added to the stock, with Quantity of {productQuantity} and Price ${productPrice:.2f}")
            stockData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in stock.items()])
            stockLabel.config(text=stockData)
            productNameEntry.delete(0, tb.END)  
            productQuantityEntry.delete(0, tb.END)
            ProductPriceEntry.delete(0,tb.END)
            yesButton.place_forget()
            noButton.place_forget()
        def adminNo():
            stockData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in stock.items()])
            stockLabel.config(text=stockData)
            infoLabel.config(text="")
            productNameEntry.delete(0, tb.END)  
            productQuantityEntry.delete(0, tb.END)
            ProductPriceEntry.delete(0,tb.END)
            yesButton.place_forget()
            noButton.place_forget()

          
        if productName==  "" or productQuantity=="" or productPrice=="":
            infoLabel.config(text="Please fill all the required fields to add or modify", bootstyle = "danger")
        else:
            try:
                productQuantity = int(productQuantity)
            except ValueError:
                infoLabel.config(text="Please enter a integer in 'Product Quantity' ", bootstyle = "danger")
                return 
        
            try: 
                productPrice = int(productPrice)
                infoLabel.config(text="entry success")
            except ValueError:
                infoLabel.config(text="Please enter a integer or float number in 'Product Price'", bootstyle = "danger")
                try:
                    productPrice = float(productPrice)
                    infoLabel.config(text="entry success")
                except:
                    infoLabel.config(text="Please enter a integer or float number in 'Product Price'", bootstyle = "danger")
                    return 



            if productName in stock and productQuantity==0:
                del stock[productName]
                infoLabel.config(text=f"{productName} has been removed", bootstyle="warning")
            elif productName in stock:
                originalQuantitiy = stock[productName][0]
                stock[productName]=[productQuantity+originalQuantitiy,productPrice]
                infoLabel.config(text=f"the Quantity of {productName} has been updated",bootstyle="success")
            else:
                infoLabel.config(text= f"The product {productName} does not exist in the stock, would you like to add it?",bootstyle="warning")
                yesButton = tb.Button(text="Yes", bootstyle = "success", command=adminYes)
                yesButton.place( x = 200, y = 695)

                noButton = tb.Button(text="Cancel", bootstyle = "default",command=adminNo )
                noButton.place( x = 250, y = 695)

            stockData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in stock.items()])
            stockLabel.config(text=stockData)
            productNameEntry.delete(0, tb.END)  
            productQuantityEntry.delete(0, tb.END)
            ProductPriceEntry.delete(0,tb.END)
            return stock
        



    updateWindow()
    stock = sortByProduct(stock)
    stockData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in stock.items()])


    adminControlLabel = tb.Label(root,text="Admin Control", font=("Helvetica",28), bootstyle="default" )
    adminControlLabel.place(x=570,y=50)



    productNameLabel = tb.Label(root, text="Product Name", font=("Helvetica"), bootstyle="success" )
    productNameLabel.place(x=150,y=307)

    productNameEntry = tb.Entry()
    productNameEntry.place(x=300,y=300)
    


    productQuantityLabel = tb.Label(root, text="Product Quantity", font=("Helvetica"), bootstyle="success" )
    productQuantityLabel.place(x=150,y=357)

    productQuantityEntry = tb.Entry()
    productQuantityEntry.place(x=300,y=350)
    

    ProductPriceLabel = tb.Label(root, text="Product Price", font=("Helvetica"), bootstyle="success" )
    ProductPriceLabel.place(x=150,y=407)

    ProductPriceEntry = tb.Entry()
    ProductPriceEntry.place(x=300,y=400)



    addToStockButton = tb.Button(root, text="Add/Update Item", bootstyle = "success",command=addToStock )
    addToStockButton.place( x = 300, y = 450)

    quantitySortButton = tb.Button(root, text="Sort by Quantity", bootstyle = "success", command=sortByQuantity)
    quantitySortButton.place( x = 300, y=500)

    stockTitleLabel = tb.Label(root,text="Stock Items", font=("Helvetica",20), bootstyle="default" )
    stockTitleLabel.place(x=750,y=235)

    stockLabel = tb.Label(text= stockData ,bootstyle= "default" )
    stockLabel.place(x=750, y=280)

    infoLabel = tb.Label(text="Hello Admin, what would you like to do?",font=("Helvetica",15), bootstyle= "success" )
    infoLabel.place(x=150, y=600)



    logoutButton = tb.Button(text="Logout", bootstyle = "danger", command=lambda: mainLayout(stock))
    logoutButton.place( x = 1200, y = 63)

    return stock


def customerLayout(stock):
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


    def addToCart(): # adds item to cart and updates the stock
        
        marketStock = stock
        productName =  cartProductNameEntry.get()
        buyQuantity = cartProductQuantityEntry.get()

        def customerYes():
            cart[productName] = [stockQuantity, itemPrice]
            del marketStock[productName]
            infoLabel.config(text=f"{productName} has been added to the cart, with Quantity of {stockQuantity}")
            cartData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in cart.items()])
            cartLabel.config(text=cartData)
            stocks = sortByProduct(stock)
            stockData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in stocks.items()])
            stockCartLabel.config(text=stockData)
            cartProductNameEntry.delete(0, tb.END)  
            cartProductQuantityEntry.delete(0, tb.END)
            yesButton.place_forget()
            noButton.place_forget()
        def customerNo():
            
            
            infoLabel.config(text="Thats alright, theres plenty of other items you can still buy")
            cartProductNameEntry.delete(0, tb.END) 
            cartProductQuantityEntry.delete(0, tb.END)
           
            yesButton.place_forget()
            noButton.place_forget()





        if productName==  "" or buyQuantity=="" :
            infoLabel.config(text="Please fill all the required fields to add or modify", bootstyle = "danger")
        else:
            try:
                buyQuantity = abs(int(buyQuantity))
            except ValueError:
                infoLabel.config(text="Please enter a integer in 'Product Quantity' ", bootstyle = "danger")
                return 
            if productName not in stock:
                infoLabel.config(text= f"{productName} is not in stock try looking for something else")
            else:
      

                itemPrice =  marketStock[productName][1]
                stockQuantity = marketStock[productName][0]
            
                if buyQuantity > stockQuantity: # if the customer wants to buy more than the quantity in the stock available , he has a choice to buy the remaining products
                    infoLabel.config(text=f" Unfortunatly we dont have that much supplies for {productName}, there is only {stockQuantity}, would you like to purchase all of the remaining product?")
                    
                    yesButton = tb.Button(text="Yes", bootstyle = "success", command=customerYes)
                    yesButton.place( x = 50, y = 240)


                    noButton = tb.Button(text="Cancel", bootstyle = "default", command=customerNo )
                    noButton.place( x = 110, y = 240)


                elif productName in cart:# if the product is already in the cart, only add the quantity to the cart and update the stock ###
                    quantityInCart = cart[productName][0]
                    cart[productName] = [buyQuantity+quantityInCart, itemPrice]
                    cartData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in cart.items()])
                    cartLabel.config(text=cartData)
                
                
                    stocks = sortByProduct(stock)
                    stockData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in stocks.items()])
                    stockCartLabel.config(text=stockData)
                else:
                    cart[productName] = [buyQuantity, itemPrice]
                marketStock[productName] = [stockQuantity-buyQuantity, itemPrice]
                cartData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in cart.items()])
                cartLabel.config(text=cartData)
                if marketStock[productName][0] == 0:
                    del marketStock[productName]
            stocks = sortByProduct(stock)
            stockData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in stocks.items()])
            stockCartLabel.config(text=stockData)
            cartProductNameEntry.delete(0, tb.END)  
            cartProductQuantityEntry.delete(0, tb.END)
        return cart 


    
    def removeFromCart():# removes products from the customer cart and sends it back to the stock
        marketStock = stock
        productName =  cartProductNameEntry.get()
        removeQuantity = cartProductQuantityEntry.get()

        def customerYes():
            
            if productName  not in marketStock:
                marketStock[productName] = [quantityInCart,itemPrice]
                del cart[productName]
                
            else:# removing all items in the cart and adding it to the quantitiy in the stock 
                stockQuantity = marketStock[productName][0]
                marketStock[productName] = [stockQuantity+quantityInCart,itemPrice]
                del cart[productName]
                

            infoLabel.config(text=f"{productName} has been Removed to the cart and returned to the stock")
            cartData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in cart.items()])
            cartLabel.config(text=cartData)
            stocks = sortByProduct(stock)
            stockData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in stocks.items()])
            stockCartLabel.config(text=stockData)
            cartProductNameEntry.delete(0, tb.END)  
            cartProductQuantityEntry.delete(0, tb.END)
            yesButton.place_forget()
            noButton.place_forget()


        def customerNo():
            
            
            infoLabel.config(text="you chose not to remove")
            cartProductNameEntry.delete(0, tb.END) 
            cartProductQuantityEntry.delete(0, tb.END)
           
            yesButton.place_forget()
            noButton.place_forget()






        if productName==  "" or removeQuantity=="" :
            infoLabel.config(text="Please fill all the required fields to add or modify", bootstyle = "danger")
        else:
            try:
                removeQuantity = abs(int(removeQuantity))
            except ValueError:
                infoLabel.config(text="Please enter a integer in 'Product Quantity' ", bootstyle = "danger")
                return 
            if productName not in cart:
                infoLabel.config(text= f"{productName} is not in stock try looking for something else")
            else:
                 
                if productName in cart:
                    itemPrice =  cart[productName][1]
                    
                    quantityInCart = cart[productName][0]
                    
                    if removeQuantity>quantityInCart:
                        infoLabel.config(text=f"Would you like to return all {quantityInCart} of {productName}? (type yes)")# returning all qantities in the cart 
                        yesButton = tb.Button(text="Yes", bootstyle = "success", command=customerYes)
                        yesButton.place( x = 50, y = 240)

                        noButton = tb.Button(text="Cancel", bootstyle = "default", command=customerNo )
                        noButton.place( x = 110, y = 240)
                    
                    else:                     
                        # stockQuantity = marketStock[productName][0]
                        # marketStock[productName] = [stockQuantity+removeQuantity,itemPrice]
                        # cart[productName] = [quantityInCart-removeQuantity,itemPrice]
                        # Get the initial quantities from the cart
                        if productName in cart:
                            quantityInCart = cart[productName][0]
                        else:
                            # If the product is not in the cart, set the quantity to 0
                            quantityInCart = 0

                        # Get the initial stock quantity
                        if productName in marketStock:
                            stockQuantity = marketStock[productName][0]
                            
                        else:
                            # If the product is not in the stock, set the quantity to 0
                            stockQuantity = 0

                        # Update stock and cart quantities
                        marketStock[productName] = [stockQuantity + removeQuantity, itemPrice]
                        cart[productName] = [quantityInCart - removeQuantity, itemPrice]
                        infoLabel.config(text=f"{productName} as been returned")
                    
                    if cart[productName][0]==0:
                        del cart[productName]
                else: 
                    infoLabel.config(text="this Product is not in your Cart")
                
            
        cartData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in cart.items()])
        cartLabel.config(text=cartData)
        stocks = sortByProduct(stock)
        stockData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in stocks.items()])
        stockCartLabel.config(text=stockData)
        cartProductNameEntry.delete(0, tb.END)  
        cartProductQuantityEntry.delete(0, tb.END)
        return cart
            
    







    updateWindow()
    stock = sortByProduct(stock)
    stockData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in stock.items()])
    cart={}
    cartData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in cart.items()])


    customerControlLabel = tb.Label(root,text="Welcome Customer", font=("Helvetica",28), bootstyle="default" )
    customerControlLabel.place(x=10,y=10)


    cartProductNameLabel = tb.Label(root, text="Product Name", font=("Helvetica"), bootstyle="success" )
    cartProductNameLabel.place(x=50,y=70)

    cartProductNameEntry = tb.Entry()
    cartProductNameEntry.place(x=215,y=68)


    cartProductQuantityLabel = tb.Label(root, text="Product Quantity", font=("Helvetica"), bootstyle="success" )
    cartProductQuantityLabel.place(x=50,y=150)

    cartProductQuantityEntry = tb.Entry()
    cartProductQuantityEntry.place(x=215,y=148)


    addToCartButton = tb.Button(root, text="Add to Cart", bootstyle = "success", command=addToCart )
    addToCartButton.place( x = 400, y = 105)

    removeFromCartButton = tb.Button(root, text="Remove Item", bootstyle = "success", command=removeFromCart)
    removeFromCartButton.place( x = 550, y=105)

    checkoutButton = tb.Button(root, text="Checkout", bootstyle = "success", command= lambda: checkout(cart))
    checkoutButton.place( x = 700, y=105)


    sstockCartLabel = tb.Label(text= "ITEMS IN SHELF" , font=("Helvetica",18),bootstyle= "default" )
    sstockCartLabel.place(x=100, y=300)

    stockCartLabel = tb.Label(text= stockData ,bootstyle= "Success" )
    stockCartLabel.place(x=100, y=350)


    ccartLabel = tb.Label(text= "ITEMS IN CART", font=("Helvetica",18) ,bootstyle= "default" )
    ccartLabel.place(x=750, y=300)

    cartLabel = tb.Label(text= cartData ,bootstyle= "Success" )
    cartLabel.place(x=750, y=350)


    infoLabel = tb.Label(text="", bootstyle= "Success" )
    infoLabel.place(x=50, y=200)


    # yesButton = tb.Button(text="Yes", bootstyle = "success" )
    # yesButton.place( x = 50, y = 240)


    # noButton = tb.Button(text="Cancel", bootstyle = "default" )
    # noButton.place( x = 110, y = 240)
    
    # backButton = tb.Button(text="Leave", bootstyle = "danger", command= mainLayout)
    # backButton.place( x = 1200, y = 63)


def mainLayout(stock):
    updateWindow()
    whoAreYouLabel =  tb.Label(text="Hello! Who are you ?",
                            font=("Helvetica",28),
                            bootstyle = "default")
    whoAreYouLabel.pack(pady=(50,0))# creates and moves the label down the y-axis by 50


    adminButton = tb.Button(text="Admin", bootstyle = "primary",command=adminAuthLayout )
    adminButton.pack(pady=30, padx= (370,200) , side="left")# moves the button west and row is the x-axis and column is the Y-axis

    CustomerButton = tb.Button(text="Customer", bootstyle = "primary",command= lambda:customerLayout(stock))
    CustomerButton.pack(pady=30, padx=(0,200) ,side="left")# moves the button west and row is the x-axis and column is the Y-axis

    exitButton = tb.Button(text="Exit", bootstyle = "primary", command= exitWindow)
    exitButton.pack( pady=0, padx=0 ,side="left")# moves the button west and row is the x-axis and column is the Y-axis




stock = {"Dog":[100,1.3],
         "Cat":[10,4.3],
         "hamsters":[18,10.50],
         "bIrDs":[122,1.3],
         "hOrse":[50,270],
         "Frog":[100,1.3], 
         "Rabbit":[737,2.30],
         "fish":[15,2.13] }
# adminLayout(stock)

# customerLayout(stock)

mainLayout(stock)

root.mainloop()



