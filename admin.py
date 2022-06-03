admin_keys = {"varsha": "pandey"}

inven = {1: {'ItemName': 'Tandoori Chicken','ItemID': 1,'Quantity': 4 ,'Price': 240,'Discount':5, 'Stock': 14},
        2: {'ItemName': 'Vegan Burger', 'ItemID': 2, 'Quantity': 1 ,'Price': 320,'Discount':5, 'Stock': 20},
        3: {'ItemName': 'Truffle Cake', 'ItemID': 3,'Quantity': 500, 'Price': 920,'Discount':5, 'Stock': 5}}
#nested dic


def piece_item(i):
        print("Item Name: ",inven[i]["ItemName"])
        print("Price: ",inven[i]["Price"],"INR")
        print("Item ID: ",inven[i]["ItemID"])
        print("Discount: ",inven[i]["Discount"],"%")
        print("Quantity: ",inven[i]["Quantity"],"pieces")
def gram_item(i):
        print("Item Name: ",inven[i]["ItemName"])
        print("Price: ",inven[i]["Price"],"INR")
        print("Item ID: ",inven[i]["ItemID"])
        print("Discount: ",inven[i]["Discount"],"%")
        print("Quantity: ",inven[i]["Quantity"],"gm")


def add_new_item():
  global x
  x = [3]
  n = int(input("how many items you want to add in list of gram items"))
  for i in range(n):  
    itemname = input("Enter the Item name: ")
    itemid = int(input("Enter the item id: "))
    price = int(input("Enter the price of the item: "))
    stock = int(input("Enter the stock value of item: "))
    Quantity = int(input("enter quantity:"))
    Discount = int(input("enter discount:"))
    inven[itemid] = {
        "ItemName": itemname,
        "ItemID": itemid,
        "Quantity": Quantity,
        "Price": price,
        "Discount": Discount,
        "Stock": stock
    }
    x.append(itemid)
  print(x)
  global y
  y = [1,2]
  n2 = int(input("items want to add in list of piece items"))
  for i in range(n2):  
    itemname = input("Enter the Item name: ")
    itemid = int(input("Enter the item id: "))
    price = int(input("Enter the price of the item: "))
    stock = int(input("Enter the stock value of item: "))
    Quantity = int(input("enter quantity:"))
    Discount = int(input("enter discount:"))
    inven[itemid] = {
        "ItemName": itemname,
        "ItemID": itemid,
        "Quantity": Quantity,
        "Price": price,
        "Discount": Discount,
        "Stock": stock
    }
    y.append(itemid)
    print("The Item"+ itemname+ "is successfully added")
    print(y)
    print(inven)

   

def edit_inven():
    item = int(input("Enter the itemid which you want to edit: "))
    a = input("Enter the item name")
    b = int(input("Enter the price of item"))
    c = int(input("Enter the stock of the item"))
    d = int(input("Enter the stock of the item"))
    e = int(input("Enter the stock of the item"))
    inven[item]["ItemName"] = a
    inven[item]["Quantity"] = b
    inven[item]["Price"] = c
    inven[item]["Discount"] = d
    inven[item]["Stock"] = e
    print("*****Edited item successfully*****")
    return inven

def price_cal(item):
    item = int(input("Enter the itemid: "))
    a= inven[item]["Price"]
    d = inven[item]["Discount"]
    z = a - ((a*d)/100)
    return z

def show_inven():
  #if admin add any item,  add those ids here also
    p = [1,2]
    for i in p:
        piece_item(i)
    g = [3]
    for i in g:
        gram_item(i)

def updated_inven():
    for i in x:
        gram_item(i)
    for i in y:
        piece_item(i)

def final_inven():
  try:
    df = True
    while df:
     i = int(input("number press 1 if you want to show updated"))
     if i ==1:
        updated_inven()
  except:
      print("no updated item")
  


def remove_item():
    d = int(input("Enter the Item id which you want to exit"))
    inven.pop(d)
    print("Remove item successfully ")
    return inven
