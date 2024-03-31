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

def adminLayout():
    updateWindow()
    stock = {"Dog":[100,1.3],
         "Cat":[10,4.3],
         "hamsters":[18,10.50],
         "bIrDs":[122,1.3],
         "hOrse":[50,270],
         "Frog":[100,1.3], 
         "Rabbit":[737,2.30],
         "fish":[15,2.13] }
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


    # stockFrame= tb.Frame(root, bootstyle="light")
    # stockFrame.pack(fill=tb.BOTH, expand=True, padx=20, pady=20)

    stockLabel = tb.Label(text= stockData ,bootstyle= "default" )
    stockLabel.place(x=750, y=280)

    infoLabel = tb.Label(text="Are you Sure?", bootstyle= "Success" )
    infoLabel.place(x=150, y=600)


    yesButton = tb.Button(text="Yes", bootstyle = "success" )
    yesButton.place( x = 200, y = 695)


    noButton = tb.Button(text="Cancel", bootstyle = "default",command=adminLayout )
    noButton.place( x = 250, y = 695)

    logoutButton = tb.Button(text="Logout", bootstyle = "danger", command= mainLayout)
    logoutButton.place( x = 1200, y = 63)
   






def adminAuthLayout():
    def login():
        
        username = adminUsernameEntry.get()
        password = adminPasswordEntry.get()

        if username == "Admin" and password == "Admin123":
            adminLayout()
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

    goBackButton = tb.Button(text="<<Back", bootstyle = "primary", command=mainLayout)
    goBackButton.place( x = 600, y = 450)

    infoLabel = tb.Label(text="", bootstyle= "Success" )
    infoLabel.place(x=150, y=600)
    
    loginButton = tb.Button(text="Login", bootstyle = "success", command=login)
    loginButton.place( x = 750, y=450)



   

def customerLayout():
    updateWindow()

    stockData = "\n".join([f"Product Name: {key}        Quantity: {info[0]}        Price per item: ${info[1]:.2f}" for key, info in stock.items()])
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


    addToCartButton = tb.Button(root, text="Add to Cart", bootstyle = "success" )
    addToCartButton.place( x = 400, y = 105)

    removeFromCartButton = tb.Button(root, text="Remove Item", bootstyle = "success")
    removeFromCartButton.place( x = 550, y=105)

    checkoutButton = tb.Button(root, text="Checkout", bootstyle = "success")
    checkoutButton.place( x = 700, y=105)


    sstockCartLabel = tb.Label(text= "ITEMS IN SHELF" , font=("Helvetica",18),bootstyle= "default" )
    sstockCartLabel.place(x=100, y=300)

    stockCartLabel = tb.Label(text= stockData ,bootstyle= "Success" )
    stockCartLabel.place(x=100, y=350)


    ccartLabel = tb.Label(text= "ITEMS IN CART", font=("Helvetica",18) ,bootstyle= "default" )
    ccartLabel.place(x=750, y=300)

    cartLabel = tb.Label(text= cartData ,bootstyle= "Success" )
    cartLabel.place(x=750, y=350)


    infoLabel = tb.Label(text="Are you Sure?", bootstyle= "Success" )
    infoLabel.place(x=50, y=200)


    yesButton = tb.Button(text="Yes", bootstyle = "success" )
    yesButton.place( x = 50, y = 240)


    noButton = tb.Button(text="Cancel", bootstyle = "default" )
    noButton.place( x = 110, y = 240)

    backButton = tb.Button(text="Leave", bootstyle = "danger", command= mainLayout)
    backButton.place( x = 1200, y = 63)

def mainLayout():
    updateWindow()
    whoAreYouLabel =  tb.Label(text="Hello! Who are you ?",
                            font=("Helvetica",28),
                            bootstyle = "default")
    whoAreYouLabel.pack(pady=(50,0))# creates and moves the label down the y-axis by 50


    adminButton = tb.Button(text="Admin", bootstyle = "primary",command=adminAuthLayout )
    adminButton.pack(pady=30, padx= (370,200) , side="left")# moves the button west and row is the x-axis and column is the Y-axis

    CustomerButton = tb.Button(text="Customer", bootstyle = "primary",command=customerLayout)
    CustomerButton.pack(pady=30, padx=(0,200) ,side="left")# moves the button west and row is the x-axis and column is the Y-axis

    exitButton = tb.Button(text="Exit", bootstyle = "primary", command= exitWindow)
    exitButton.pack( pady=0, padx=0 ,side="left")# moves the button west and row is the x-axis and column is the Y-axis


    
#creating label 
stock = {"Dog":[100,1.3],
         "Cat":[10,4.3],
         "hamsters":[18,10.50],
         "bIrDs":[122,1.3],
         "hOrse":[50,270],
         "Frog":[100,1.3], 
         "Rabbit":[737,2.30],
         "fish":[15,2.13] }


cart = { }

mainLayout()


root.mainloop()


