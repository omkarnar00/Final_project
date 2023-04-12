import json
class Restaurent:

    def __init__(self,name):
        self.restro_name=name
        self.food={}
        self.food_ID=len(self.food)+1
        self.user_details={}
        self.ordered_item=[]


    def check_admin(self):
        with open("admin.json") as f:
            data=json.load(f)    
        name=input("ENTER ADMIN  NAME : ")  
        password=input("ENTER ADMIN PASSWORD : ")  

        if data["name"]==name and data["password"]==password:
            print("ADMIN LOGIN SUCCESSFULLY.........")
        else:
            print("PLEASE ENTER A VALID DETAILS ")
 
    def add_food_items(self):
            name=input("ENTER THE FOOD NAME : ")
            quantity=float(input("ENTER THE QUANTITY : "))
            price=float(input("ENTER THE PRICE OF FOOD : "))
            discount=(input("ENTER THE DISCOUT : "))
            stock=float(input("ENTER THE AVAILABLE STOCK : "))
            food_item={"Name": name, "Quantity": quantity, "Price": price, "Discount": discount, "Stock": stock}
            self.food_ID=len(self.food)+1
            self.food[self.food_ID]=food_item

            print("FOOD ADDED SUCCESSFULLY ")

    def view_food_items(self):
        print("LIST OF FOODD ITEMS : ")        
        if len(self.food)!=0:
            for i in self.food:
                print(f"FOOD ID : {i}" )
                for j in self.food[i]:
                    print(j,":",self.food[i][j])
                print()   

        else:
            print("SORRY NO FOOD ITEM IS ADDED!!!")   

    def edit_food_item(self):
        id=input("ENTER THE FOOD ID YOU WANT TO UPDATE : ")              
        if id in self.food.keys():
            print("""
            1.UPDATE FOOD NAME\n 
            2.UPDATE FOOD QUANTITTY\n
            3.UPDATE PRICE\n
            4.UPDATE DISCOUNT\n
            5.UPDATE STOCK\n
            """)

        key=input("ENTER THE NUMBER : ")

        if key=="1":
            self.food[id]["name"]=input("UPDATE FOOD NAME : ")
            print("FOOD NAME UPDATED")
        elif key=="2":
            self.food[id]["quantity"]=input("UPDATE THE FOOD QUANTITY : ")    
            print("QUANTITY UPDATED")
        elif key=="3":
            self.food[id]["price"]=input("UPDATE THE FOOD PRICE  : ")    
            print("PRICE UPDATED") 
        elif key=="4":
            self.food[id]["discount"]=input("UPDATE THE FOOD DISCOUNT : ")    
            print("DISCOUNT UPDATED")   
        elif key=="5":
            self.food[id]["stock"]=input("UPDATE THE FOOD STOCK : ")    
            print("STOCK UPDATED") 
        else:
            print("PLEASE ENTER A VALID FOOD ID ")                        


    def delete_food_item(self):
        x=input("ENTER A FOOD ID TO BE DELETED : ")
        if x in self.food.keys():
            del self.food[x]
            print("FOOD ITEM DELETED ")

        else:
            print("INCORRECT FOOD ID ")   


##USER      

    def user_register(self):
        while True:
                user_name = input("Enter your full name : ")
                phone_no = int(input("Enter your  phone number : "))
                email = input("Enter your email id : ")
                password = input("Enter your password : ")
                address = input("Enter your address  ")
                self.user_details = {"User Name": user_name, "Phone No.": phone_no, "Email_ID": email,
                                     "Password": password, "Address": address}
                print("\n!! Your Account is Created Successfully !!\n")
                print(f"Welcome TO {self.restro_name} Restaurant\n")
                print("User Details : ")
                for i in self.user_details:
                    print(i, ":", self.user_details[i])
                break
        

    def user_login(self):
        while True:
                print(f"Welcome TO {self.restro_name} Restaurant\n\n")
                email = input("Enter Your Email ID : ")
                password = input("Enter Your Password : ")
                if len(self.user_details) != 0:
                    if email == self.user_details["Email_ID"] and password == self.user_details["Password"]:
                        print("\n!! Login successfully !!")
                        while True:
                            print("""1. Place New Order\n
                                  2. Check Order History\n
                                  3. Update Your Profile Details\n
                                  4. Exit""")
                            z = input()
                            if z == "1":
                                self.place_order()
                            elif z == "2":
                                self.ordered_history()
                            elif z == "3":
                                self.update_details()
                            elif z == "4":
                                break
                            else:
                                print("invalid Number")
                    else:
                        print("\n!! Incorrect Email or Password!!\n")
                else:
                    print("\n! There is no Account with this Email ID !\n\n!! Please Create Your Account First!!\n")
                    break
                break


    def place_order(self):
        if len(self.food) != 0:
                menu = []
                for items in self.food:
                    menu.append([self.food[items]["Name"], self.food[items]["Quantity"], self.food[items]["Price"]])
                for i in menu:
                    print(i)
                while True:
                    print("\nEnter 1 to Place the Order\nEnter 2 to Exit ")
                    x = input()
                    if x == "1":
                        print("Enter the Food number You want to ordered separated by comma")
                        y = input().split(",")
                        for i in y:
                            z = int(i)
                            if z <= len(menu):
                                self.ordered_item.append(menu[z - 1])
                            else:
                                print("We Don't have this Food Item : ", z)
                        print("List of food item you selected : \n")
                        for j in self.ordered_item:
                            print(j)
                    elif x == "2":
                        break
                    else:
                        print("!! Invalid Number !!\n")
        else:
                print("\n!! Sorry! No Food Items are available Now !!\n")

    def ordered_history(self):
        print("\nList of Previous ordered : ")
        for i in self.ordered_item:
            print(i)
    
    def update_details(self):
            while True:
                print("Select Below Options to Update Your Profile Details\n")
                print("1. Name\n2. Phone number\n3. Email ID\n4. Password\n5. Address\n6. Exit\n")
                x = input()
                if x == "1":
                    self.user_details["User Name"] = input("Enter your updated full name : ")
                    print("\n!! Detail Updated Successfully !!\n")
                elif x == "2":
                    self.user_details["Phone No."] = int(input("Enter your updated 10 digit phone number : "))
                    print("\n!! Detail Updated Successfully !!\n")
                elif x == "3":
                    self.user_details["Email_ID"] = input("Enter your updated email id : ")
                    print("\n!! Detail Updated Successfully !!")

                elif x == "4":
                    self.user_details["Password"] = input("Enter your updated password : ")
                    print("\n!! Detail Updated Successfully !!\n")

                elif x == "5":
                    self.user_details["Address"] = input("Enter your updated address with area PIN code ")
                    print("\n!! Detail Updated Successfully !!\n")

                elif x == "6":
                    break
                else:
                    print("\n!! Invalid Number Entered !!\n")

                if x in ["1", "2", "3", '4', "5"]:
                    for i in self.user_details:
                        print(i, ":", self.user_details[i])
                else:
                    print("\nPlease Enter correct Input\n")

                    
   
o=Restaurent("omkar")
o.add_food_items()
o.view_food_items()