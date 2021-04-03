# Laura Moreno
# PSID: 1763766

# define class for soccer list
# have issues with the code as a infinite loop
# not complete just basic

details = {}


# start and base of the code not fully finish
def Get_players(self):
    for i in range(1,6):
        j = int(input("Enter player {}'s jersey number:",i))
        r = int(input("Enter player {}'s ratings:",i))
        self.details[j] = r


# define and implement the menu
def Print_menu(self):
    print("\nMENU\n"
          "a - Add player\n"
          "d - Remove player\n"
          "u - Update player rating\n"
          "r - Output players above a rating\n"
          "o - Output roster\n"
          "q - Quit\n")
    option = input("\nChoose and option: ")
    return option


# define Output roaster
def Output_Roaster(self):
    s_j = sorted(self.details.keys())
    print("ROSTER")
    for jer in s_j:
        print("Jersey number: {} , Rating: {}".format(jer,self.details[jer]))


# define the new player to details list
def Add_player(self):
    j = int(input("Enter a new player's jersey number:"))
    r = int(input("Enter the player's rating:"))
    self.details[j] = r


# delete player method
def Delete_player(self):
    j = int(input("Enter a jersey number: "))
    del self.details[j]


# if a user choose a new player add to the list
def Update_player_rating(self):
    j = int(input("Enter a jersey number: "))
    n_r = int(input("Enter a new rating for player: "))
    self.details[j] = n_r


# from instruction define the output to show players
def Output_players_above(self):
    r = int(input("Enter a rating"))
    s_j = sorted(self.details.keys())
    print("ABOVE {}".format(r))
    for j in s_j:
        if self.details[j] > r:
            print("Jersey number: {}, Rating:{}".format(j,self.details[j]))


if __name__ == "__main__":

    # menu to print the options menu to choose what the user wants
    Get_players(details)
    choose = Print_menu()
    while choose != "q":
        if choose == "a":
            Add_player()
        elif choose == 'd':
            Delete_player()
        elif choose == 'u':
            Update_player_rating()
        elif choose == 'r':
            Output_players_above()
        elif choose == "o":
            Output_Roaster()
