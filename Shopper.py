from User import User
from datetime import datetime


class Shopper(User):
    def __init__(self, id, name, dob, role, active, basket, order):
        super().__init__(id, name, dob, role, active)
        self.__basket = basket
        self.__order = order

    def __str__(self):
        return f"Shopper: {self.id}\nName: {self.name}\nDate of Birth: {self.dob}\nRole: {self.role}\nActive: {self.active}\nBasket: {self.basket}\nOrder: {self.order}"

    @classmethod
    def create_new_user(cls, id, name, dob, role, active, basket, order):
        return cls(id, name, dob, role, active, basket, order)

    @property
    def basket(self):
        return self.__basket

    @basket.setter
    def basket(self, basket):
        self.__basket = basket

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        self.__order = order

    @staticmethod
    def add_new_user(users, role):
        print("\n[+] Adding New User...")
        # get the user info from the user
        # get ID
        while True:
            try:
                id = int(input("ID: "))
                # check if the id 6-digits
                if len(str(id)) != 6:
                    print("\n[-] ID Must be 6-Digits, Try Again Please...")
                    raise ValueError
                # check if the user exist
                for user in users:
                    if user.id == id:
                        print("\n[-] User Already Exist, Try Again Please...")
                        raise ValueError
                    
                break
            except ValueError or KeyboardInterrupt:
                print("\n[-] Please Enter a Valid ID...")
                continue
        # get Name
        name = input("Name: ")
        # get Date of Birth
        while True:
            try:
                dob = input("Date of Birth: ")
                dob = datetime.strptime(dob, "%d/%m/%Y").date()
                break
            except ValueError or KeyboardInterrupt:
                print("\n[-] Invalid Date, Please Try Again...")
                continue

        # get Active
        while True:
            try:
                active = int(input("Active: "))
                if active != 1 and active != 0:
                    print("\n[-] Invalid Input, Try Again Please...")
                    continue
                else:
                    break
            except ValueError or KeyboardInterrupt:
                print("\n[-] Invalid Input, Try Again Please...")
                continue
        # set Basket as Empty Basket
        basket = {}

        # set order
        order = 0

        # create a new user
        users.append(
            Shopper.create_new_user(id, name, dob, role, active, basket, order)
        )

    @staticmethod
    def list_shoppers(users):
        print("1. All")
        print("2. With Items in the Basket")
        print("3. Has an Processed Orders")
        print("4. Requested an Order")

        choose = 0
        while True:
            try:
                choose = int(input("Choose an Option Please: "))
                break
            except ValueError or KeyboardInterrupt:
                print("\n[-] Invalid Input, Try Again...")
                continue
        match choose:
            case 1:
                print("\n[+] Displaying All Shoppers...")
                for u in users:
                    if u.role == "shopper":
                        print("____________User Information______________")
                        print(u)
            case 2:
                for u in users:
                    if u.role == "shopper" and u.basket != {}:
                        print("____________User Information______________")
                        print(u)

            case 3:
                for u in users:
                    if u.role == "shopper" and u.order != 0:
                        print("____________User Information______________")
                        print(u)

            case 4:
                for u in users:
                    if u.role == "shopper" and u.order == 0:
                        print("____________User Information______________")
                        print(u)

            case _:
                print("\n[-] Invalid Input, Try Again...")
            # end of list_shoppers()

    def add_product_to_basket(self, products):
        print("\n[+] Adding Product...")
        # print produucts
        print("\n______________________Products List________________________\n")
        for p in products:
            print(p)
        print("\n")

        while True:
            try:
                id = int(input("Enter the ID of the product: "))
                break
            except ValueError or KeyboardInterrupt:
                print("\n[-] Invalid Input, Try Again Please...")

        # search for id
        product = None
        for p in products:
            if p.id == id:
                product = p

        if product == None:
            print("\n[-] There is no product with the attached ID")
        else:
            product_inventory = product.inventory
            while True:
                try:
                    number_to_be_added = int(input("Enter the Quantitiy to Add: "))
                    if number_to_be_added > product_inventory:
                        print(
                            f"\n[-] The Inventory has {product_inventory} of this product"
                        )
                        continue
                    else:
                        break
                except:
                    print("\n[-] Invalid Input, please Try Again")

            self.basket = {id: number_to_be_added}
            # inventory
            product.inventory -= number_to_be_added
            print("\n[+] Added Successfully...")
            # end of add_product_to_basket()

    def display_basket(self, products):
        print("\n[+] Displaying Basket...")
        if self.basket == {}:
            print("\n[-] Your Basket is Empty...")
        else:
            # print info for each product
            for id, quantity in self.basket.items():
                print(
                    "\n______________________Product Information________________________\n"
                )
                for p in products:
                    if p.id == id:
                        print(p)
                        print(f"Quantity: {quantity}")
            # calculate the total price
            total_price = 0
            for id, quantity in self.basket.items():
                for p in products:
                    if p.id == id:
                        if p.has_an_offer == 1:
                            total_price += p.offer.offer_price * quantity
                        else:
                            total_price += p.price * quantity
                print(f"\n[+] Total Price = {total_price}")
            # end of display_basket()

    def update_basket(self, products):
        # print basket
        print("\n______________________Basket Information________________________\n")
        self.display_basket(products)
        
        print("\n[+] Updating Basket...")
        print("1. Clear")
        print("2. Remove")
        print("3. Update")

        option = 0
        while True:
            try:
                option = int(input("Choose an Option: "))
                break
            except ValueError and KeyboardInterrupt:
                print("\n[-] Invalid Input, Please Try Again...")
                continue
        match option:
            case 1:
                # Clear the User Basket...
                self.basket = {}
                # update inventory of products
                for id, quantity in self.basket.items():
                    for p in products:
                        if p.id == id:
                            p.inventory += quantity
            case 2:
                while True:
                    try:
                        id = int(input("Enter the ID of the Product to be Removed: "))
                        break
                    except ValueError and KeyboardInterrupt:
                        print("\n[-] Invalid Input, Please Try Again...")
                        continue

                # Search for the Product
                product = None
                for p in products:
                    if p.id == id:
                        product = p
                if product == None:
                    print("\n[-] The Product is not Exist...")
                else:
                    for key, value in self.basket.items():
                        if key == id:
                            
                            # update inventory of products
                            for id, quantity in self.basket.items():
                                for p in products:
                                    if p.id == id:
                                        p.inventory += quantity
                            print("\n[+] Removed Successfully")
                            del self.basket[id]
                            break
                        else:
                            print("\n[-] The Product is not Exist in the Basket...")

            case 3:
                # Update the number of items in the basket
                while True:
                    try:
                        id = int(input("Enter the ID of the Product to be Updated: "))
                        break
                    except ValueError and KeyboardInterrupt:
                        print("\n[-] Invalid Input, Please Try Again...")
                        continue
                # is it added in the shopper basket?
                is_added = False
                product = None
                for key, value in self.basket.items():
                    if key == id:
                        is_added = True
                        for p in products:
                            if p.id == id:
                                product = p
                        break
                if is_added == False:
                    print("\n[-] The Product is not Exist in the Basket...")
                else:
                    # take the new number of items:
                    while True:
                        try:
                            new_quantity = int(
                                input("Enter the New Number of Items: ")
                            )
                            break
                        except ValueError and KeyboardInterrupt:
                            print("\n[-] Invalid Input, Please Try Again...")
                            continue
                    # check if the new number is less than the inventory
                    if new_quantity > product.inventory + self.basket[id]:
                        print(
                            f"\n[-] The Inventory has {product.inventory} of this product"
                        )
                    else:
                        # update the number of items in shopper basket
                        pastQuantity = self.basket[id]
                        self.basket[id] = new_quantity
                        # update inventory of products
                        for id, quantity in self.basket.items():
                            for p in products:
                                if p.id == id:
                                    p.inventory += pastQuantity
                                    p.inventory -= new_quantity
                        print("\n[+] Updated Successfully...")
               
                        
            case _:
                print("\n[-] Invalid Input, Please Try Again...")
        # end of update_basket()

    def request_order(self):
        print("\n[+] Requesting Order...")
        if self.basket == {}:
            print("\n[-] Your Basket is Empty...")
        elif self.order == 1:
            print("\n[+] You Already Requested an Order...")
        else:
            self.order = 1
            print("\n[+] Requested Successfully...")
        # end of request_order()

    def execute_order(self, products):
        print("\n[+] Executing Order...")
        if self.order == 0:
            print("\n[-] You Don't Have an Order...")
        else:
            # print info for each product
            for id, quantity in self.basket.items():
                print(
                    "\n______________________Product Information________________________\n"
                )
                for p in products:
                    if p.id == id:
                        print(p)
                        print(f"Quantity: {quantity}")
            # calculate the total price
            total_price = 0
            for id, quantity in self.basket.items():
                for p in products:
                    if p.id == id:
                        if p.has_an_offer == 1:
                            total_price += p.offer.offer_price * quantity
                        else:
                            total_price += p.price * quantity
                print(f"\n[+] Total Price = {total_price}")
                # clear basket
                self.basket = {}
                print("\n[+] The order executed successfully, and the Basket is Clear Now...")
    # end of execute_order()

   
        
