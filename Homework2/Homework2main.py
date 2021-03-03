# Laura Moreno
# ID 1763766
# Part A
# import datetime or  need to change the date format
# need to revise and improve, need to be more responsible with time and due dates
# ask questions
dates = {'January':1,'February':2, 'March':3, 'April':4, 'May':5,
         'June':6, 'July':7, 'August':8, 'September':9, 'October':10,
         'November':11, 'December':12} # dictionary for month and numbers
day = dates[1].split() # need to define from dictionary from str to int
month = dates[0].split() # from dictionary in dates
year = dates[-1].split() # from file the last part is consider the year
new_date = month, '/', day, '/', year # change the format
# need to properly change the new_date format a
# by datetime module do we import? or the format can change
# Part B
with open('inputDates.txt', 'r') as file: # open and read files
    for x in file.read():
        if x != '-1': # check to parse the string
            list = x.split() # separate the list, new list?
            print(x)

file.close()
# Part C
with open('parsedDates.txt','w') as file2: # open and read
    file2.write(new_date) # the dates from the 1st file goes to the new file2
file2.close()
