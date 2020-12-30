
from players import get_roster
from league import get_team_ids
import time




if __name__ == "__main__":
    start = time.time()

    f = open("test.txt", "w")


    leagues = []
    for x in range(12086, 12087):
    #for x in range(12086, 12102):  # first and last league num for OTH 2019
        leagues.append(x)

    OTH_team_ids = {}
    for league in leagues:
        OTH_team_ids[league] = get_team_ids(league)


    lap1 = time.time()
    dur = lap1 - start
    print("Have team ids. {:.2f} seconds".format(dur))

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




    f.close()
    end = time.time()
    dur = end - start
    print("Total Elapsed Time: {:.2f} seconds".format(dur))
    # print(OTH_team_ids)
