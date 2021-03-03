# Laura Moreno
# ID 1763766

import csv # add the import module since a file needs to be read

filename = input() # ask user for filename
frequency = {} # dictionary to store the frequency the
# file = open(filename, 'r'), use the with statement to open because is a list
with open(filename, 'r') as file:
    reader = csv.reader(file) # use the csv to read from file
    for line in reader: # for loop to specify what we want to get from the file
        for word in line:
            if word in frequency: # for every word then count the frequency which it repeats
                frequency[word] = frequency[word] + 1
            else:
                frequency[word] = 1
for word in list(frequency.keys()): # use keys() to return the object in the dictionary
    print(word, frequency[word])  # from the file print the list and the frequency
file.close()
