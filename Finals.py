import os
#Finals
#IT100L
#Kenneth Kim Castro


#The menu of the list
menu = [["M1", "Adobong Manok/rice", 50],["M2", "Sinigang Baboy/rice", 60],["M3", "Afritadang Baboy/rice", 60],["M4", "Kalderetang Baka/rice", 80],["M5", "Hamunadong Baka/rice", 50],
    ["D1", "Coke", 20],["D2", "Pepsi", 20],["D3", "Sprite", 20],["D4", "Mountain Dew", 20],["D5", "Rootbeer", 20],]


def bura():  #Use to clear some codes on output
    os.system( 'cls' )

#List of the items you ordered
Cart_list = []
#Main class
class mainclass:
    
    Total_payment = 0
    Item_name = None
    items = 0

    
    def payment(self):  #Payment
        try:
            cash = 0
            while self.Total_payment > cash:
                try:
                    bura()
                    mainclass.Display()
                    mainclass.cart()
                    cash = 0
                    cash = int(input("Your money input: "))
                    if self.Total_payment > cash:
                        print("You have Insufficient money")
                except:
                    print("Error!")
                    continue
            if self.Total_payment < cash:
                change = cash - self.Total_payment
                print(f"Your Change: {change} Pesos")
                print("Thank you for ordering!")
        except ValueError:
            print("\nerror")
            print("Error has occured")

        print("Thanks for ordering")
    

    @staticmethod
    def Display(): #Display the list
        print("\n******************************************************")
        print(" "+ "{: ^13} {: ^23} {: ^15}".format("Item_Code", "Product", "Price")+ " ")
        for item in menu:
            print("** "+"{: ^10} {: ^26} {: ^10}".format(*item)+ " **")
        print("\n******************************************************")
        print("\nType [D] if your done ordering and [R] if you want to remove an order")
        

    @classmethod
    def GetTotalPrice(cls): #Getting the total price
        cls.Total_payment = 0
        for row, customer_items in enumerate(
            Cart_list):
            cls.Total_payment += Cart_list[row][3]
        print("\n{: >38}".format(f"TOTAL: {cls.Total_payment}"))

    @classmethod
    def split_string(cls, inputs): #To split the input string
        x = inputs.split(" ")
        print(x)
        cls.Item_name = x[0]
        cls.items = int(x[1])

    @classmethod
    def cart(cls): #Your orders
        print("\n******************************************************")
        print("{: ^10} {: ^10} {: ^20} {: ^10}".format(
            "Item_Code", "Qty", "Price", "Total"))

        for customer_items in Cart_list:
            print("{: ^5} {: ^20} {: ^10} {: ^10}".format(
                *customer_items))
        cls.GetTotalPrice()
        print("\n******************************************************")
        print("Type [Code] [Quantity]")

    @classmethod
    def Remove_Items(cls): #Remove Orders
        input_item_code = input("Enter Item Code to remove: ").upper()
        cls.split_string(input_item_code)
        for row, data in enumerate(Cart_list):
            if cls.Item_name == Cart_list[row][0]:
                if Cart_list[row][1] > 1:
                    Cart_list[row][1] = Cart_list[row][1] - cls.items
                    Cart_list[row][3] = Cart_list[row][2] * Cart_list[row][1]
                    if Cart_list[row][1] < 1:
                        Cart_list.pop([row][0])
                else:
                    Cart_list.pop([row][0])
                break
        cls.cart()
    @classmethod
    def order(cls): #My order list
        total = 0
        for a, b in enumerate(menu):
            for c, d in enumerate(b):
                if cls.Item_name == d:
                    existing = False
                    num_row = 0
                    for row, data in enumerate(Cart_list):
                        if Cart_list[row][0] == menu[a][c]:
                            existing = True
                            num_row = row
                            break
                    total = cls.items * menu[a][c + 2]
                    if existing:
                        Cart_list[num_row][1] += cls.items
                        Cart_list[num_row][3] += total
                    else:
                        temp_cart = [None, None, None, total]
                        temp_cart[0] = (menu[a][c])
                        temp_cart[1] = cls.items
                        temp_cart[2] = (menu[a][c + 2])
                        Cart_list.append(temp_cart)
loop = None
while loop != "N":
    try:
        bura()
        mainclass.Display()
        mainclass.cart()
        loop = input("Enter Code and Quantity: ").upper()

        if loop == "R":
            mainclass.Remove_Items()
        elif loop == "D":
            mainclass().payment()
            loop = "N"
        else:
            mainclass.split_string(loop)
            mainclass.order()
    except:
        pass



