
from players import get_roster
import time
import requests

def get_team_ids(league):

    """
    :param league: integer FF league_id
    :return: returns a list of team_ids in the passed league_id
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









if __name__ == "__main__":
    start = time.time()

    f = open("test.txt", "w")


    leagues = []
    for x in range(12086, 12088):  # this will eventually become an argument list
    #for x in range(12086, 12102):  # first and last league num for OTH 2019
        leagues.append(x)

    OTH_team_ids = {}
    for league in leagues:
        OTH_team_ids[league] = get_team_ids(league)
    print(OTH_team_ids)


    lap1 = time.time()
    dur = lap1 - start
    print("Have team ids. {:.2f} seconds".format(dur))
    """
    temp_all_rosters = {}
    for league in OTH_team_ids.keys():
        for team in OTH_team_ids[league]:
            lap1 = time.time()
            temp_all_rosters[team] = get_roster(league, team)
            lap2 = time.time()
            dur = lap2 - lap1
            print("Got roster for {:} in {:.2f} sec".format(team, dur))


    for team in temp_all_rosters:
        a = temp_all_rosters[team]
        for player_id in a:
            f.write("Team: {:}, ID: {:}, Name: {:}".format(team, player_id, a[player_id] + "\n"))
    """


    f.close()
    end = time.time()
    dur = end - start
    print("Total Elapsed Time: {:.2f} seconds".format(dur))
    # print(OTH_team_ids)
