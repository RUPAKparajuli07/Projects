shopping = [{"id": 1001, "Name": "HP-AE12", "Available": 100, "Price": 25000, "Original_Price": 24000},
            {"id": 1002, "Name": "DELL", "Available": 100, "Price": 35000, "Original_Price": 34000},
            {"id": 1003, "Name": "ASUS", "Available": 100, "Price": 28000, "Original_Price": 27000},
            {"id": 1004, "Name": "APPLE", "Available": 100, "Price": 60000, "Original_Price": 59000},
            {"id": 1005, "Name": "ACER", "Available": 100, "Price": 24000, "Original_Price": 23000},
            {"id": 1006, "Name": "SAMSUNG", "Available": 100, "Price": 35000, "Original_Price": 34000},
            {"id": 1007, "Name": "OPPO", "Available": 100, "Price": 15000, "Original_Price": 14000},
            {"id": 1008, "Name": "XAOMI", "Available": 100, "Price": 45000, "Original_Price": 44000},
            {"id": 1009, "Name": "HUAWEI", "Available": 100, "Price": 20000, "Original_Price": 19000},
            {"id": 1010, "Name": "VIVO", "Available": 100, "Price": 12000, "Original_Price": 11000}]

shopping1 = shopping
temp = []
order = ""

def adminLoginWindow():
    print("=====================")
    print("1.Display Menu")
    print("2.Add Product")
    print("3.Remove Product")
    print("4.Products goods available")
    print("5.Total Income")
    print("6.Logout")
    print("=====================")


def adminDisplayMenuWindow():
    print("Id\tName\tAvailable\tPrice\tOriginal Price")
    print("====================================================")
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}\t{d["Original_Price"]}')


def addproducts():
    n = int(input("Enter the no.of.items need to be added : "))
    for i in range(n):
        new_id = int(input("Enter id : "))
        new_Name = input("Enter Name : ")
        new_Available = int(input("Enter Available : "))
        new_Price = int(input("Enter Price : "))
        new_original = int(input("Enter the original price : "))
        d = [{"id": new_id, "Name": new_Name, "Available": new_Available, "Price": new_Price,
              "Original_Price": new_original}]
        shopping.extend(d)
        adminDisplayMenuWindow()


def removeproducts():
    dressId = int(input("Enter the id need to be deleted : "))
    found = False
    for d in shopping1:
        found = d["id"] == dressId
        if found != True:
            temp.append(d)
            continue
        if found == True:
            d["Available"] -= 1
    print("Deleting item....")
    if len(temp) == d:
        print(f"{dressId} not found")
    else:
        print(f"{dressId}'s one available is removed from the list")
    adminDisplayMenuWindow()


def availableproducts():
    Total = 0
    print("\n")
    for d in shopping:
        print(f'{d["Name"]} = {d["Available"]}')
        Total += (d["Available"])
    print("\nTotal available goods is : ", Total)


def monthlyincome():
    total = 0
    for d in shopping:
        total += ((d["Available"] * d["Price"]) - (d["Available"] * d["Original_Price"]))
    print("\nTotal income is : ", total)


def logoutwindow():
    login()


def adminOptions():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 2:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        addproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 3:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        removeproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 4:
        availableproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 5:
        monthlyincome()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 6:
        logoutwindow()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()


def userLoginWindow():
    print("=====================\n")
    print("1.Display Menu")
    print("2.Place order")
    print("3.Cancel order")
    print("4.Logout")
    print("\n======================")


def userDisplayMenuWindow():
    print("Id\tName\tAvailable\tPrice")
    print("===================================================")
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')


def user_id():
    userDisplayMenuWindow()
    p_id = int(input("\nEnter the id : "))


def placeOrder():
    order_number = 10
    userDisplayMenuWindow()
    p_id = int(input("\nEnter the id : "))

    for d in shopping:
        if d["id"] == p_id:
            print("\nId\tName\tAvailable\tPrice")
            print("=============================================================")
            print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
            order = '{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}'
            conform = input("\nDo you want to place an order on the above shown product : Y/N ")

            if conform == 'Y' or conform == 'y':
                print("\nSuccessfully placed the order on the product {} {}".format(d["id"], d["Name"]))
                order_number += 1
                print("Your order number is : ", order_number)
                d["Available"] -= 1
                break

            elif conform == 'N' or conform == 'n':
                print("The order is not placed. You can carry on with you purchase. Happy shopping!!!!")
                break
            else:
                print("\nYou have entered wrong option. Please enter again\n")
                conform = input("\nDo you want to place an order on the above shown product : Y/N ")
                break

    if d["id"] != p_id:
        print("\nYou have entered invalid id. Please enter valid id\n")
        user_id()
    print("\nAvailable products : \n")
    userDisplayMenuWindow()


def cancelOrder():
    found = False
    temp = []
    order_id = input("Enter the order id : ")
    for d in shopping:
        found = d["id"] == order_id
        if found != True:
            temp.append(d)
    if len(temp) == d:
        print(f'{order_id} is not found')
    else:
        print(f'{order_id} is removed from the placed order')


def userChoiceOptions():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        userDisplayMenuWindow()
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions()
    elif choice == 2:
        placeOrder()
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions()
    elif choice == 3:
        cancelOrder()
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions()
    elif choice == 4:
        logoutwindow()
    else:
        print("Invalid Choice. Please enter valid choice")


def login():
    tp = input("Login Admin/Login User [Type A to Login in the Admin/ Type U to Login in the User] : ")
    if tp == 'A' or tp == 'a':
        password = input("Enter the password : ")
        if password == "itsmepython":
            adminLoginWindow()
            adminOptions()
        else:
            print("Invalid password. Please enter valid password")

    elif tp == 'U' or tp == 'u':
        password = input("Enter the password : ")
        if (password == "89y3@naeetmkwiSS"):
            userLoginWindow()
            userChoiceOptions()
        else:
            print("Invalid password. Please enter valid password")
    else:
        print("Invalid user type. Enter valid user type")


login()
