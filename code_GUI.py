from tkinter import *
from ttkbootstrap.constants import *
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


def adminLayout(stock):
    updateWindow()
    stock=sortByProduct(stock)
    stockData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in stock.items()])


    adminControlLabel = tb.Label(root,text="Admin Control", font=("Helvetica",28), bootstyle="default" )
    adminControlLabel.place(x=570,y=50)



    productnameLabel = tb.Label(root, text="Product Name", font=("Helvetica"), bootstyle="success" )
    productnameLabel.place(x=150,y=307)

    productnameEntry = tb.Entry()
    productnameEntry.place(x=300,y=300)
    


    productQuantityLabel = tb.Label(root, text="Product Quantity", font=("Helvetica"), bootstyle="success" )
    productQuantityLabel.place(x=150,y=357)

    productQuantityEntry = tb.Entry()
    productQuantityEntry.place(x=300,y=350)
    

    ProductPriceLabel = tb.Label(root, text="Product Price", font=("Helvetica"), bootstyle="success" )
    ProductPriceLabel.place(x=150,y=407)

    ProductPriceEntry = tb.Entry()
    ProductPriceEntry.place(x=300,y=400)



    addToStockButton = tb.Button(root, text="Add/Update Item", bootstyle = "success" )
    addToStockButton.place( x = 300, y = 450)

    quantitySortButton = tb.Button(root, text="Sort by Quantity", bootstyle = "success")
    quantitySortButton.place( x = 300, y=500)


    stockLabel = tb.Label(text= stockData ,bootstyle= "default" )
    stockLabel.place(x=750, y=280)

    infoLabel = tb.Label(text="Are you Sure?", bootstyle= "Success" )
    infoLabel.place(x=150, y=600)


    yesButton = tb.Button(text="Yes", bootstyle = "success" )
    yesButton.place( x = 200, y = 695)

    
    # noButton = tb.Button(text="Cancel", bootstyle = "default",command=adminLayout )
    # noButton.place( x = 250, y = 695)

    # logoutButton = tb.Button(text="Logout", bootstyle = "danger", command= mainLayout)
    # logoutButton.place( x = 1200, y = 63)
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

def checkQuantity(compartment): # this is to check the quantity of either stock or cart is =0 , if yes , it removes the item 
    storageCopy =  compartment.copy() # creating a copy of the dictionary beacuse we cant delete items while iterating over the orginal dictionary
    for item,info in storageCopy.items():
        if info[0]<=0:
            del compartment[item]
    for items, info in compartment.items():
        print(f"Product Name: {items}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" )
    return compartment

def sortByQuantity(adminStock): # converts to a list then back to a dictionary and sorts Quantity by decending order 
    adminStock= dict(sorted(adminStock.items(), key=lambda x: x[1], reverse=True))
    for items, info in adminStock.items():
        print(f"Product Name: {items}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" )


def sortByProduct(adminStock): # sorts products in alphabetical order 
    adminStock = dict(sorted(adminStock.items())) 
    for items, info in adminStock.items():
        print(f"Product Name: {items}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" )
    return adminStock


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


stock = {"Apples":[100,1.3],
        "books":[10,4.3],
        "lights":[18,10.50],
        "chocolates":[122,1.3],
        "rat":[50,270],
        "apples":[100,1.3], 
        "Bananas":[737,2.30],
        "bbq":[15,2.13] }
adminLayout(stock)

root.mainloop()