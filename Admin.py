from User import User
from datetime import datetime

class Admin(User):
    def __init__(self, id, name, dob, role, active):
        super().__init__(id, name, dob, role, active)

    def __str__(self):
        return f"Admin: {self.id}\nName: {self.name}\nDate of Birth: {self.dob}\nRole: {self.role}\nActive: {self.active}"
    
    @classmethod
    def create_new_user(cls, id, name, dob, role, active):
        return cls(id, name, dob, role, active)
        

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

        # create a new user
        users.append(Admin.create_new_user(id, name, dob, role, active))
    
