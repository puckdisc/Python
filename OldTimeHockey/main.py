import draft
from players import get_roster
from league import get_team_ids
import time




if __name__ == "__main__":
    start = time.time()

    leagues = []
    for x in range(12086, 12102):  # first and last league num for OTH 2019
        leagues.append(x)

    OTH_team_ids = {}
    for a in leagues:
        OTH_team_ids[a] = get_team_ids(a)


    """
    temp_all_rostered = {}
    for a in OTH_team_ids:
        print(a)
        b = get_roster(a)
        for key, value in b:
            temp_all_rostered[key] = value
    """




    end = time.time()
    dur = end - start
    print("{:.2f} seconds".format(dur))
    print(OTH_team_ids)
