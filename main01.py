from restaurent import Restaurent

obj = Restaurent("The Royal Kitchen")
print(f"*^*^*^*^*^*^*^*^*^EATZZ*^*^*^*^*^*^*^*^*^*\n")
print(f"__/\__  Welcome To {obj.restro_name} Restaurant  __/\__\n")
print("!!**********************************************************************")
print("\nHello and Welcome \nWhat do you want to order in my Restuarant ? Its a treat from my side :)")
print("***********************************************************************!!\n")

while True:
        print("1. Admin\n2. User\n3. Exit\n")
        x = input()
        if x == "1":
            obj.check_admin()
            while True:
                    print(
                        "1. Add New Food Items\n2. Edit Food Items\n3. View Food Items \n4. Delete Food Items\n5. Exit")
                    y = input()
                    if y == "1":
                        obj.add_food_items()
                    elif y == "2":
                        obj.edit_food_item()
                    elif y == "3":
                        obj.view_food_items()
                    elif y == "4":
                        obj.delete_food_item()
                    elif y == "5":
                        break
                    else:
                        print("Invalid Number")
        elif x == "2":
            while True:
                    print("\nEnter the Below Options\n")
                    print("1. Register\n2. Login\n3. Exit\n")
                    y = input()
                    if y == "1":
                        obj.user_register()
                    elif y == "2":
                        obj.user_login()
                    elif y == "3":
                        break
                    else:
                        print("\nInvalid Number ")
        elif x == "3":
            break
        else:
            print("Invalid Number")