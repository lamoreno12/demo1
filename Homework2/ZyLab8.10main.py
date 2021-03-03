# Laura Moreno
# ID 1763766

word = input()  # get the word from the user
# word.replace(" ", "")  # according to the hint remove spaces
# if spaces are not remove then the editor think is a palindrome
palindrome = ""  # define variables to see if it work
no_palindrome = ""  # see if it doesnt work
for x in word:  # loop to check the string enter will met the requirements
    if x != ' ':  # check if the word is equivalent to its reverse or if it changes
        # if the space is not define then the editor thinks is not a palindrome
        palindrome += x  # add to the correct if its true
        no_palindrome = x + no_palindrome  # add to see if its no palindrome
if palindrome == no_palindrome:  # if statement to check if the palindrome condition is true
    print(word, 'is a palindrome')  # proceed to print if is true or not
else:
    print(word, 'is not a palindrome')
