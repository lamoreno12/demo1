#Laura Moreno
#PSID = 1763766
lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))
print()
print('Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(nectar), 'cup(s) agave nectar\n')

make = float(input('How many servings would you like to make?\n'))
print()
print('Lemonade ingredients - yields', '{:.2f}'.format(make), 'servings')
print('{:.2f}'.format(lemon_juice * make/servings), 'cup(s) lemon juice')# have to adjust the amount for the ingredient
print('{:.2f}'.format(water * make/servings), 'cup(s) water')
print('{:.2f}'.format(nectar * make/servings), 'cup(s) agave nectar\n')

print('Lemonade ingredients - yields', '{:.2f}'.format(make), 'servings')
print('{:.2f}'.format(lemon_juice * make/servings/16), 'gallon(s) lemon juice')
print('{:.2f}'.format(water * make/servings/16), 'gallon(s) water')
print('{:.2f}'.format(nectar * make/servings/16), 'gallon(s) agave nectar')

