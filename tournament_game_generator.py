def get_number_of_teams():
    while True:
        num_teams = int(input('Enter the number of teams in the tournament: '))
        if num_teams >= 2:
            break

        print('The minimum number of games is 2, try again.')
    return num_teams

def get_names_of_teams(num_teams):
    team_names = []

    for i in range(num_teams):
        while True:
            name = input(f'Enter the name for team #{i + 1}: ')
            if len(name) >= 2 and len(name.split()) <= 2:
                team_names.append(name)
                break
            elif len(name) < 2:
                print('Team names must have at least 2 characters, try again.')
            elif len(name.split()) > 2:
                print('Team names may have at most 2 words, try again.')
    return team_names

def get_number_of_games_played(num_teams):
    while True:
        num_games_played = int(input('Enter the number of games played by each team: '))
        if num_games_played >= num_teams - 1:
            break

        print('Invalid number of games. Each team plays each other at least once in the regular season, try again.')
    return num_games_played

def get_team_wins(num_teams, team_names, num_games_played):
    team_wins = []

    for i in range(num_teams):
        while True:
            wins = int(input(f'Enter the number of wins Team {team_names[i]} had: '))
            if wins >= 0 and wins <= num_games_played:
                team_wins.append(wins)
                break
            elif wins < 0:
                print('The minimum number of wins is 0, try again.')
            elif wins > num_games_played:
                print(f'The maximum number of wins is {num_games_played}, try again.')
    return team_wins

def generate_schedule(team_names, team_wins, num_teams):
    print('Generating the games to be played in the first round of the tournament...')
    team_names_wins = list(zip(team_names, team_wins))
    team_names_wins.sort(key = lambda x: x[1], reverse = True)
    for i in range(num_teams // 2):
        print(f'Home: {team_names_wins[-1 - i][0]} VS Away: {team_names_wins[i][0]}')

def main():
    num_teams = get_number_of_teams()
    team_names = get_names_of_teams(num_teams)
    num_games_played = get_number_of_games_played(num_teams)
    team_wins = get_team_wins(num_teams, team_names, num_games_played)
    generate_schedule(team_names, team_wins, num_teams)

if __name__ == '__main__':
    main()