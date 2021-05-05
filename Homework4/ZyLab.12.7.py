# Laura Moreno
# PSID 1763766

# define function to et the age from user
def get_age():
    age = int(input())
    if 18 <= age <= 75:  # check the range between the age
        return age
    else:  # if the age doesnt match in range print error
        raise ValueError("Invalid age.")


# define function for burning heart rate
def fat_burning_heart(age):
    heart_rate = (220 - age) * 0.7  # calculate rate of fat
    return heart_rate


if __name__ == "__main__":
    # using handling exceptions to detect an error while calculating
    try:
        age = get_age()
        heart_rate = fat_burning_heart(age)
        print("Fat burning heart rate for a",age,"year-old:",heart_rate,"bpm")
    except ValueError as x:
        print(x)
        print("Could not calculate heart rate info.\n")
