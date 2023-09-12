from Product import Product, Category
from User import User
from Admin import Admin
from Shopper import Shopper
from datetime import datetime
from Offer import Offer

print(
    "\n______________________________________________Welcome To Osama's E-Commerce Systeem...______________________________________________\n"
)

# load the data from files (products & users)
# create a list of products
products = []
with open("products.txt", "r") as file:
    line_number = 0
    for line in file:
        info = line.strip().split(";")
        line_number += 1

        try:
            # check if info[0] is only 6 digits
            if len(info[0]) != 6:
                print(f"\n[-] Error in Line {line_number} in products.txt file...")
                raise ValueError
            
            # check has_an_offer 1 or 0
            if int(info[6]) != 1 and int(info[6]) != 0:
                print(f"\n[-] Error in Line {line_number} in products.txt file...")
                raise ValueError
            
            # check if info[0] is in list
            for p in products:
                if p.id == int(info[0]):
                    print(f"\n[-] Error in Line {line_number} in products.txt file...")
                    raise ValueError
            # offer
            try:
                offer = Offer.create_new_offer(
                    int(info[7]), datetime.strptime(info[8], "%d/%m/%Y").date()
                )
            except:
                # put empty date
                offer = Offer.create_new_offer(int(info[7]), "0/0/0")
            products.append(
                Product.create_new_product(
                    int(info[0]),
                    str(info[1]),
                    Category[info[2]].name,
                    int(info[3]),
                    int(info[4]),
                    str(info[5]),
                    int(info[6]),
                    offer,
                )
            )
        except:
            print(
                f"\n[-] Error in Line {line_number} in products.txt file... >> Notes: Check if there is any repetetion, the ID should be 6-digits only and check the validity of all inputs like: Date..."
            )
            continue

# create a list of users
users = []
line_number = 0
with open("users.txt", "r") as file:
    for line in file:
        info = line.strip().split(";")
        line_number += 1
        try:
            # check if only the role admin or shopper
            if info[3] != "admin" and info[3] != "shopper":
                print(f"\n[-] Error in Line {line_number} in users.txt file...")
                raise ValueError

            # check the active if only 1 or 0
            if int(info[4]) != 1 and int(info[4]) != 0:
                print(f"\n[-] Error in Line {line_number} in users.txt file...")
                raise ValueError

            # check if info[0] is only 6 digits
            if len(info[0]) != 6:
                print(f"\n[-] Error in Line {line_number} in users.txt file...")
                raise ValueError

            # check if info[0] is in list
            for u in users:
                if u.id == int(info[0]):
                    print(f"\n[-] Error in Line {line_number} in users.txt file...")
                    raise ValueError

            if info[3] == "shopper":
                # check the inventory & quantity of products
                basket = eval(info[5])
                for key in basket:
                    for p in products:
                        if p.id == key:
                            if basket[key] > p.inventory:
                                # rasie error message
                                raise ValueError(
                                    f"\n[-] In line {line_number} the Quantity of the {key} Product More Than Product Inventory"
                                )

                users.append(
                    Shopper.create_new_user(
                        int(info[0]),
                        info[1],
                        datetime.strptime(
                            info[2], "%d/%m/%Y"
                        ).date(),  # converte str to date
                        info[3],
                        int(info[4]),
                        eval(info[5]),
                        int(info[6]),  # eval() function converts str to dict
                    )
                )
                # reduce the inventory
                for key in basket:
                    for p in products:
                        if p.id == key:
                            p.inventory -= basket[key]
            else:
                users.append(
                    Admin.create_new_user(
                        int(info[0]),
                        info[1],
                        datetime.strptime(
                            info[2], "%d/%m/%Y"
                        ).date(),  # converte str to date
                        info[3],
                        int(info[4]),
                    )
                )
        except:
            print(
                f"\n[-] Error in Line {line_number} in users.txt file... >> Notes: Check if there is any repetetion, the ID should be 6-digits only and check the validity of all inputs like: Date..."
            )
            continue
# _______________________________The Data is Ready to Work_______________________________ #
# if lists are empty exit
if len(products) == 0 or len(users) == 0:
    print("\n[-] There is No Data to Work With...")
    exit()

# User Login...
print("\n[+] Please Enter Your ID to Continue...")
while True:
    try:
        id = int(input("ID: "))
        user = None
        for u in users:
            if u.id == id:
                user = u
                break

        if user is None:
            print("\n[-] User Not Found...")
        else:
            break
    except ValueError:
        print("\n[-] Please Enter a Valid ID...")
        continue

# Welcoming
print("\n__________________________________\n")
print(f"Welcome {user.name}...")
print(f"Your Role is {user.role}...")
print("Enjoy...")
print("\n__________________________________\n")


# print_menu() function
def print_menu():
    print("\nPlease Select One of the Following Options:")
    print("1. Add product (admin-only)")
    print("2. Place an item on sale (admin-only)")
    print("3. Update product (admin-only)")
    print("4. Add a new user (admin-only)")
    print("5. Update user (admin-only)")
    print("6. Display all users (admin-only)")
    print("7. List products (admin and shopper)")
    print("8. List shoppers (admin)")
    print("9. Add product to the basket (shopper-only)")
    print("10. Display basket (shopper-only)")
    print("11. Update basket (shopper-only)")
    print("12. Place order (shopper-only)")
    print("13. Execute order (admin-only)")
    print("14. Save products to a file (admin-only)")
    print("15. Save users to a text file (admin-only)")
    print("16. Exit")
    print("17. Switch User")


