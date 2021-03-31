# Laura Moreno
# PSID: 1763766

# define class from lab name
class ItemToPurchase:
    # default constructor
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    # print method
    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(
            self.item_price * self.item_quantity))


if __name__ == "__main__":

    # create objects
    # get item 1
    print("Item 1")
    item1 = ItemToPurchase()
    item1.item_name = input("Enter the item name:\n") # \nfor space
    # add  integer for numbers
    item1.item_price = int(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))
    print()
    # get item 2
    print("Item 2")
    item2 = ItemToPurchase()
    item2.item_name = input("Enter the item name:\n")
    # add  integer for numbers
    item2.item_price = int(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))

    # get total cost
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

    # print everything
    # print uppercase
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    # print the whole total
    print("\nTotal: $" + str(total_cost))
