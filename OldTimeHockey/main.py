import time
import requests
import csv

def get_team_ids(league):

    """
    This sub gets all team_ids for a given league.

    :param league: integer FF league_id
    :return: returns a list of team_ids in the passed league_id

    Future Improvements: classes/subclasses to get more information from this view
    """


    params = {}
    params['sport'] = 'NHL'
    params['league_id'] = league
    params['season'] = 2019

    url = 'https://www.fleaflicker.com/api/FetchLeagueRosters'

    r = requests.get(url, params)  #Fetch LeaguePlayerListing

    r_json = r.json()  # json

    LeagueRoster = r_json['rosters']

    team_ids = []
    for a in LeagueRoster:
        b = a['team']
        team_ids.append(b['id'])  # pull just team id, append to return list


    r.close()
    del r
    return team_ids

def get_roster(league_id, team_id):
    """
    This function is used to get players rostered by a specific team

    :param: int league_id, int team_id
    :return: [player_ids]

    Future Improvements: classes?, clean up code
    """

    params = {}
    params['sport'] = 'NHL'
    params['league_id'] = league_id
    params['team_id'] = team_id
    params['season'] = 2019

    url = 'https://www.fleaflicker.com/api/FetchRoster'

    r = requests.get(url, params)  #Fetch LeaguePlayerListing

    r_json = r.json()  # json
    RosterGroup = r_json['groups']  # ws.flea.api.RosterGroup, 3 dicts, 0:starting 1:bench 2:injured

    Starting_Slots = RosterGroup[0]['slots']
    Bench_Slots = RosterGroup[1]['slots']


    try:  # teams w/o IR players do not have an injured roster group
        Injured_Slots = RosterGroup[2]['slots']
        position_slots = [Starting_Slots, Bench_Slots, Injured_Slots]
    except IndexError:
        position_slots = [Starting_Slots, Bench_Slots]

    roster = []
    for group in position_slots:
        for slot in group:
            try:
                temp = slot['leaguePlayer']
            except KeyError:
                continue
            temp = temp['proPlayer']['id']
            #temp = temp['id']
            roster.append(temp)

    r.close()
    del r
    return roster



def get_rostered_players(leagues):
    """
    This function is used to record all rostered players in the provided list of leagues.
    Output is a csv file containing player_ids.

    :param leagues: list of leagues to get rostered players
    :return: .csv of rostered player_ids w/o duplicates

    Future Improvement: include player name, use this as a id:name master list
    Future Improvement: include league and team as columns
    """


    all_rosters = {}
    league_rosters = {}
    for league in leagues:
        team_list = get_team_ids(league)
        for team in team_list:
            league_rosters[team] = get_roster(league, team)
        all_rosters[league] = league_rosters.copy()
        league_rosters.clear()

    check1 = time.time()
    dur = check1 - start
    print("Have all rosters. {:.2f} seconds".format(dur))


    all_rostered_players = []
    for league in all_rosters:
        #print(league, all_rosters[league])
        for roster in all_rosters[league].values():
            for player in roster:
                all_rostered_players.append(player)



    temp = all_rostered_players.copy()
    all_rostered_players.clear()
    for player in temp:
        if player not in all_rostered_players:
            all_rostered_players.append(player)
    del temp
    check2 = time.time()
    dur = check2 - check1
    print("Removed duplicates. {:.2f} seconds".format(dur))


    fields = ['player_id']

    rows = []
    for player in all_rostered_players:
        temp = [player]
        rows.append(temp)

    print(rows)


    filename = "rostered_players.csv"  # output data as csv
    with open(filename, 'w', newline='') as csvfile:  # need newline param because windows
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)



    #lap2 = time.time()
   # dur = lap2 - start
    #print("Have team ids. {:.2f} seconds".format(dur))



    """
    for team in temp_all_rosters:
        a = temp_all_rosters[team]
        for player_id in a:
            f.write("Team: {:}, ID: {:}, Name: {:}".format(team, player_id, a[player_id] + "\n"))
    """


    end = time.time()
    dur = end - start
    print("Total Elapsed Time: {:.2f} seconds".format(dur))
    # print(OTH_team_ids)




if __name__ == "__main__":
    start = time.time()



    leagues = []
    for x in range(12086, 12088):  # this will eventually become an argument list
    #for x in range(12086, 12102):  # first and last league num for OTH 2019
        leagues.append(x)

    get_rostered_players(leagues)


