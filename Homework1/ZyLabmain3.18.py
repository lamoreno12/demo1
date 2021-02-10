#Laura Moreno
#PSID = 1763766
h = int(input('Enter wall height (feet):\n'))
w = int(input('Enter wall width (feet):\n'))
wall = h * w
print('Wall area:', wall, 'square feet')
paint = (wall / 350)
print('Paint needed:', '{:.2f}'.format(paint), 'gallons')
import math
print('Cans needed:', round(paint), 'can(s)\n')
color = input('Choose a color to paint the wall:\n')
colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}
colort = round(paint) * colors[color]
print('Cost of purchasing', color, 'paint: $''{}'.format(colort))
#add the {}.format because i keep getting a space
# need to * the cans * the colors for the last option since are different values
