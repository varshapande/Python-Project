
import admin as aa
import user as us
from user import User


inp = int(input("Where You want to login select 1.Admin and 2.User and 3.Exit"))
if inp == 1:
    username = input("Enter the username of admin: ")
    password = input("Enter the password of admin: ")
    if aa.admin_keys[username]==password :
       
        print("*****You're successfully logged inn*****")
        admin_crawler = True
        while admin_crawler:
            adm_choice = int(input("Choose the options of admin panel 1.ADD NEW ITEM 2.EDIT ITEM 3.final VIEW INVENTORY 4. show_inven 5.REMOVE ITEM 6.EXIT"))
            if adm_choice == 1:
                aa.add_new_item()
            elif adm_choice == 2:
                aa.edit_inven()
            elif adm_choice == 3:
                aa.final_inven()
            elif adm_choice == 4:
                aa.show_inven()
            elif adm_choice == 5:
                aa.remove_item() 
            elif adm_choice == 6:
                print(f"You're Exit to the admin panel{Username}")
                admin_crawler = False
            else:
                print("This is the wrong selection please select valid option")
    else:
        print("These are the wrong credentials! SORRY!!!")
elif inp == 2:
    print("Welcome to the user panel, resister your account")
    uhh = User(input("name :"),input("enternumber :"),input("email address:"),input("address :"),input("password :"))
    username = input("Enter the username here: ")
    password = input("Enter the password here: ")
    if User.login(username, password):
        print(f"You are logged in successfully {username}")
        user_crawler = True
        while user_crawler:
            usr_choice = int(input(f"{username}, Enter the option 1.Place new order 2.Order history 3.Exit"))
            if usr_choice == 1:
                uhh.place_order()
            elif usr_choice == 2:
                print(f"Here is your order history, {username}")
                print(uhh.order_history)
            elif usr_choice == 3:
                user_crawler = False
                print("You're Successfully looged out")
            else:
                print("You choose the invalid option")
    else:
        print("These are the wrong credentials! SORRY!!!")
else:
    exit()



