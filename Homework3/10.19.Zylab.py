# Laura Moreno
# PSID: 1763766

# define class for item to purchase
class ItemToPurchase:
    # default constructor
    def __init__(self,name='none',price=0,quantity=0,description='none'):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    # print method
    def print_item_cost(self):
        t = self.item_price * self.item_quantity
        print('%s %d @ $%d = $%d' % (self.item_name,self.item_quantity,self.item_price,t))

    # print for description
    def print_item_description(self):
        print('%s',self.item_name,self.item_description)


# built shopping class
class ShoppingCart:
    pass

    # define all methods
    def __init__(self,customer_name='none',current_date='January 1,2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # to add the item to the shop list
    def add_item(self,item_get):
        self.cart_items.append(item_get)

    # need to define and declare parameter
    def remove_item(self,i_name):
        no_item = False
        for x in self.cart_items:
            # check if the item selected by user is in the cart or not
            if x.item_name == i_name:
                self.cart_items.remove(x)
                no_item = True
                break
            if not no_item:
                print('Item not found in cart. Nothing removed.')

    # modify the shopping list to add items from user
    def modify_item(self,item_get):
        flag = False
        for i in self.cart_items:
            if i.item_name == item_get:
                flag = True
                quantity = input("Enter the new quantity: \n")
                i.item_quantity = quantity
                break
        # check parameter to see if its meet the requierments
        if not flag:
            print("Item not found in cart. Nothing modified.")

    # check how many items are in the cart
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    # check the amount from user for price
    def get_cost_of_cart(self):
        cost_of_cart = 0
        for item in self.cart_items:
            cost_of_cart += item.item_quantity * item.item_price
        return cost_of_cart

    # print if the car have change and the total of the new items included in the list
    def print_total(self):
        cost_of_cart = self.get_cost_of_cart()
        if cost_of_cart == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name,self.current_date))
            print("Number of Items: %d\n" % self.get_num_items_in_cart())
            for item in self.cart_items:
                item.print_item_cost()

            print("\nTotal: $%d" % cost_of_cart)

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(self.customer_name + "'s Shopping Cart -" + self.current_date)
            print("Number of Items: ",self.get_num_items_in_cart())
            for item in self.cart_items:
                item.print_item_description()


# menu to ask user their option and within each command it will call the def parameter and execute the method
# some options or within the code have create repetition
def print_menu(shopcart):
    client = shopcart
    menu = ("\nMENU\n"
            "a - Add item to cart\n"
            "r - Remove item from cart\n"
            "c - Change item quantity\n"
            "i - Output items' descriptions\n"
            "o - Output shopping cart\n"
            "q - Quit\n")
    option = " "
    while option != "q":
        print(menu)
        option = input('Choose an option:\n')
        while option != "a" and option != "r" and option != "c" and option != "i" and option != "o" and option != "q":
            option = input("Choose an option:\n ")
        if option == "a":
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = int(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            item_get = ItemToPurchase(item_name,item_price,item_quantity,item_description)
            client.add_item(item_get)
        elif option == "r":
            print("REMOVE ITEM FROM CART")
            i_name = input("Enter name of item to remove:\n")
            client.remove_item(i_name)
        elif option == "c":
            print("\nCHANGE ITEM QUANTITY")
            i_name = input("Enter the item name:\n")
            qu = int(input("Enter the new quantity:\n"))
            item_get = ItemToPurchase(i_name,0,qu)
            client.modify_item(item_get)
        elif option == "i":
            print("\nOUTPUT ITEM'S DESCRIPTIONS")
            client.print_descriptions()
        elif option == "o":
            print("\nOUTPUT SHOPPING CART")
            client.print_total()


# main menu for user to first select the 1st option follow the menu
if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print("\nCustomer name:",customer_name)
    print("Today's date:",current_date)
    cart = ShoppingCart(customer_name,current_date)
    print_menu(cart)
