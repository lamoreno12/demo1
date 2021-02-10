# Laura Moreno
# PSID = 1763766
menu = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12,
    '-': " "
}
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print()
service_1 = input('Select first service:\n')
service_2 = input('Select second service:\n')
print()
print("Davy's auto shop invoice\n")

total = 0
if service_1 == '-':
    print('Service 1: No service')
else:
    print('Service 1: ' + service_1 + ', $' + str(menu[service_1]))
    # add the {:}.format because i keep getting a space between the $ and the #
    # add + sign to add the comma together
if service_2 == '-':
    print('Service 2: No service')
else:
    print('Service 2: ' + service_2 + ', $' + str(menu[service_2]))
print()
total = menu[service_1] + menu[service_2]
# this will give the the result with services

#total = str(menu[service_1]) + str(menu[service_2])
#this will give me the result with no service

#if change to str it will change my sum and produce an error
#have trouble setting the sum to work propertly if i change the str
print('Total:', '$''{}'.format(str(total)))
