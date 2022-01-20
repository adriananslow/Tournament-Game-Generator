def get_number_of_teams():
    num_teams = 0

    while num_teams < 2:
        response = int(input('Enter the number of teams in the tournament: '))
        if response >= 2:
            num_teams = response
            break

        print('The minimum number of games is 2, try again.')
    
    return num_teams

def get_names_of_teams(num_teams):
    teams = {}

    for i in range(1, num_teams + 1):
        teams[i] = None
        while teams[i] == None:
            response = input(f'Enter the name for team #{i}: ')
            if len(response) < 2:
                print('Team names must ahve at least 2 characters, try again.')
                continue
            if len(response.split()) > 2:
                print('Team names may have at most 2 words, try again.')
                continue
            teams[i] = {'Name': response}

    return teams

def get_number_of_games_played(num_teams):
    num_games_played = 0

    while num_games_played < num_teams - 1:
        response = int(input('Enter the number of games played by each teamname for team: '))
        if response < num_teams - 1:
            print('Invalid number of games. Each team plays each other at least once in the regular season, try again.')
            continue
        num_games_played = response

    return num_games_played

def get_team_wins(teams, num_games_played):
    for i in range(1, len(teams) + 1):
        teams[i]['Won'] = None
        while teams[i]['Won'] == None:
            response = int(input(f'Enter the number of wins Team {teams[i]["Name"]} had: '))
            if response < 0:
                print('The minimum number of wins is 0, try again.')
                continue
            if response > num_games_played:
                print(f'The maximum number of wins is {num_games_played}, try again.')
                continue
            teams[i]['Won'] = response

    return teams

def generate_schedule(teams):
    print('Generating the games to be played in the first round of the tournament...')
    sorted_teams =sorted([teams[index] for index in teams], key = lambda x: x['Won'], reverse = True)
    sorted_names = [team['Name'] for team in sorted_teams]
    for i in range(len(teams) // 2):
        print(f'Home: {sorted_names[-1 - i]} VS Away: {sorted_names[i]}')

def main():
    num_teams = get_number_of_teams()
    teams = get_names_of_teams(num_teams)
    num_games_played = get_number_of_games_played(num_teams)
    teams = get_team_wins(teams, num_games_played)
    generate_schedule(teams)


if __name__ == '__main__':
    main()