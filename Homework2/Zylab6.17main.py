# Laura Moreno
# ID 1763766
letter = input()
password = ''

for i in letter:  # loop to change the input letter to new password
    if i == 'i':  # replace i to the new letter in the variable password
        password += '!'  # use regulate if/elif statements
    elif i == 'a':
        password += '@'
    elif i == 'm':
        password += 'M'
    elif i == 'B':
        password += '8'
    elif i == 'o':
        password += '.'
    else:
        password += i  # if other letters are used just print them in the i password

password += 'q*s'  # from the loop the password add the q*s at the end
print(password)  # print the loop of the password + changes
