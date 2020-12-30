import requests


def get_team_ids(league):

    """
    :param league: league_id
    :return: returns a list of team_ids in the league
    """


    params = {}
    params['sport'] = 'NHL'
    params['league_id'] = league
    params['season'] = 2019

    url = 'https://www.fleaflicker.com/api/FetchLeagueRosters'

    r = requests.get(url, params)  #Fetch LeaguePlayerListing

    r_json = r.json()  # json

    LeagueRoster = r_json['rosters']

    temp = []
    team_ids = {}
    for a in LeagueRoster:
        b = a['team']
        temp.append(b['id'])  # pull just team id, append to return list
    team_ids[league] = temp

    r.close()
    del r
    return team_ids



if __name__ == "__main__":
    get_team_ids(12093)
