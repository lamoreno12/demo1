# Laura Moreno
# PSID: 1763766

# define class
class Team:
    # define every single element in the teams
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        # formula
        # team_wins / (team_wins + team_losses)
        # need to return the win percentage with the given formula in zybook

        percentage = self.team_wins / (self.team_wins + self.team_losses)
        return percentage


if __name__ == "__main__":
    # team define by the elements from zybook, zylab 10.14 information
    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team',team.team_name,'has a winning average!')
    else:
        print('Team',team.team_name,'has a losing average.')
