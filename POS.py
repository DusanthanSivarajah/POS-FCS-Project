# FCS 50 Project
# You are tasked with developing a Point of Service (POS) system for a retail company (the company
# who buy things and then sell the things to other companies).
# When the user first runs your system, they are greeted with the first menu.
# Menu 1:
# Enter:
# 1. To modify the quantities in storage.
# 2. To add an order
# 3. To exit
# If the user inputs 1, the list of items, and their quantities in storage, are displayed in alphabetical 
# order, ignoring the case of the letters (so “abc” is displayed before “BB”)
# For example, the code can display:
# apples: 5
# Basketball: 10
# Candles:3
# Once all these items are displayed, the user is shown menu 2:
# Enter:
# 1. To modify the quantities of an item.
# 2. To display the items sorted by quantities.
# If the user inputs 1, they are prompted for the item name, and then the new quantity of that item. 
# If the item did not previously exist in the storage data structure, it is added with the given quantity.
# If the item exists, it is updated with its new quantity.
# And if the user inputs quantity =0, the item is deleted from storage.
# If the user inputs 2, the items are displayed in descending order, sorted by quantity. For example, 
# the previous items would be displayed as the following:
# Basketball: 10
# apples: 5
# Candles:3
# Once the user makes these selection, they are taken back to Menu 1.
# ----- Menu 2 is done, we go back to menu 1 -----
# Going back to Menu 1, if the user inputs 2, it means that there is a customer who would like to buy 
# the items from storage.
# The items are first displayed to the user, and then the user is repeatedly asked to input the items
# and quantities the customer is buying. Once the user inputs -1 as the item name, or -1 as the 
# quantity purchased, it means that the clients have purchased all the items they want.
# Beware: while buying the items the client might ask for something that does not exist in storage (for 
# example, oranges), or might want to purchase more quantities than available in stock (for example,
# 100 candles). In these cases, the user should get a warning that this item, or quantity, is not 
# available in stock).
# Once the user completed adding all the items they would like to purchase, they are asked if they 
# would like to place the order:
# Would you like to place this order? (y/n)
# If the user inputs y, the purchased items are printed to the user along with their quantities, and the 
# quantities in storage are updated.
# If the user inputs n, or any other input, the system displays: order not placed.
# Once this menu is complete, the user is taken back to Menu 1.
# The deadline of this project is Sunday, March 31st
# . We will discuss in class when the code review 
# session will be.