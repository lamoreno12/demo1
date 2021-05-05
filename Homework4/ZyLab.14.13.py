# Laura Moreno
# PSID 1763766

# Global variable
num_calls = 0

# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high),
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary

# define function of partition
def partition(user_ids,i,k):
    x = i - 1
    p = user_ids[k]
    for q in range(i,k): # loop to check range from input and rearrange the output
        if user_ids[q] <= p:
            x = x + 1
            user_ids[x],user_ids[q] = user_ids[q],user_ids[x]
    user_ids[x + 1],user_ids[k] = user_ids[k],user_ids[x + 1]
    return x + 1


# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quisksort() is called
def quicksort(user_ids,i,k):
    if i < k: # check partition and check sort
        p = partition(user_ids,i,k)
        quicksort(user_ids,i,p - 1)
        quicksort(user_ids,p + 1,k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids,0,len(user_ids) - 1)
    num_calls = int(2 * len(user_ids)-1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
