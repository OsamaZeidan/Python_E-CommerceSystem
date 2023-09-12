from enum import Enum
from datetime import datetime
from Offer import Offer


class Category(Enum):
    FOOD = "Food"
    DRINK = "Drink"
    ELECTRONICS = "Electronics"
    CLOTHES = "Clothes"
    SHOES = "Shoes"
    ACCESSORIES = "Accessories"
    BOOKS = "Books"
    OTHER = "Other"


class Product:
    def __init__(
        self,
        id,
        name,
        category,
        price,
        inventory,
        supplier,
        has_an_offer,
        offer,
    ):
        # private
        self.__id = id
        self.__name = name
        self.__category = category
        self.__price = price
        self.__inventory = inventory
        self.__supplier = supplier
        self.__has_an_offer = has_an_offer
        self.__offer = offer

    # setters & getters
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        self.__category = category

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def inventory(self):
        return self.__inventory

    @inventory.setter
    def inventory(self, inventory):
        self.__inventory = inventory

    @property
    def supplier(self):
        return self.__supplier

    @supplier.setter
    def supplier(self, supplier):
        self.__supplier = supplier

    @property
    def has_an_offer(self):
        return self.__has_an_offer

    @has_an_offer.setter
    def has_an_offer(self, has_an_offer):
        self.__has_an_offer = has_an_offer

    @property
    def offer(self):
        return self.__offer

    @offer.setter
    def offer(self, offer):
        self.__offer = offer

    @classmethod
    def create_new_product(
        cls,
        id,
        name,
        category,
        price,
        inventory,
        supplier,
        has_an_offer,
        offer,
    ):
        return cls(
            id,
            name,
            category,
            price,
            inventory,
            supplier,
            has_an_offer,
            offer,
        )

    def __str__(self):
        return f"ID: {self.__id}\nProduct: {self.__name}\nCategory: {self.__category}\nPrice: {self.__price}\nInventory: {self.__inventory}\nSupplier: {self.__supplier}\nHas an offer: {self.__has_an_offer}\nOffer:\n{self.__offer}\n"

    # _______________add_product() Function___________________________
    @staticmethod
    def add_product(products):
        print("\n[+] Adding Product...")
        # get the product info from the user
        while True:
            try:
                id = int(input("ID: "))
                # check if 6 digit
                if len(str(id)) != 6:
                    print("\n[-] Please Enter a Valid ID...")
                    raise ValueError
                
                # check if is already exists
                for product in products:
                    if product.id == id:
                        print("\n[-] This Product is Already Exist...")
                        raise ValueError
                break
            except ValueError:
                print("\n[-] Please Enter a Valid ID...")
                continue

        name = input("Name: ")
        while True:
            try:
                print(
                    "\n[+] Categories List: \n_____________________________________\n"
                )
                for category in Category:
                    print(category.value)

                category = Category[input("Category: ").upper()]
                break
            except:
                print("\n[-] Please Enter a Valid Category...")
                continue

        while True:
            try:
                price = int(input("Price: "))
                break
            except ValueError:
                print("\n[-] Please Enter a Valid Price...")
                continue

        while True:
            try:
                inventory = int(input("Inventory: "))
                break
            except ValueError:
                print("\n[-] Please Enter a Valid Inventory...")
                continue

        supplier = input("Supplier: ")
        while True:
            try:
                
                has_an_offer = int(input("Has an Offer: "))
                # check if 1 or 0
                if has_an_offer != 1 and has_an_offer != 0:
                    print("\n[-] Please Enter a Valid Has an Offer value...")
                    raise ValueError
                break
            except ValueError:
                print("\n[-] Please Enter a Valid Has an Offer value...")
                continue

        if has_an_offer == 1:
            while True:
                try:
                    offer_price = int(input("Offer Price: "))
                    break
                except ValueError:
                    print("\n[-] Please Enter a Valid Offer Price...")
                    continue

            while True:
                try:
                    valid_until = datetime.strptime(
                        input("Valid Until: "), "%d/%m/%Y"
                    ).date()
                    break
                except ValueError:
                    print("\n[-] Please Enter a Valid Date...")
                    continue

            offer = Offer.create_new_offer(offer_price, valid_until)
        else:
            offer = Offer.create_new_offer(0, "00/00/00")

        # create a new product
        products.append(
            Product.create_new_product(
                id, name, category, price, inventory, supplier, has_an_offer, offer
            )
        )

    # end of add_product()

    # _______________update_product() Function___________________________
    @staticmethod
    def update_product(products):
        print("\n[+] Updating a Product")

        while True:
            try:
                id = int(input("ID: "))
                break
            except:
                print("\n[-] Invalid Id, Try Again Please..")

        # search for the product
        product = None
        for p in products:
            if p.id == id:
                product = p
                break
        if product == None:
            print("\n[-] This Product is not Exist")
        else:
            print(product)
            option1 = 0
            while True:
                print("____________________\n")
                print("\n[+] Choose what do you want to update: ")
                print("1. Name")
                print("2. Category")
                print("3. Price")
                print("4. Inventory")
                print("5. Supplier")
                print("6. Has an Offer")
                print("7. All")
                print("8. Exit")
                while True:
                    try:
                        option1 = int(input("Choose an Option: "))
                        break
                    except ValueError or KeyboardInterrupt:
                        print("\n[-] Invalid Input, Try Again...")
                match option1:
                    case 1:
                        name = input("Enter the New Name: ")
                        product.name = name

                    case 2:
                        # Update category
                        print(
                            "\n[+] Enter the Name of the new Category from the Category List...(Case Insensetive)"
                        )
                        # print categories list
                        print(
                            "\n______________________Categories List________________________\n"
                        )
                        print(Category._member_names_)
                        print("\n")

                        while True:
                            category = input("New Category: ").upper()
                            if category in Category._member_names_:
                                break
                            else:
                                print("\n[-] Invalid Input, Try Again Please...")
                        product.category = category

                    case 3:
                        while True:
                            try:
                                price = int(input("Enter the New Price: "))
                                break
                            except:
                                print("\n[-] Invalid Input, Try Again Please...")
                        product.price = price

                        if option1 == 103:
                            option1 = 104
                        else:
                            option1 = 0
                    case 4:
                        while True:
                            try:
                                inventory = int(input("Enter the New Inventory: "))
                                break
                            except:
                                print("\n[-] Invalid Input, Try Again Please...")
                        product.inventory = inventory

                    case 5:
                        supplier = input("Enter the New Supplier: ")
                        product.supplier = supplier

                    case 6:
                        while True:
                            try:
                                has_an_offer = int(
                                    input(
                                        "if the product has an offer enter '1' else enter '0': "
                                    )
                                )
                                if has_an_offer != 1 and has_an_offer != 0:
                                    print("\n[-] Invalid Input, Try Again Please...")
                                    continue
                                else:
                                    break
                            except:
                                print("\n[-] Invalid Input, Try Again Please...")
                        product.has_an_offer = has_an_offer
                        if has_an_offer == 1:
                            while True:
                                try:
                                    offer_price = int(
                                        input("Enter the New Offer Price: ")
                                    )
                                    break
                                except:
                                    print("\n[-] Invalid Input, Try Again Please...")
                            while True:
                                try:
                                    valid_until = datetime.strptime(
                                        input("Enter the New Valid Until: "), "%d/%m/%Y"
                                    ).date()
                                    break
                                except:
                                    print("\n[-] Invalid Input, Try Again Please...")
                            product.offer = Offer.create_new_offer(
                                offer_price, valid_until
                            )
                        else:
                            product.offer = Offer.create_new_offer(0, "00/00/00")

                    case 7:
                        # execute all cases from 1 to 6

                        # case 1 code:
                        name = input("Enter the New Name: ")
                        product.name = name

                        # _______________________________________________________#
                        # case 2 code:
                        # Update category
                        print(
                            "\n[+] Enter the Name of the new Category from the Category List...(Case Insensetive)"
                        )
                        # print categories list
                        print(
                            "\n______________________Categories List________________________\n"
                        )
                        print(Category._member_names_)
                        print("\n")

                        while True:
                            category = input("New Category: ").upper()
                            if category in Category._member_names_:
                                break
                            else:
                                print("\n[-] Invalid Input, Try Again Please...")
                        product.category = category
                        # __________________________________________________________#
                        # case 3 code:
                        while True:
                            try:
                                price = int(input("Enter the New Price: "))
                                break
                            except:
                                print("\n[-] Invalid Input, Try Again Please...")
                        product.price = price

                        if option1 == 103:
                            option1 = 104
                        else:
                            option1 = 0
                        # __________________________________________________________#
                        # case 4 code:
                        while True:
                            try:
                                inventory = int(input("Enter the New Inventory: "))
                                break
                            except:
                                print("\n[-] Invalid Input, Try Again Please...")
                        product.inventory = inventory
                        # __________________________________________________________#
                        # case 5 code:
                        supplier = input("Enter the New Supplier: ")
                        product.supplier = supplier
                        # __________________________________________________________#
                        # case 6 code:
                        while True:
                            try:
                                has_an_offer = int(
                                    input(
                                        "if the product has an offer enter '1' else enter '0': "
                                    )
                                )
                                if has_an_offer != 1 and has_an_offer != 0:
                                    print("\n[-] Invalid Input, Try Again Please...")
                                    continue
                                else:
                                    break
                            except:
                                print("\n[-] Invalid Input, Try Again Please...")
                        product.has_an_offer = has_an_offer
                        if has_an_offer == 1:
                            while True:
                                try:
                                    offer_price = int(
                                        input("Enter the New Offer Price: ")
                                    )
                                    break
                                except:
                                    print("\n[-] Invalid Input, Try Again Please...")
                            while True:
                                try:
                                    valid_until = datetime.strptime(
                                        input("Enter the New (Valid Until) Date: "),
                                        "%d/%m/%Y",
                                    ).date()
                                    break
                                except:
                                    print("\n[-] Invalid Input, Try Again Please...")
                            product.offer = Offer.create_new_offer(
                                offer_price, valid_until
                            )
                        else:
                            product.offer = Offer.create_new_offer(0, "00/00/00")
                        # __________________________________________________________#
                        # end of cases

                    case 8:
                        break

                    case _:
                        print("\n[-] Invalid Input, Try Again Please...")
                        continue

    # end of update_product()

    # _______________place_item_on_sale() Function___________________________
    def place_item_on_sale(products):
        print("\n[+] Placing Item on Sale...")
        # get the product info from the user
        while True:
            try:
                id = int(input("ID: "))
                break
            except ValueError:
                print("\n[-] Please Enter a Valid ID...")
                continue

        # search for the product
        product = None
        for p in products:
            if p.id == id:
                product = p
                print(p)
                break

        if product is None:
            print("\n[-] Product Not Found...")
        else:
            # place the item on sale
            # set has an offer to 1
            product.has_an_offer = 1

            while True:
                try:
                    offer_price = int(input("Offer Price: "))
                    break
                except ValueError:
                    print("\n[-] Please Enter a Valid Offer Price...")
                    continue

            while True:
                try:
                    valid_until = datetime.strptime(
                        input("Valid Until: "), "%d/%m/%Y"
                    ).date()
                    break
                except ValueError:
                    print("\n[-] Please Enter a Valid Date...")
                    continue

            product.offer = Offer.create_new_offer(offer_price, valid_until)
            print("\n[+] Done!\n")

    # end of place_item_on_sale()
    
    @staticmethod
    def list_products(products):
            print("1. All")
            print("2. By Offers")
            print("3. By Category")
            print("4. By Name")

            choose = 0
            while True:
                try:
                    choose = int(input("Choose an Option: "))
                    break
                except ValueError or KeyboardInterrupt:
                    print("\n[-] Invalid Input, Try Again...")
                    continue
            match choose:
                case 1:
                    print("\n[+] Displaying All Products...")
                    for p in products:
                        print(p)
                case 2:
                    print("\n[+] Displaying All Products with Offers...")
                    for p in products:
                        if p.has_an_offer == 1:
                            print(p)
                case 3:
                    print("\n[+] Displaying All Products by Category...")
                    print(
                        "\n[+] Enter the Category from the Category List...(Case Insensetive)"
                    )
                    # print categories list
                    print(
                        "\n______________________Categories List________________________\n"
                    )
                    print(Category._member_names_)
                    print("\n")
                    while True:
                        category = input("Category: ").upper()
                        if category in Category._member_names_:
                            break
                        else:
                            print("\n[-] Invalid Input, Try Again Please...")
                    for p in products:
                        if p.category == category:
                            print(p)
                case 4:
                    print("\n[+] Displaying All Products by Name...")
                    name = input("Enter the Name of the Product: ")
                    for p in products:
                        if p.name == name:
                            print(p)
                case _:
                    print("\n[-] Invalid Input, Try Again...")
    # end of list_products()

    @staticmethod 
    def save_products_on_file(file, products):
        with open(file, "w") as f:
            for product in products:
                if product.has_an_offer == 1:
                    f.write(f"{product.id};{product.name};{product.category};{product.price};{product.inventory};{product.supplier};{product.has_an_offer};{product.offer.offer_price};{product.offer.valid_until.day}/{product.offer.valid_until.month}/{product.offer.valid_until.year}")
                else:
                    f.write(f"{product.id};{product.name};{product.category};{product.price};{product.inventory};{product.supplier};0;0;0/0/0")
                f.write("\n")
        
