# Laura Moreno
# ID 1763766

# define variables for 1st equation
q = int(input()) # if int is not used, then the  print is no solution
w = int(input()) # i think is because the editor thinks is a string
e = int(input())
# define variables for 2nd equation
a = int(input())
s = int(input())
d = int(input())

works = False # use a boolean statement to verify is the equation is working
# from the brute force approach to get the values of x and y
for x in range(-10, 11): # its from -10 to 10, however a extra # is added to the range
    for y in range(-10, 11):
        if ((q * x) + (w * y) == e) and ((a * x) + (s * y) == d):
            # set up the equation based on the input to find x and y in the loop
            print(x, y)
            works = True
            break # allows the boolean to check if the statement is true or not
if not works: # if it didnt work no solution
    print('No solution')