productsSaved = 0
usersSaved = 0


def exit_system():
    print("\n[+] Thank You For Using Osama's E-Commerce System...")
    # save products to a file
    if productsSaved == 0:
        while True:
            # ask user
            save = input("Do You Want to Save Products to a File? (y/n): ").lower()
            if save == "y":
                # file name
                file_name = input("Enter the File Name: ")
                # save products to a file
                Product.save_products_on_file(file_name, products)
                break
            elif save == "n":
                break
            else:
                print("\n[-] Invalid Input, Try Again...")
                continue

    # save users to a file
    if usersSaved == 0:
        while True:
            # ask user
            save = input("Do You Want to Save Users to a File? (y/n): ").lower()
            if save == "y":
                # file name
                file_name = input("Enter the File Name: ")
                # save users to a file
                User.save_users_on_file(file_name, users)
                break
            elif save == "n":
                break
            else:
                print("\n[-] Invalid Input, Try Again...")
                continue
    print("Good Bye!")
    exit()
    # end of exit_system()


while True:
    print_menu()
    # choose an option
    while True:
        try:
            option = int(input("Option: "))
            if option < 1 or option > 17:
                print("\n[-] Please Enter a Valid Option...")
                continue
            else:
                break
        except ValueError:
            print("\n[-] Please Enter a Valid Option...")
            continue
    match option:
        case 1:
            if user.role == "admin":
                Product.add_product(products)
            else:
                print("\n[-] You Don't Have Permission to Add a Product...")
        case 2:
            if user.role == "admin":
                # place an item on sale
                Product.place_item_on_sale(products)

            else:
                print("\n[-] You Don't Have Permission to Place an Item on Sale...")
        case 3:
            if user.role == "admin":
                Product.update_product(products)
            else:
                print("\n[-] You Don't Have Permission to Update a Product...")
        case 4:
            if isinstance(user, Admin):
                role = input("Enter the Rolle of the New User: ").lower()
                if role == "admin":
                    Admin.add_new_user(users, role)
                elif role == "shopper":
                    Shopper.add_new_user(users, role)
                else:
                    print("\n[-] Invalid Input, Try Again...")
            else:
                print("\n[-] You Don't Have Permission to Add a User...")
        case 5:
            if user.role == "admin":
                User.update_user(users)
            else:
                print("\n[-] You Don't Have Permission to Update a User...")
        case 6:
            if user.role == "admin":
                User.display_all_users(users)
            else:
                print("\n[-] You Don't Have Permission to Display All Users...")
        case 7:
            Product.list_products(products)
        case 8:
            if user.role == "admin":
                Shopper.list_shoppers(users)
            else:
                print("\n[-] You Don't Have Permission to Display All Shoppers...")
        case 9:
            if user.role == "shopper":
                # add product to the basket
                user.add_product_to_basket(products)

            else:
                print(
                    "\n[-] You Don't Have Permission to Add a Product to the Basket..."
                )
        case 10:
            if user.role == "shopper":
                # display basket
                user.display_basket(products)
            else:
                print("\n[-] You Don't Have Permission to Display Your Basket...")

        case 11:
            if user.role == "shopper":
                # update basket
                user.update_basket(products)
            else:
                print("\n[-] You Don't Have Permission to Update Your Basket...")
        case 12:
            if user.role == "shopper":
                # place order
                user.request_order()
            else:
                print("\n[-] You Don't Have Permission to Place an Order...")
        case 13:
            if user.role == "admin":
                # execute order for all shoppers have order = 1
                for u in users:
                    if u.role == "shopper" and u.order == 1:
                        print("hi")
                        u.execute_order(products)
            else:
                print("\n[-] You Don't Have Permission to Execute an Order...")

        case 14:
            if user.role == "admin":
                # file name
                file_name = input("Enter the File Name: ")
                # save products to a file
                Product.save_products_on_file(file_name, products)
                productsSaved = 1
            else:
                print("\n[-] You Don't Have Permission to Save Products to a File...")

        case 15:
            if user.role == "admin":
                # file name
                file_name = input("Enter the File Name: ")
                # save users to a file
                User.save_users_on_file(file_name, users)
                usersSaved = 1

            else:
                print("\n[-] You Don't Have Permission to Save Users to a File...")
        case 16:
            if user.role == "admin":
                exit_system()
            else:
                print("\n[+] Good Bye, Thank You for Using Osama's E-commerce System")
                exit()
        case 17:
            # switch user:
            print("\n[+] Please Enter Your ID to Continue...")
            while True:
                try:
                    id = int(input("ID: "))
                    user = None
                    for u in users:
                        if u.id == id:
                            user = u
                            break

                    if user is None:
                        print("\n[-] User Not Found...")
                    else:
                        break
                except ValueError:
                    print("\n[-] Please Enter a Valid ID...")
                    continue
        case _:
            print("\n[-] Please Enter a Valid Option...")
            continue
