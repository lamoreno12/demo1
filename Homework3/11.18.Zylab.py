# Laura Moreno
# PSID: 1763766

# get list from user
integer = input().split()
# put new values integers list
no_integer = []

# loop to check the numbers
for i in integer:
    # establish that a number will be used so int is need it
    i = int(i)
    # check if its greater than 0 for negative values
    if i >= 0:
        # add at the end of list
        no_integer.append(i)
# sort list according to loop
no_integer.sort()
# loop to check no integer or negative numbers
for x in no_integer:
    # add end for one line and space
    print(x, end=" ")


