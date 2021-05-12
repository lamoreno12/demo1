# Laura Moreno
# PSID: 1763766

# import the necessary commands
import csv
from datetime import date
# this will work if the service data list is call and then the condition check for the date list
import csv

# using with statement
items = {} # list to storage the items that are going to be read from the file
files = ['ManufacturerList.csv','PriceList.csv','ServiceDatesList.csv']
for f in files:
    with open(f,'r') as csv_file: # open and read the files
        csv_read = csv.reader(csv_file,delimiter=',')
        for line in csv_read: # check for every word/line in the file and define each name
            item_id = line[0]
            if f == files[0]: # check the first file to read
                items[item_id] = {} # from items list define
                man_name = line[1] # first line of file represents manufactures name
                item_type = line[2] # second line of file represents item type (laptop or phone)
                items[item_id]['manufacturer'] = man_name.strip()
                items[item_id]['item_type'] = item_type.strip()
            elif f == files[1]: # checks the second file
                price = line[1]  # first line of code is the price, however the actual first thing is the id #
                items[item_id]['price'] = price
            elif f == files[2]: # checks the third file
                s_date = line[1]   # first line check the date the service was provide
                items[item_id]['service_date'] = s_date

manufactures = [] # checks for the manufactures inside the files
types = [] # check and storage the types from the files

# used to check that manufacture and item type are including in the check
# this allows us to see if they match with the given file
for item in items:
    check_m = items[item]['manufacturer'] # loop to check if item are inside the file
    c_t = items[item]['item_type']
    if check_m not in types: # if not in manufactures then ask the question
        manufactures.append(check_m)
    if c_t not in types: # if not in types then ask question and add to the end
        types.append(c_t)

u_input = None # define input as none
while u_input != 'q': # while statement to check inside the condition that everything runs while theres no q selected
    u_input = input("Enter item manufacturer and item type or q to quit:\n")
    if u_input == 'q': # condition
        break # if the condition is met then exit the code
    else:
        s_manuf = None # define variables
        s_type = None
        u_input = u_input.split() # space between each other
        b_input = False
        for word in u_input: # check each word from input and verify in loop
            if word in manufactures:
                if s_manuf:
                    b_input = True
                else:
                    s_manuf = word
            elif word in types:
                if s_type:
                    b_input = True
                else:
                    s_type = word
        if not s_manuf or not s_type or b_input: # if the word doesnt match then the item then is not in the file
            print("No such item in inventory")
        else:
            #    keys = sorted(items.keys())
            mat_item = []
            consider = []
            # check for damage item to not add in the list

            if mat_item: # if the input of the user match the item the establish connection and print accordingly
                item = mat_item[0]
                item_id = item[0]
                man_name = item[1]['manufacturer']
                item_type = item[1]['item_type']
                price = item[1]['price']
                print("Your item is: {}, {}, {}, {}\n".format(item_id,man_name,item_type,price))

            if consider: # if they have similar items or references then print the consider items to view from file
                item = consider[0]
                item_id = item[0]
                man_name = item[1]['manufacturer']
                item_type = item[1]['item_type']
                price = item[1]['price']
                print("You may also consider: {},{},{},{}\n".format(item_id,man_name,item_type,price))
                # the code runs but doesnt print the item is option or the may consider option.
