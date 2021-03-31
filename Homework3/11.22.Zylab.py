# Laura Moreno
# PSID: 1763766

# get words from user and split to have space between each other
word = input().split(" ")
# loop to check every word and each "i" will print the count of the word
for i in word:
    print(i, word.count(i))


