
import admin as ad

class User:
    username = " "
    password = " "
    login_info = {"username":username, "password": password}

    def __init__(self, name, number, email, address, password):
        self.name = name
        self.number = number
        self.email = email
        self.address = address
        self.password = password
        User.login_info["username"] = name
        User.login_info["password"] = password
        self.profile={"Name":name}
        self.order_history = {}
        
            

    @classmethod
    def login(cls,name,password):
          if cls.login_info["username"]== name and cls.login_info["password"] == password :
              print("You're are successfully logged in.....")
              return True
          else:
              print("SORRY! These are the Wrong Credentials")
              return False

    def place_order(self):
        print("What you want to order here in the Inventory")
        print(ad.final_inven())
        user_choice = int(input("If you want to order then select 1.YES 2.NO"))
        if user_choice == 1:
            print(ad.show_inven())
            n=int(input("Enter how many items do you want to Order"))
            x=0
            for i in range(n):
             itemid = int(input("Enter the Item id here: "))
             quan = int(input("Enter the quantity of the item: "))
             quantity =int(ad.inven[itemid]["Quantity"])
             price = ad.price_cal(itemid)
             print(price)
             if quan>= quantity:
              x = x + ((price * quan)/quantity)
              print(x)
             else:
              print("minimum order has already given")
             if x>1000:
                 x = x- ((x*10)/100)
             again_ask = input("Are you still want to order this Enter YES or NO")
             if again_ask == "YES":
                print(f'''Your item name is {ad.inven[itemid]["ItemName"]}''')
                print(f'''Price of your Item is {ad.inven[itemid]["Price"]}''')
                print(f"This is your quantity {quan}")
                print(f"It costs you {x}INR in total")
                print("You're all set for this order")
                self.order_history[itemid] = {
                    "Item Name": ad.inven[itemid]["ItemName"],
                    "Price": ad.inven[itemid]["Price"],
                    "Quantity": quan
                }
                final_stock = ad.inven[itemid]["Stock"] - quan
                ad.inven[itemid]["Stock"] = final_stock
                
                print("You're order is successfully placed")

             elif again_ask == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")

    def account_register(self):
        print("please enter name:",self.name)
        print("eneter number:",self.number)
        print("enter email:",self.email)
        print("enter adress:",self.address)
        print("please enter password:",self.password)
        print("enter your login_info:",User.login_info)


def account_update():
    cs = User(input("name: "),int(input("enter number: ")),input("email_id: "),input("enter_ adress: "),input("enter password: "))
    return cs.display()

