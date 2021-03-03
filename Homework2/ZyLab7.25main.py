# Laura Moreno
# ID 1763766
def exact_change(user_total):  # added by the instructions
    dollars = user_total // 100  # need to define and establish the values of each input
    user_total %= 100
    quarters = user_total // 25  # set and specify the proper format for the money
    user_total %= 25
    dimes = user_total // 10
    user_total %= 10
    nickels = user_total // 5
    user_total %= 5
    pennies = user_total
    return dollars, quarters, dimes, nickels, pennies


# if a define function is given use a return value for the variables declared

if __name__ == '__main__':  # added by instructions
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    if input_val <= 0:
        print('no change')  # by condition if theres no money in
    else:  # if its bigger then process the loop
        if num_dollars > 1:  # if theres more than 1 print the value of it
            print(num_dollars, 'dollars')
        elif num_dollars == 1:  # if its equal then then print the result
            print(num_dollars, 'dollar')
        if num_quarters > 1:
            print(num_quarters, 'quarters')
        elif num_quarters == 1:
            print(num_quarters, 'quarter')
        if num_dimes > 1:
            print(num_dimes, 'dimes')
        elif num_dimes == 1:
            print(num_dimes, 'dime')
        if num_nickels > 1:
            print(num_nickels, 'nickels')
        elif num_nickels == 1:
            print(num_nickels, 'nickel')
        if num_pennies > 1:
            print(num_pennies, 'pennies')
        elif num_pennies == 1:
            print(num_pennies, 'penny')
