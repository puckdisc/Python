import requests
import time

def get_roster(team_id):
    params = {}
    params['sport'] = 'NHL'
    params['league_id'] = 12093
    params['team_id'] = team_id
    params['season'] = 2019

    url = 'https://www.fleaflicker.com/api/FetchRoster'

    r = requests.get(url, params)  #Fetch LeaguePlayerListing

    r_json = r.json()  # json

    RosterGroup = r_json['groups']  # ws.flea.api.RosterGroup, 3 dicts, 0:starting 1:bench 2:injured

    Starting_Slots = RosterGroup[0]
    Starting_Slots = Starting_Slots['slots']
    Bench_Slots = RosterGroup[1]
    Bench_Slots = Bench_Slots['slots']
    Injured_Slots = RosterGroup[2]
    Injured_Slots = Injured_Slots['slots']

    position_slots = []
    position_slots.append(Starting_Slots)
    position_slots.append(Bench_Slots)
    position_slots.append(Injured_Slots)

    temp_player_dict = {}
    player_dict = {}

    for z in position_slots:
        for a in z:
            Player = a['leaguePlayer']
            Player = Player['proPlayer']  # digging into nested items to produce {id : name}
            temp_player_dict[Player['id']] = Player['nameFull']  # produces duplicate entries

    for key, value in temp_player_dict.items():  # getting rid of duplicates
        if key not in player_dict.keys():
            player_dict[key] = value

    r.close()
    del r

    return player_dict


if __name__ == "__main__":
    start = time.time()
    print(get_roster(63182))

    end = time.time()
    dur = end - start
    print("{:.2f} seconds".format(dur))

