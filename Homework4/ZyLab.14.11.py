# Laura Moreno
# PSID 1763766

# define function to check sort
def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):  # for loop to check range in numbers
        max_n = i
        for y in range(i + 1, len(numbers)):  # loop to check and put the numbers in the sort position
            if numbers[max_n] < numbers[y]:
                max_n = y
        numbers[i],numbers[max_n] = numbers[max_n],numbers[i]
        for x in numbers:
            print(x, end=" ")  # space between each result
        print()  # print so it gives space in column to each answer
    return numbers


if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]  # for the list of numbers get input from user and go to the loop
    selection_sort_descend_trace(numbers)
