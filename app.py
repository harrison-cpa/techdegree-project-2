import copy

from constants import TEAMS, PLAYERS

players_list = []
balanced_teams_list = {}


def clean_data():
    """ Create a duplicate list of players. 
    Clean up the height and experience of each player so that they are in the correct format.

    create duplicate PLAYERS list named players_list - via for loop
    clean height   
        for each player dict[height], remove " inches" from player
        for each player dict[height], change value type to integer
    experience
        for each player dict[experience], change value type from "YES" or "NO" to boolean
"""
    players_list = [player for player in copy.deepcopy(PLAYERS)]
    for player in players_list:
        if player['experience'] == 'YES':
            player['experience'] = True
        elif player['experience'] == 'NO':
            player['experience'] = False
        player['height'] = int(player['height'][0:2])
        player['guardians'] = player['guardians'].split(' and ')
    return players_list


def balance_teams():
    """add player dicts from player_list to teams in balanced_teams_list. 
    Need to put an even number of players on each team. 

    split players_list to 3 even groups
    add each group to a team in balanced_teams_list
"""
    exp_players_list = [player for player in players_list if player['experience'] == True]
    inexp_players_list = [player for player in players_list if player['experience'] == False]
    num_exp_players_team = int(len(exp_players_list) / len(TEAMS))
    num_inexp_players_team = int(len(inexp_players_list) / len(TEAMS))
    players_distributed = 0
    for team in copy.deepcopy(TEAMS):
        balanced_teams_list[team] = exp_players_list[players_distributed:(players_distributed + num_exp_players_team)]
        players_distributed += num_exp_players_team
    players_distributed = 0
    for team in balanced_teams_list:
        balanced_teams_list[team].extend(inexp_players_list[players_distributed:(players_distributed + num_inexp_players_team)])
        players_distributed += num_inexp_players_team
    return balanced_teams_list
    # Above is not very DRY. Ideas for improving it:
        # Could do two more functions for distributing experienced players and inexperienced players. Then call those functions here.
        # Could make a function for to create an inexperience or experienced list and calculate the number of those players per team. 
            # The function would return both values, which could then be called in the function above. 


def display_team(selection):
    selected_team = TEAMS[selection]
    print(f'\nTeam: {selected_team} Stats\n'+'-'*20)
    selected_team_list = balanced_teams_list[selected_team]
    total_players = len(selected_team_list)
    print(f'Total players: {total_players}')
    total_experienced = 0
    total_inexperienced = 0
    for player in selected_team_list:
        if player['experience'] == True:
            total_experienced += 1
        elif player['experience'] == False:
            total_inexperienced +=1
    print(f'Total experienced: {total_experienced}')
    print(f'Total inexperienced: {total_inexperienced}')
    total_height = 0
    for player in selected_team_list:
        total_height += player['height']
    average_height = round((total_height / total_players),1)
    print(f'Average Height: {average_height}')
    print('\nPlayers on team:')
    short_player_list = [player['name'] for player in selected_team_list]
    print(', '.join(short_player_list))
    print('\nGuardians for team:')
    guardians_list = []
    for player in selected_team_list:
        guardians_list.extend(player['guardians'])
    print(', '.join(guardians_list))
    any_key = input('\nPress ENTER to continue...')


if __name__ == '__main__':
    print('\nBASKETBALL TEAM STATS TOOL')
    players_list = clean_data() 
    balanced_teams_list = balance_teams()
    # for each team print:
        # teams name (as a string)
        # total players on the team (as an integer)
        # the player names as strings, separated by commas
    # may need for teams_list to include iterable data for below to work.
    while True:
        print('\n'+'-'*4+'MENU'+'-'*4)
        print("\nHere are your choices:")
        print("1) Display Team Stats")
        print("2) Quit\n")
        try:
            user_selection = int(input("Enter an option > "))
            if user_selection != 1 and user_selection != 2:
                raise ValueError
        except ValueError:
                print("\nSorry that choice is not available. You must select either 1 or 2.\nBelow is the menu again.\n\n|\nV")
        if user_selection == 2:
            print('\nHave a great day!\n')
            break
        elif user_selection == 1:
            while True:
                print('')
                print('Teams:\n'+'-'*12)
                team_number = 1
                for team in TEAMS:
                    print(f'{team_number}) {team}')
                    team_number += 1
                print('')
                try:
                    team_selection = int(input('Enter an option > '))
                    if team_selection not in range(1, team_number):
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print("Oops, that's not one of the available teams. Please enter one of the numbers below.\n\n|\nV")
                    continue
            display_team(team_selection-1)
            # team_number = 0
            continue
    # Make sure this is not needed:
    # for team in balanced_teams_list:
    #     print(f'\nTeam: {team}')
    #     print(f'# of Players: {len(balanced_teams_list[team])}')
    # print('')
            