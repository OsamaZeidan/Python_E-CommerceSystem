from datetime import datetime

class User:
    # Constructor
    def __init__(self, id, name, dob, role, active):
        # private
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__role = role
        self.__active = active

    # Setters & Getters
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
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, dob):
        self.__dob = dob

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active):
        self.__active = active

    @classmethod
    def create_new_user(cls, id, name, dob, role, active):
        raise ValueError

    def __str__(self):  # abstract method
        raise ValueError

    # Methods
    @staticmethod
    def add_new_user(users):
        raise ValueError

    @staticmethod
    def update_user(users):
        # get the user ID & Search for it
        while True:
            try:
                id = int(input("ID: "))
                break
            except ValueError or KeyboardInterrupt:
                print("\n[-] Please Enter a Valid ID...")
                continue
        # search for the user
        user = None
        for u in users:
            if u.id == id:
                user = u
                break
        if user is None:
            print("\n[-] This User is not Exisit...")
        else:
            # update the selected field
            print("\n______________________User Information________________________\n")
            print(user)
            choose = 0
            while True:
                print("1. Update Name")
                print("2. Update Date of Birth")
                print("3. Update Role")
                print("4. Update Active")
                print("5. Exit")
                print("\n** Only the Shopper Can Update the Basket and Order")
                while True:
                    try:
                        choose = int(input("Choose an Option: "))
                        break
                    except ValueError or KeyboardInterrupt:
                        print("\n[-] Invalid Input, Try Again...")
                        continue
                match choose:
                    
                    case 1:
                        name = input("Enter the New Name: ")
                        user.name = name
                    case 2:
                        while True:
                            try:
                                dob = input("Enter the New Date of Birth: ")
                                dob = datetime.strptime(dob, "%d/%m/%Y").date()
                                break
                            except ValueError or KeyboardInterrupt:
                                print("\n[-] Invalid Date, Try Again...")
                                continue
                        user.dob = dob
                    case 3:
                        while True:
                            role = input("Enter the New Role: ")
                            if role == "admin" or role == "shopper":
                                break
                            else:
                                print("\n[-] Invalid Input, Try Again...")
                                continue
                        user.role = role
                    case 4:
                        while True:
                            try:
                                active = int(input("Enter the New Active: "))
                                if active != 1 and active != 0:
                                    print("\n[-] Invalid Input, Try Again...")
                                    continue
                                break
                            except ValueError or KeyboardInterrupt:
                                print("\n[-] Invalid Input, Try Again...")
                                continue
                        user.active = active
                    case 5:
                        break
                    case _:
                        print("\n[-] Invalid Input, Try Again...")
                        continue
            print("\n[+] User Updated Successfully...")
            # end of update_user()

    @staticmethod
    def display_all_users(users):
        print("\n[+] Displaying All Users...")
        for u in users:
            print(u)
            print("______________________________\n")
        # end of display_all_users()
    @staticmethod
    def save_users_on_file(file, users):
        print("\n[+] Saving Users on File...")
        # open file
        file = open(file, "w")
        # write users on file
        for u in users:
            if u.role == "shopper":
                file.write(f"{u.id};{u.name};{u.dob.day}/{u.dob.month}/{u.dob.year};{u.role};{u.active};{u.basket};{u.order}")
            else:
                #file.write(f"{u.id};{u.name};{u.dob};{u.role};{u.active}")
                file.write(f"{u.id};{u.name};{u.dob.day}/{u.dob.month}/{u.dob.year};{u.role};{u.active}")
            file.write("\n")
        # close file
        file.close()
        print("\n[+] Saved Successfully...")
