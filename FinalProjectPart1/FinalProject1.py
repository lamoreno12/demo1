# Laura Moreno
# PSID: 1763766

# import the necessary commands
import csv
from datetime import date


# using with statement
# define class of the inventory to report
class Inventory:

    # define the method and initiate the list for the files to read
    def __init__(self,i_list):
        self.i_list = i_list

    # first method for full inventory with all the information
    def full_list(self,items):
        with open('FullInventory.csv','w') as file:
            contents = self.i_list
            # sort by manufacture
            f_inventory = sorted(contents.keys())
            # each row should ha item ID, manufacture name, item type, price, service data, damage
            for f in f_inventory:
                # define the name based on processed inventory format
                ID = contents[items]['item_ID']
                m_name = contents[items]['manufacture']
                i_type = contents[items]['item_type']
                price = contents[items]['price']
                s_date = contents[items]['service_date']
                damage = contents[items]['damage']
                # in the respective file write the format required
                file.write('{},{},{},{},{}'.format(ID,m_name,i_type,price,s_date,damage))

    # second output/method:
    def output(self):
        contents = self.i_list
        types = []
        ty = sorted(contents.keys())
        for item in contents:
            i_type = contents[item]['item_type']
            # check for item type otherwise add at the end
            if i_type not in types:
                types.append(i_type)
        # need tp include the inventory and the new file
        for t in types:
            file_name = t + 'LaptopInventory.csv'
            with open(file_name,'w') as file:
                for i in ty:
                    ID = contents[i]['item_id']
                    m_name = contents[i]['manufacture']
                    price = contents[i]['price']
                    s_date = contents[i]['service_date']
                    damage = contents[i]['damage']
                    # variable to check if the item is inside the file
                    i_type = contents[i]['item_type']
                    if t == i_type:
                        file.write('{},{},{},{},{}'.format(ID,m_name,price,s_date,damage,i_type))

    def p_service(self):
        contents = self.i_list
        # trying to sort and also access the date time from the file of its service data
        ps = sorted(contents,date(contents['service_date']))
        with open('PastServiceDateInventory.csv','w') as file:
            for s in ps:
                ID = contents[s]['item_id']
                m_name = contents[s]['manufacture']
                i_type = contents[s]['item_type']
                price = contents[s]['price']
                s_date = contents[s]['service_date']
                damage = contents[s]['damage']
                # trying to add the current date to compare the expire vs new
                act_date = date.today()
                s_expire = date(s_date,'m/d/y')
                expire = s_expire < act_date
                if expire:
                    file.write('{}.{},{},{},{},{}'.format(ID,m_name,i_type,price,s_date,damage))

    # define method for damage in file
    def damage(self):
        contents = self.i_list
        d = sorted(contents.keys())
        with open('DamagedInventory.csv','w') as file:
            for item in d:
                # check for damage according to format
                id = contents[item]['item_id']
                m_name = contents[item]['manufacture']
                i_type = contents[item]['item_type']
                price = contents[item]['price']
                s_date = contents[item]['service_date']
                damage = contents[item]['damage']
                # value expensive in the main menu check
                if damage:
                    file.write('{},{},{},{},{}'.format(id,m_name,i_type,price,s_date,damage))


if __name__ == "__main__":
    products = {}
    # the input files to check the inventory
    files = ['ManufacturerList.csv', 'PriceList.csv','ServiceDatesList.csv']
    for file in files:
        # open file read and select the data to check the require output
        with open(file, 'r') as csv_f:
            csv_f = csv.reader(csv_f)
            for l in csv_f:
                id_i = l[0]
                # check according to the position/location of the data to check the inventory
                if file == files[0]:
                    products[id_i] = {}
                    m_name = l[1]
                    i_type = l[2]
                    damage = l[3]
                    # check for damage
                    products[id_i]['manufacturer'] = m_name
                    products[id_i]['item_type'] = i_type
                    products[id_i]['damage'] = damage
                elif file == files[1]:
                    price = l[1]
                    products[id_i]['price'] = price
                elif file == files[2]:
                    s_date = l[1]
                    products[id_i]['service_date'] = s_date
# not sure about the output


